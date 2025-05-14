# -------------------------------------------------------------------------- #
# Copyright 2025-present, Federation Manager, by Software Networks, i2CAT    #
#                                                                            #
# Licensed under the Apache License, Version 2.0 (the "License"); you may    #
# not use this file except in compliance with the License. You may obtain    #
# a copy of the License at                                                   #
#                                                                            #
# http://www.apache.org/licenses/LICENSE-2.0                                 #
#                                                                            #
# Unless required by applicable law or agreed to in writing, software        #
# distributed under the License is distributed on an "AS IS" BASIS,          #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.   #
# See the License for the specific language governing permissions and        #
# limitations under the License.                                             #
# -------------------------------------------------------------------------- #

import connexion
import six
import json

from models.app_app_id_body import AppAppIdBody  # noqa: E501
from models.app_identifier import AppIdentifier  # noqa: E501
from models.application_onboarding_body import ApplicationOnboardingBody  # noqa: E501
from models.federation_context_id import FederationContextId  # noqa: E501
from models.inline_response2007 import InlineResponse2007  # noqa: E501
from models.problem_details import ProblemDetails  # noqa: E501
from models.zone_identifier import ZoneIdentifier  # noqa: E501
import util
from models.mongo_document import OriginatingOperatorPlatform
from models.mongo_document import OriginatingArtefactManagement
from models.mongo_document import OriginatingApplicationOnboardingManagement
from models.mongo_document import OriginatingApplicationOnboardingManagementUpdate
from models.mongo_document import OriginatingZoneInfo
from models.mongo_document import OriginatingApplicationDeploymentManagement

from models.mongo_document import OriginatingOperatorPlatformOriginatingOP
from models.mongo_document import OriginatingApplicationOnboardingManagementOriginatingOP
from models.mongo_document import OriginatingApplicationOnboardingManagementUpdateOriginatingOP

from flask import abort
from clients import i2edge

from configparser import ConfigParser
from clients import fed_manager as fm_client

CONFIG = ConfigParser()
CONFIG.read("conf/config.cfg")
roleOp = CONFIG.get("partner_op", "role")

operation_POST = "POST"
operation_PATCH = "PATCH"


def delete_app(federation_context_id, app_id):  # noqa: E501
    """Deboards the application from any zones, if any, and deletes the App.

     # noqa: E501

    :param federation_context_id:
    :type federation_context_id: dict | bytes
    :param app_id:
    :type app_id: dict | bytes

    :rtype: None
    """
    if roleOp == util._ROLE_PARTNER_OP:
        # Check if exist Federation Context Id in Operator Platform
        try:
            originating_op_objects = OriginatingOperatorPlatform.objects(id=federation_context_id)
            if not originating_op_objects:
                abort(404, "Federation not found at Operator Platform")
        except Exception as error:
            abort(422, f"Incorrect value for Federation. Error: {error}")

        # Check if exist Federation Context Id and App Id in Application Onboarding Management
        originating_ao_objects = OriginatingApplicationOnboardingManagement.objects(
            orig_ao_federation_context_id=federation_context_id,
            orig_ao_app_id=app_id)
        if not originating_ao_objects:
            abort(404, "Federation Context and App Id not found at Application Onboarding Management")

        # Check if there are application deployments dependents of the onboarding
        if check_childs_onboarding(federation_context_id, app_id):
            abort(409, "Unable to remove Onboarding. There are application deployments dependent. Remove it and try again ")

        # Delete onboarding at i2edge
        try:
            response = i2edge.delete_onboarding(app_id)
            if response.status_code == 200:
                # Delete all the onboarding updates related to onboarding application
                obj_onboarding = originating_ao_objects.get()
                id_onboarding = obj_onboarding.id
                originating_ao_update_objects = OriginatingApplicationOnboardingManagementUpdate.objects()
                for o in originating_ao_update_objects:
                    try:
                        if o.federation_context_app_id.pk == id_onboarding:
                            o.delete()
                    except Exception as error:
                        print(f"Unable to delete onboarding updates. Error: {error}")

                # Delete Application Onboarding
                originating_ao_objects.delete()
            else:
                abort(422, f"Unable to delete App Onboarding at i2edge. Error {response.status_code} - {response.content}")
        except Exception as error:
            abort(422, f"Unable to delete Application Onboarding at i2edge. Error: {error}")
    elif roleOp == util._ROLE_ORIGINATING_OP:
        try:
            # Extract the token from the header
            bearer_token = util.get_token_from_request(connexion)

            # Find federation at originating OP
            originating_op_objects = OriginatingOperatorPlatformOriginatingOP.objects(id=federation_context_id)
            if not originating_op_objects:
                return "Federation not found", 404
            originating_op_instance = originating_op_objects[0]

            # Find application onboarding at partner
            response_get = fm_client.get_profile(originating_op_instance.partner_federation_id, app_id, bearer_token)

            if "appId" in response_get:
                originating_ao_objects = find_application_onboarding_at_originating_op(federation_context_id, app_id)
                if originating_ao_objects:
                    # Delete application onboarding from partner
                    response_data = fm_client.delete_profile(originating_op_instance.partner_federation_id, app_id, bearer_token)

                    if "deletion" in response_data:
                        # If application onboarding has been removed well, remove application onboarding from originating
                        deleteApplicationOnboardingOriginatingOP(originating_ao_objects)
                        return response_data, 200
                    else:
                        return response_data, 422
                else:
                    return "Application Onboarding exist at partner operator but not in originating operator", 409
            else:
                if find_application_onboarding_at_originating_op(federation_context_id, app_id):
                    return "Application Onboarding exist in originating operator but not at partner operator", 409
                else:
                    return "Application Onboarding not found", 404

        except Exception as error:
            return f"Error while deleting application onboarding. Reason: {error}", 422
    else:
        return "Error: Not assigned role to the operator (originating_op|partner_op)", 422

    return 'App deletion successful', 200


def onboard_application(body, federation_context_id):  # noqa: E501
    """Submits an application details to a partner OP. Based on the details provided,  partner OP shall do bookkeeping, resource validation and other pre-deployment operations.

     # noqa: E501

    :param body: Details about application compute resource requirements, associated artefacts, QoS profile and regions where application shall be made available etc.
    :type body: dict | bytes
    :param federation_context_id:
    :type federation_context_id: dict | bytes

    :rtype: None
    """
    if roleOp == util._ROLE_PARTNER_OP:
        # Check if exist Federation Context Id in Operator Platform
        try:
            originating_op_objects = OriginatingOperatorPlatform.objects(id=federation_context_id)
            if not originating_op_objects:
                abort(404, "Federation not found at Operator Platform")
        except Exception as error:
            abort(422, f"Incorrect value for Federation. Error: {error}")

        if connexion.request.is_json:
            try:
                body = ApplicationOnboardingBody.from_dict(connexion.request.get_json())
            except Exception as error:
                abort(422, f"Onboarding Validation Error. Message: {error}")

        # Check if exist Federation Context Id and App Id in Application Onboarding Management
        originating_ao_objects = OriginatingApplicationOnboardingManagement.objects(
            orig_ao_federation_context_id=federation_context_id,
            orig_ao_app_id=body.app_id)
        if originating_ao_objects:
            abort(409, "Federation Context and App Id already exists at Application Onboarding Management")

        # check if exist app Id at i2edge. If found app id belongs to another federation
        try:
            response = i2edge.get_onboarding(body.app_id)
            if response.status_code == 200:
                abort(409, "App Id already exists at i2edge and belongs to another OP")
        except Exception as error:
            abort(409, f"An error occurred when finding app id at i2edge. Error: {error}")

        # Check if exist app id in the database. If found app id belongs to another federation
        originating_ao_objects = OriginatingApplicationOnboardingManagement.objects(
            orig_ao_app_id=body.app_id)
        if originating_ao_objects:
            abort(409, "App Id already exists for another Federation at Application Onboarding Management")

        # Check if exist artefact id for this federation context
        if not check_artefact_id(federation_context_id, body, operation_POST):
            abort(404, "Federation Context and Artefact Id not found at Artefact Management")

        # Check if exist the provider of the body natches with the providers of the artefact in component specs
        if not check_provider_with_artefact_id_post(federation_context_id, body):
            abort(404, "App provider do not matches with the providers of the artefact in component specs")

        # Check if exist zones for this federation context
        if body.app_deployment_zones:
            if not check_deployment_zones(federation_context_id, body):
                abort(404, "Deployment zones not found for the Federation Context Id or not found at i2edge")

        # Create onboarding at i2edge
        # Retrieve JSON
        i2edge_data = fill_application_onboarding_post_i2edge(body)
        try:
            response = i2edge.post_onboarding(i2edge_data)
            if response.status_code == 201:
                # Save Application Onboarding in FM
                # Convert the original model instance to the MongoEngine document
                onboarding_data = fill_application_onboarding_mongo_document(federation_context_id, body)

                # Create a new MongoEngine document and save it to MongoDB
                new_onboarding = OriginatingApplicationOnboardingManagement(**onboarding_data)
                new_onboarding.save()
            else:
                abort(422, f"Unable to save Application Onboarding at i2edge. Error {response.status_code} - {response.content}")
        except Exception as error:
            abort(422, f"Unable to save Application Onboarding at i2edge. Error: {error}")
    elif roleOp == util._ROLE_ORIGINATING_OP:
        try:
            # Extract the token from the header
            bearer_token = util.get_token_from_request(connexion)

            body = ApplicationOnboardingBody.from_dict(connexion.request.get_json())

            # Find federation at originating OP
            originating_op_objects = OriginatingOperatorPlatformOriginatingOP.objects(id=federation_context_id)
            if not originating_op_objects:
                return "Federation not found", 404
            originating_op_instance = originating_op_objects[0]
            # Find application onboarding at partner
            response_get = fm_client.get_profile(originating_op_instance.partner_federation_id, body.app_id, bearer_token)
            if "appId" in response_get:
                if find_application_onboarding_at_originating_op(federation_context_id, body.app_id):
                    return "Application onboarding already exist", 422
                else:
                    return "Application onboarding exist at partner operator but not exist in originating operator", 409
            else:
                if find_application_onboarding_at_originating_op(federation_context_id, body.app_id):
                    return "Application onboarding exist in originating operator but not exist at partner operator", 409
                else:
                    # Create application profile at partner
                    response_data = fm_client.create_profile(originating_op_instance.partner_federation_id, connexion.request.get_json(), bearer_token)

                    if "accepted" in response_data:
                        # Create application onboarding in originating
                        create_application_onboarding_originatingOP(federation_context_id, originating_op_instance.partner_federation_id, body)
                        return response_data, 202
                    else:
                        return response_data, 422

        except Exception as error:
            return f"Error while creating application onboarding. Reason: {error}", 422
    else:
        return "Error: Not assigned role to the operator (originating_op|partner_op)", 200

    return 'Application onboarded request accepted', 202


def update_application(body, federation_context_id, app_id):  # noqa: E501
    """Updates partner OP about changes in application compute resource requirements, QOS Profile, associated descriptor or change in associated components

     # noqa: E501

    :param body: Details about application compute resource requirements, associated artefact and QOS profile that needs to be updated.
    :type body: dict | bytes
    :param federation_context_id:
    :type federation_context_id: dict | bytes
    :param app_id:
    :param app_id:
    :type app_id: dict | bytes

    :rtype: None
    """
    if roleOp == util._ROLE_PARTNER_OP:
        # Check if exist Federation Context Id in Operator Platform
        try:
            originating_op_objects = OriginatingOperatorPlatform.objects(id=federation_context_id)
            if not originating_op_objects:
                abort(404, "Federation not found at Operator Platform")
        except Exception as error:
            abort(422, f"Incorrect value for Federation. Error: {error}")

        # Check if exist Federation Context Id and App Id in Application Onboarding Management
        originating_ao_objects = OriginatingApplicationOnboardingManagement.objects(
            orig_ao_federation_context_id=federation_context_id,
            orig_ao_app_id=app_id)
        if not originating_ao_objects:
            abort(404, "Federation Context and App Id not found at Application Onboarding Management")
        originating_ao_instance = originating_ao_objects[0]

        if connexion.request.is_json:
            try:
                body = AppAppIdBody.from_dict(connexion.request.get_json())  # noqa: E501
            except Exception as error:
                abort(422, f"Onboarding Validation Error. Message: {error}")

        # Check if exist artefact id for this federation context
        if not check_artefact_id(federation_context_id, body, operation_PATCH):
            abort(404, "Federation Context and Artefact Id not found at Artefact Management")

        # Check if the provider of the onboarding natches with the providers of the artefact in component specs
        if not check_provider_with_artefact_id_update(federation_context_id, originating_ao_instance.orig_ao_app_provider_id, body):
            abort(404, "App provider do not matches with the providers of the artefact in component specs")

        # Update onboarding at i2edge
        # Retrieve JSON
        i2edge_data = fill_application_onboarding_update_i2edge(body, originating_ao_instance)
        try:
            response = i2edge.update_onboarding(app_id, i2edge_data)
            if response.status_code == 200:
                # Update onboarding in FM
                # Convert the original model instance to the MongoEngine document
                onboarding_update_data = fill_update_application_onboarding_mongo_document(body, originating_ao_instance)
                originating_ao_instance.update(orig_ao_app_qos_profile_latency_constraints=body.app_upd_qo_s_profile.latency_constraints)
                originating_ao_instance.update(orig_ao_app_qos_profile_bandwidth_required=body.app_upd_qo_s_profile.bandwidth_required)
                originating_ao_instance.update(orig_ao_app_qos_profile_multi_user_clients=body.app_upd_qo_s_profile.multi_user_clients)
                originating_ao_instance.update(orig_ao_app_qos_profile_no_of_users_per_app_inst=body.app_upd_qo_s_profile.no_of_users_per_app_inst)
                originating_ao_instance.update(orig_ao_app_qos_profile_app_provisioning=body.app_upd_qo_s_profile.app_provisioning)
                originating_ao_instance.update(orig_ao_app_meta_data_mobility_support=body.app_upd_qo_s_profile.mobility_support)
                originating_ao_instance.update(orig_ao_app_component_specs=onboarding_update_data.get("app_component_specs"))

                # Create a new MongoEngine document and save it to MongoDB
                new_onboarding_update = OriginatingApplicationOnboardingManagementUpdate(**onboarding_update_data)
                new_onboarding_update.save()
            else:
                abort(422, f"Unable to update Application Onboarding. Error: {response.status_code} from i2edge. {response.content}")
        except Exception as error:
            abort(422, f"Unable to update Application Onboarding at i2edge. Error: {error}")
    elif roleOp == util._ROLE_ORIGINATING_OP:
        # Extract the token from the header
        bearer_token = util.get_token_from_request(connexion)

        body = AppAppIdBody.from_dict(connexion.request.get_json())

        # Find federation at originating OP
        originating_op_objects = OriginatingOperatorPlatformOriginatingOP.objects(id=federation_context_id)
        if not originating_op_objects:
            return "Federation not found", 404
        originating_op_instance = originating_op_objects[0]
        # Find application onboarding at partner
        response_get = fm_client.get_profile(originating_op_instance.partner_federation_id, app_id, bearer_token)
        if "appId" in response_get:
            originating_ao_objects = find_application_onboarding_at_originating_op(federation_context_id, app_id)
            if originating_ao_objects:
                # Update application onboarding at partner
                response_data = fm_client.update_profile(bearer_token, originating_op_instance.partner_federation_id, app_id,
                                                         connexion.request.get_json())
                if "accepted" in response_data:
                    originating_ao_instance = originating_ao_objects[0]
                    update_application_onboarding_originating_op(body, federation_context_id,
                                                                 originating_op_instance.partner_federation_id, app_id,
                                                                 originating_ao_instance)
                    return response_data, 202
                else:
                    return response_data, 422

            else:
                return "Application onboarding exist at partner operator but not exist in originating operator", 409
        else:
            if find_application_onboarding_at_originating_op(federation_context_id, app_id):
                return "Application onboarding exist in originating operator but not exist at partner operator", 409
            else:
                return "Application onboarding not found", 404

    else:
        return "Error: Not assigned role to the operator (originating_op|partner_op)", 422

    return 'Application update request accepted', 202


def view_application(federation_context_id, app_id):  # noqa: E501
    """Retrieves application details from partner OP

     # noqa: E501

    :param federation_context_id:
    :type federation_context_id: dict | bytes
    :param app_id:
    :type app_id: dict | bytes

    :rtype: InlineResponse2007
    """
    if roleOp == util._ROLE_PARTNER_OP:
        # Check if exist Federation Context Id in Operator Platform
        try:
            originating_op_objects = OriginatingOperatorPlatform.objects(id=federation_context_id)
            if not originating_op_objects:
                abort(404, "Federation not found at Operator Platform")
        except Exception as error:
            abort(422, f"Incorrect value for Federation. Error: {error}")

        # Check if exist Federation Context Id and App Id in Application Onboarding Management
        originating_ao_objects = OriginatingApplicationOnboardingManagement.objects(
            orig_ao_federation_context_id=federation_context_id,
            orig_ao_app_id=app_id)
        if not originating_ao_objects:
            abort(404, "Federation Context and App Id not found at Application Onboarding Management")

        operator = originating_op_objects.get()
        application = originating_ao_objects.get()

        appMetadata = {"'appName": application.orig_ao_app_meta_data_app_name,
                       "version": application.orig_ao_app_meta_data_version,
                       "appDescription": application.orig_ao_app_meta_data_app_description,
                       "mobilitySupport": application.orig_ao_app_meta_data_mobility_support,
                       "accessToken": application.orig_ao_app_meta_data_access_token,
                       "category": application.orig_ao_app_meta_data_category
                       }

        appQoSProfile = {"latencyConstraints": application.orig_ao_app_qos_profile_latency_constraints,
                         "bandwidthRequired": application.orig_ao_app_qos_profile_bandwidth_required,
                         "multiUserClients": application.orig_ao_app_qos_profile_multi_user_clients,
                         "noOfUsersPerAppInst": application.orig_ao_app_qos_profile_no_of_users_per_app_inst,
                         "appProvisioning": application.orig_ao_app_qos_profile_app_provisioning
                         }

        zones_list = []
        for z in application.orig_ao_app_deployment_zones:
            zone_element = {
                "countryCode": operator.orig_op_country_code,
                "zoneInfo": z
            }
            zones_list.append(zone_element)

        response_data = {
            "appId": application.orig_ao_app_id,
            "appProviderId": application.orig_ao_app_provider_id,
            "appDeploymentZones": zones_list,
            "appMetaData": appMetadata,
            "appQoSProfile": appQoSProfile,
            "appComponentSpecs": json.loads(application.orig_ao_app_component_specs)
        }

        application_response_data = InlineResponse2007.from_dict(response_data)
    elif roleOp == util._ROLE_ORIGINATING_OP:
        # Extract the token from the header
        bearer_token = util.get_token_from_request(connexion)

        # Find federation at originating OP
        originating_op_objects = OriginatingOperatorPlatformOriginatingOP.objects(id=federation_context_id)
        if not originating_op_objects:
            return "Federation not found", 404
        originating_op_instance = originating_op_objects[0]

        application_response_data = fm_client.get_profile(originating_op_instance.partner_federation_id, app_id, bearer_token)
        if "appId" in application_response_data:
            if find_application_onboarding_at_originating_op(federation_context_id, app_id):
                return application_response_data, 200
            else:
                return "Application Onboarding exist at partner operator but not in originating operator", 409
        else:
            if find_application_onboarding_at_originating_op(federation_context_id, app_id):
                return "Application Onboarding exist in originating operator but not at partner operator", 409
            else:
                return "Application Onboarding not found", 404
    else:
        application_response_data = {"Error": "Not assigned role to the operator (originating_op|partner_op)"}

    return application_response_data

def check_artefact_id(federation_context_id, body, operation):
    exist_artefact = True
    artefact_id = ""

    for acs in body.app_component_specs:
        if operation == operation_POST:
            artefact_id = acs.get("artefactId")
        elif operation == operation_PATCH:
            artefact_id = acs.artefact_id
        # Check if exist Federation Context Id and Artefact Id in Artefact Management
        originating_am_objects = OriginatingArtefactManagement.objects(
            orig_am_federation_context_id=federation_context_id,
            orig_am_artefact_id=artefact_id)
        if not originating_am_objects:
            exist_artefact = False
            break

    return exist_artefact


def check_provider_with_artefact_id_post(federation_context_id, body):
    same_provider = True
    artefact_id = ""

    for acs in body.app_component_specs:
        artefact_id = acs.get("artefactId")

        # Check if exist Federation Context Id and Artefact Id in Artefact Management
        originating_am_objects = OriginatingArtefactManagement.objects(
            orig_am_federation_context_id=federation_context_id,
            orig_am_artefact_id=artefact_id)
        if not originating_am_objects:
            same_provider = False
            break
        artefact = originating_am_objects.get()
        # Check if the provider of the body matches with the provider of the artefact
        if body.app_provider_id != artefact.orig_am_app_provider_id:
            same_provider = False
            break

    return same_provider


def check_provider_with_artefact_id_update(federation_context_id, app_provider_id, body):
    same_provider = True
    artefact_id = ""

    for acs in body.app_component_specs:
        artefact_id = acs.artefact_id

        # Check if exist Federation Context Id and Artefact Id in Artefact Management
        originating_am_objects = OriginatingArtefactManagement.objects(
            orig_am_federation_context_id=federation_context_id,
            orig_am_artefact_id=artefact_id)
        if not originating_am_objects:
            same_provider = False
            break
        artefact = originating_am_objects.get()
        # Check if the provider of the body matches with the provider of the artefact
        if app_provider_id != artefact.orig_am_app_provider_id:
            same_provider = False
            break

    return same_provider


def check_deployment_zones(federation_context_id, body):
    exist_zone = True

    # Check if exist Federation Context Id in Availability Zones
    originating_zi_objects = OriginatingZoneInfo.objects(orig_zi_federation_context_id=federation_context_id)
    if not originating_zi_objects:
        abort(404, "Federation Context not found at Availability Zones")

    # check Zones of the Federation Context Id
    zones = originating_zi_objects.get()
    for acs in body.app_deployment_zones:
        # Check if exist Federation Context Id and Zone Id in Availability Zones
        if acs not in zones.orig_zi_acceptedAvailabilityZones:
            return False

    # Check if exist deployment zones in i2edge
    for acs in body.app_deployment_zones:
        # Check if exist Zone Id in i2edge
        zone_data = i2edge.get_zone_by_zone_id(acs)
        if not zone_data:
            return False

    return exist_zone


def fill_application_onboarding_mongo_document(federation_context_id, body):

    onboarding_data = {
        "orig_ao_federation_context_id": federation_context_id,
        "orig_ao_app_id": body.app_id,
        "orig_ao_app_provider_id": body.app_provider_id,
        "orig_ao_app_deployment_zones": body.app_deployment_zones,
        "orig_ao_app_meta_data_app_name": body.app_meta_data.app_name,
        "orig_ao_app_meta_data_version" : body.app_meta_data.version,
        "orig_ao_app_meta_data_app_description" : body.app_meta_data.app_description,
        "orig_ao_app_meta_data_mobility_support" : body.app_meta_data.mobility_support,
        "orig_ao_app_meta_data_access_token" : body.app_meta_data.access_token,
        "orig_ao_app_meta_data_category" : body.app_meta_data.category,
        "orig_ao_app_qos_profile_latency_constraints" : body.app_qo_s_profile.latency_constraints,
        "orig_ao_app_qos_profile_bandwidth_required" : body.app_qo_s_profile.bandwidth_required,
        "orig_ao_app_qos_profile_multi_user_clients" : body.app_qo_s_profile.multi_user_clients,
        "orig_ao_app_qos_profile_no_of_users_per_app_inst" : body.app_qo_s_profile.no_of_users_per_app_inst,
        "orig_ao_app_qos_profile_app_provisioning" : body.app_qo_s_profile.app_provisioning,
        "orig_ao_app_component_specs": json.dumps(body.app_component_specs),
        "orig_ao_app_status_callback_link" : body.app_status_callback_link
    }

    return onboarding_data

def fill_update_application_onboarding_mongo_document(body, originating_ao_instance):

    app_update_component_specs_list = []
    for acs in body.app_component_specs:
        data_acs = {
            "service_name_nb": acs.service_name_nb,
            "service_name_ew": acs.service_name_ew,
            "component_name": acs.component_name,
            "artefact_id": acs.artefact_id
        }
        app_update_component_specs_list.append(data_acs)

    onboarding_update_data = {
        "app_qos_profile_latency_constraints": body.app_upd_qo_s_profile.latency_constraints,
        "app_qos_profile_bandwidth_required": body.app_upd_qo_s_profile.bandwidth_required,
        "app_qos_profile_multi_user_clients": body.app_upd_qo_s_profile.multi_user_clients,
        "app_qos_profile_no_of_users_per_app_inst": body.app_upd_qo_s_profile.no_of_users_per_app_inst,
        "app_qos_profile_app_provisioning": body.app_upd_qo_s_profile.app_provisioning,
        "app_component_specs": json.dumps(app_update_component_specs_list),
        "federation_context_app_id" : originating_ao_instance
    }

    return onboarding_update_data


def fill_application_onboarding_post_i2edge(body):

    app_update_component_specs_list = []
    for acs in body.app_component_specs:
        data_acs = {
            "serviceNameNB": acs.get('serviceNameNB'),
            "serviceNameEW": acs.get('serviceNameEW'),
            "componentName": acs.get('componentName'),
            "artefactId": acs.get('artefactId')
        }
        app_update_component_specs_list.append(data_acs)

    appMetadata = {"appName": body.app_meta_data.app_name,
                   "version": body.app_meta_data.version,
                   "appDescription": body.app_meta_data.app_description,
                   "mobilitySupport": body.app_meta_data.mobility_support,
                   "accessToken": body.app_meta_data.access_token,
                   "category": body.app_meta_data.category
                   }

    appQoSProfile = {"latencyConstraints": body.app_qo_s_profile.latency_constraints,
                     "bandwidthRequired": body.app_qo_s_profile.bandwidth_required,
                     "multiUserClients": body.app_qo_s_profile.multi_user_clients,
                     "noOfUsersPerAppInst": body.app_qo_s_profile.no_of_users_per_app_inst,
                     "appProvisioning": body.app_qo_s_profile.app_provisioning
                     }

    response_data = {
        "app_id": body.app_id,
        "appProviderId": body.app_provider_id,
        "appDeploymentZones": body.app_deployment_zones,
        "appMetaData": appMetadata,
        "appQoSProfile": appQoSProfile,
        "appComponentSpecs": app_update_component_specs_list,
        "appStatusCallbackLink": body.app_status_callback_link
    }

    response = {
        "profile_data" : response_data
    }

    return response

def fill_application_onboarding_update_i2edge(body, instance):

    app_update_component_specs_list = []
    for acs in body.app_component_specs:
        data_acs = {
            "serviceNameNB": acs.service_name_nb,
            "serviceNameEW": acs.service_name_ew,
            "componentName": acs.component_name,
            "artefactId": acs.artefact_id
        }
        app_update_component_specs_list.append(data_acs)

    appMetadata = {"appName": instance.orig_ao_app_meta_data_app_name,
                   "version": instance.orig_ao_app_meta_data_version,
                   "appDescription": instance.orig_ao_app_meta_data_app_description,
                   "mobilitySupport": body.app_upd_qo_s_profile.mobility_support,
                   "accessToken": instance.orig_ao_app_meta_data_access_token,
                   "category": instance.orig_ao_app_meta_data_category
                   }

    appQoSProfile = {"latencyConstraints": body.app_upd_qo_s_profile.latency_constraints,
                     "bandwidthRequired": body.app_upd_qo_s_profile.bandwidth_required,
                     "multiUserClients": body.app_upd_qo_s_profile.multi_user_clients,
                     "noOfUsersPerAppInst": body.app_upd_qo_s_profile.no_of_users_per_app_inst,
                     "appProvisioning": body.app_upd_qo_s_profile.app_provisioning
                     }

    response_data = {
        #"appId": instance.orig_ao_app_id,
        "appProviderId": instance.orig_ao_app_provider_id,
        "appDeploymentZones": instance.orig_ao_app_deployment_zones,
        "appMetaData": appMetadata,
        "appQoSProfile": appQoSProfile,
        "appComponentSpecs": app_update_component_specs_list,
        "appStatusCallbackLink": instance.orig_ao_app_status_callback_link
    }

    response = {
        "profile_data" : response_data
    }

    return response

def check_childs_onboarding(federation_context_id, app_id):
    found = False

    originating_ad_objects = OriginatingApplicationDeploymentManagement.objects(
        orig_ad_federation_context_id=federation_context_id,
        orig_ad_app_id=app_id
    )
    if originating_ad_objects:
        return True

    return found

def find_application_onboarding_at_originating_op(federation_id, app_id):
    originating_ao_objects = OriginatingApplicationOnboardingManagementOriginatingOP.objects(
        orig_ao_federation_context_id=federation_id,
        orig_ao_app_id=app_id)

    return originating_ao_objects

def deleteApplicationOnboardingOriginatingOP(originating_ao_objects):
    # Delete all the onboarding updates related to onboarding application
    obj_onboarding = originating_ao_objects.get()
    id_onboarding = obj_onboarding.id
    originating_ao_update_objects = OriginatingApplicationOnboardingManagementUpdateOriginatingOP.objects()
    for o in originating_ao_update_objects:
        try:
            if o.federation_context_app_id.pk == id_onboarding:
                o.delete()
        except Exception as error:
            print(f"Unable to delete onboarding updates. Error: {error}")

    # Delete Application Onboarding
    originating_ao_objects.delete()


def create_application_onboarding_originatingOP(federation_id, partner_federation_id, body):

    onboarding_data = {
        "orig_ao_federation_context_id": federation_id,
        "orig_ao_app_id": body.app_id,
        "orig_ao_app_provider_id": body.app_provider_id,
        "orig_ao_app_deployment_zones": body.app_deployment_zones,
        "orig_ao_app_meta_data_app_name": body.app_meta_data.app_name,
        "orig_ao_app_meta_data_version" : body.app_meta_data.version,
        "orig_ao_app_meta_data_app_description" : body.app_meta_data.app_description,
        "orig_ao_app_meta_data_mobility_support" : body.app_meta_data.mobility_support,
        "orig_ao_app_meta_data_access_token" : body.app_meta_data.access_token,
        "orig_ao_app_meta_data_category" : body.app_meta_data.category,
        "orig_ao_app_qos_profile_latency_constraints" : body.app_qo_s_profile.latency_constraints,
        "orig_ao_app_qos_profile_bandwidth_required" : body.app_qo_s_profile.bandwidth_required,
        "orig_ao_app_qos_profile_multi_user_clients" : body.app_qo_s_profile.multi_user_clients,
        "orig_ao_app_qos_profile_no_of_users_per_app_inst" : body.app_qo_s_profile.no_of_users_per_app_inst,
        "orig_ao_app_qos_profile_app_provisioning" : body.app_qo_s_profile.app_provisioning,
        "orig_ao_app_component_specs": json.dumps(body.app_component_specs),
        "orig_ao_app_status_callback_link" : body.app_status_callback_link,
        "partner_federation_id": partner_federation_id
    }

    # Create a new MongoEngine document and save it to MongoDB
    new_onboarding = OriginatingApplicationOnboardingManagementOriginatingOP(**onboarding_data)
    new_onboarding.save()

def update_application_onboarding_originating_op(body, federation_context_id, partner_federation_id, app_id, originating_ao_instance):
    app_update_component_specs_list = []
    for acs in body.app_component_specs:
        data_acs = {
            "service_name_nb": acs.service_name_nb,
            "service_name_ew": acs.service_name_ew,
            "component_name": acs.component_name,
            "artefact_id": acs.artefact_id
        }
        app_update_component_specs_list.append(data_acs)

    onboarding_update_data = {
        "app_qos_profile_latency_constraints": body.app_upd_qo_s_profile.latency_constraints,
        "app_qos_profile_bandwidth_required": body.app_upd_qo_s_profile.bandwidth_required,
        "app_qos_profile_multi_user_clients": body.app_upd_qo_s_profile.multi_user_clients,
        "app_qos_profile_no_of_users_per_app_inst": body.app_upd_qo_s_profile.no_of_users_per_app_inst,
        "app_qos_profile_app_provisioning": body.app_upd_qo_s_profile.app_provisioning,
        "app_component_specs": json.dumps(app_update_component_specs_list),
        "federation_context_app_id": originating_ao_instance,
        "partner_federation_id": partner_federation_id
    }

    originating_ao_instance.update(orig_ao_app_qos_profile_latency_constraints=body.app_upd_qo_s_profile.latency_constraints)
    originating_ao_instance.update(orig_ao_app_qos_profile_bandwidth_required=body.app_upd_qo_s_profile.bandwidth_required)
    originating_ao_instance.update(orig_ao_app_qos_profile_multi_user_clients=body.app_upd_qo_s_profile.multi_user_clients)
    originating_ao_instance.update(orig_ao_app_qos_profile_no_of_users_per_app_inst=body.app_upd_qo_s_profile.no_of_users_per_app_inst)
    originating_ao_instance.update(orig_ao_app_qos_profile_app_provisioning=body.app_upd_qo_s_profile.app_provisioning)
    originating_ao_instance.update(orig_ao_app_meta_data_mobility_support=body.app_upd_qo_s_profile.mobility_support)
    originating_ao_instance.update(orig_ao_app_component_specs=onboarding_update_data.get("app_component_specs"))

    # Create a new MongoEngine document and save it to MongoDB
    new_onboarding_update = OriginatingApplicationOnboardingManagementUpdateOriginatingOP(**onboarding_update_data)
    new_onboarding_update.save()
