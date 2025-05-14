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

from models.app_identifier import AppIdentifier  # noqa: E501
from models.app_provider_id import AppProviderId  # noqa: E501
from models.application_lcm_body import ApplicationLcmBody  # noqa: E501
from models.federation_context_id import FederationContextId  # noqa: E501
from models.inline_response2008 import InlineResponse2008  # noqa: E501
from models.inline_response2009 import InlineResponse2009  # noqa: E501
from models.inline_response202 import InlineResponse202  # noqa: E501
from models.instance_identifier import InstanceIdentifier  # noqa: E501
from models.problem_details import ProblemDetails  # noqa: E501
from models.zone_identifier import ZoneIdentifier  # noqa: E501
import util
from models.mongo_document import OriginatingOperatorPlatform
from models.mongo_document import OriginatingOperatorPlatformOriginatingOP
from models.mongo_document import OriginatingApplicationOnboardingManagement
from models.mongo_document import OriginatingZoneInfo
from models.mongo_document import OriginatingApplicationDeploymentManagement
from models.mongo_document import OriginatingApplicationDeploymentManagementOriginatingOP
from flask import abort
from clients import i2edge
import json

from configparser import ConfigParser
from clients import fed_manager as fm_client

CONFIG = ConfigParser()
CONFIG.read("conf/config.cfg")
roleOp = CONFIG.get("partner_op", "role")


def get_all_app_instances(federation_context_id, app_id, app_provider_id):  # noqa: E501
    """Retrieves all application instance of partner OP

     # noqa: E501

    :param federation_context_id:
    :type federation_context_id: dict | bytes
    :param app_id:
    :type app_id: dict | bytes
    :param app_provider_id:
    :type app_provider_id: dict | bytes

    :rtype: List[InlineResponse2009]
    """
    if roleOp == util._ROLE_PARTNER_OP:
        # Check if exist Federation Context Id in Operator Platform
        try:
            originating_op_objects = OriginatingOperatorPlatform.objects(id=federation_context_id)
            if not originating_op_objects:
                abort(404, "Federation not found at Operator Platform")
        except Exception as error:
            #abort(422, f"Incorrect value for Federation. Error: {error}")
            abort(422, f"Error: {error}")

        # Check if exist Federation Context Id and App Id in Application Onboarding Management
        originating_ao_objects = OriginatingApplicationOnboardingManagement.objects(
            orig_ao_federation_context_id=federation_context_id,
            orig_ao_app_id=app_id)
        if not originating_ao_objects:
            abort(404, "Federation Context and App Id not Found at Application Onboarding Management")

        # Check if exist application deployment by federation id, app Id, and app provider id
        originating_ad_objects = OriginatingApplicationDeploymentManagement.objects(
            orig_ad_federation_context_id=federation_context_id,
            orig_ad_app_id=app_id,
            orig_ad_app_provider_id=app_provider_id
        )
        if not originating_ad_objects:
            abort(404, "Application Deployment Management Not Found by Federation Context, "
                       "appId and appProviderId")

        # Get list of zones and their instances to fill response data
        instances_deployment = originating_ad_objects.filter()
        list_zones_instances = get_list_zones_instances(instances_deployment)

        # Fill response data from the list of zones and their instances
        list_responses = []
        zones_id = {}
        instances_id = []
        for zi in list_zones_instances:
            # Add instances for each zone
            for ins in zi[1]:
                # Find instance state from i2edge
                instance_state = find_instance_state(zi[0], ins)
                instances_id.append({"appInstIdentifier": ins, "appInstanceState": instance_state})
            zones_id = {"zoneId": str(zi[0]), "appInstanceInfo": instances_id}
            # Add InlineResponse2009 to the list of responses
            list_responses.append(InlineResponse2009.from_dict(zones_id))
            # Clear instances array for the next zone
            instances_id = []

        deployment_response_data = list_responses
    elif roleOp == util._ROLE_ORIGINATING_OP:
        # Extract the token from the header
        bearer_token = util.get_token_from_request(connexion)

        # Find federation at originating OP
        originating_op_objects = OriginatingOperatorPlatformOriginatingOP.objects(id=federation_context_id)
        if not originating_op_objects:
            return "Federation not found", 404
        originating_op_instance = originating_op_objects[0]
        # Find application deployment at partner
        deployment_response_data = fm_client.get_all_instances_deployment(originating_op_instance.partner_federation_id, app_id,
                                                                          app_provider_id, bearer_token)
        info = ""
        if len(deployment_response_data) > 0:
            try:
                info = deployment_response_data[0]
            except:
                info = ""
        if "appInstanceInfo" in info:
            # Find all instances in originating operator
            if find_all_instances_originating_op(federation_context_id, app_id, app_provider_id):
               return deployment_response_data, 200
            else:
                return "Application deployment exists at partner operator but not in originating operator", 409
        else:
            if find_all_instances_originating_op(federation_context_id, app_id, app_provider_id):
                return "Application deployment exists in originating operator but not at partner operator", 409
            else:
                return "Application deployment not found", 404

    else:
        deployment_response_data = {"Error": "Not assigned role to the operator (originating_op|partner_op)"}

    return deployment_response_data

def get_app_instance_details(federation_context_id, app_id, app_instance_id, zone_id):  # noqa: E501
    """Retrieves an application instance details from partner OP.

     # noqa: E501

    :param federation_context_id:
    :type federation_context_id: dict | bytes
    :param app_id:
    :type app_id: dict | bytes
    :param app_instance_id:
    :type app_instance_id: dict | bytes
    :param zone_id:
    :type zone_id: dict | bytes

    :rtype: InlineResponse2008
    """
    if roleOp == util._ROLE_PARTNER_OP:
        # Check if exist Federation Context Id in Operator Platform
        try:
            originating_op_objects = OriginatingOperatorPlatform.objects(id=federation_context_id)
            if not originating_op_objects:
                abort(404, "Federation not found at Operator Platform")
        except Exception as error:
            #abort(422, f"Incorrect value for Federation. Error: {error}")
            abort(422, f"Error: {error}")

        # Check if exist Federation Context Id and App Id in Application Onboarding Management
        originating_ao_objects = OriginatingApplicationOnboardingManagement.objects(
            orig_ao_federation_context_id=federation_context_id,
            orig_ao_app_id=app_id)
        if not originating_ao_objects:
            abort(404, "Federation Context and App Id not Found at Application Onboarding Management")

        # Check if exist instance id at i2edge
        try:
            response = i2edge.get_app_by_zone_ap_name(zone_id, app_instance_id)
            if response.status_code != 200:
                abort(422, f"Error: {response.status_code} from i2edge. {response.content}")
        except Exception as error:
            #abort(422, f"Unable to find Instance Id at i2edge. Error: {error}")
            abort(422, f"Error: {error}")

        # Check if exist zone id at i2edge
        try:
            if not i2edge.get_zone_by_zone_id(zone_id):
                abort(422, "Zone Id not found at i2edge")
        except Exception as error:
            #abort(422, f"Unable to find Zone Id at i2edge. Error: {error}")
            abort(422, f"Error: {error}")

        onboarding_instance = originating_ao_objects.get()
        # check if exist zone for this federation at Availability Zones of onboarding
        # Because zone id of the deployment can be assigned automatically if we do not specify the zone
        # when create deployment, it has not sense this validation
        #if not check_zone_by_federation_and_onboarding(zone_id, onboarding_instance):
        #    abort(422, f"Zone id not found for this Federation at Availability Zones of onboarding")

        # Check if exist application deployment by federation id, app Id, instance Id and zone Id
        originating_ad_objects = OriginatingApplicationDeploymentManagement.objects(
            orig_ad_federation_context_id=federation_context_id,
            orig_ad_app_id=app_id,
            orig_ad_instance_id=app_instance_id,
            orig_ad_zone_info_zone_id=zone_id
        )
        if not originating_ad_objects:
            abort(404, "Application Deployment Management Not Found by Federation Context, "
                       "appId, appInstanceId and zoneId")

        response_data = create_response_instance_details(zone_id, app_instance_id)
        if response_data == "":
            abort(422, "Unable to get app by zone id and app name form i2edge")

        deployment_response_data = InlineResponse2008.from_dict(response_data)
    elif roleOp == util._ROLE_ORIGINATING_OP:
        # Extract the token from the header
        bearer_token = util.get_token_from_request(connexion)

        # Find federation at originating OP
        originating_op_objects = OriginatingOperatorPlatformOriginatingOP.objects(id=federation_context_id)
        if not originating_op_objects:
            return "Federation not found", 404
        originating_op_instance = originating_op_objects[0]
        # Find application deployment details at partner
        deployment_response_data = fm_client.get_instance_details_deployment(originating_op_instance.partner_federation_id,
                                                                             app_id, app_instance_id,
                                                                             zone_id, bearer_token)
        if "appInstanceState" in deployment_response_data:
            # Find instance details in originating operator
            if find_instance_details(federation_context_id, app_id, app_instance_id, zone_id):
                return deployment_response_data, 200
            else:
                return "Application Deployment exist at partner operator but not in originating operator", 409
        else:
            if find_instance_details(federation_context_id, app_id, app_instance_id, zone_id):
                return "Application Deployment exist in originating operator but not at partner operator", 409
            else:
                return "Application Deployment not found", 404

    else:
        deployment_response_data = {"Error": "Not assigned role to the operator (originating_op|partner_op)"}

    return deployment_response_data


def install_app(federation_context_id, body=None):  # noqa: E501
    """Instantiates an application on a partner OP zone.

     # noqa: E501

    :param federation_context_id:
    :type federation_context_id: dict | bytes
    :param body: Details about application and zones where application instance should be created. It also definea call back URI which the partner OP shall use update home OP about a change in instance status.
    :type body: dict | bytes

    :rtype: InlineResponse202
    """
    if roleOp == util._ROLE_PARTNER_OP:
        # Check if exist Federation Context Id in Operator Platform
        try:
            originating_op_objects = OriginatingOperatorPlatform.objects(id=federation_context_id)
            if not originating_op_objects:
                abort(404, "Federation not found at Operator Platform")
        except Exception as error:
            #abort(422, f"Incorrect value for Federation. Error: {error}")
            abort(422, f"Error: {error}")

        if connexion.request.is_json:
            try:
                body = ApplicationLcmBody.from_dict(connexion.request.get_json())  # noqa: E501
            except Exception as error:
                #abort(422, f"Deployment Validation Error. Message: {error}")
                abort(422, f" Error: {error}")

        # Check if exist Federation Context Id and App Id in Application Onboarding Management
        originating_ao_objects = OriginatingApplicationOnboardingManagement.objects(
            orig_ao_federation_context_id=federation_context_id,
            orig_ao_app_id=body.app_id)
        if not originating_ao_objects:
            abort(404, "Federation Context and App Id not Found at Application Onboarding Management")

        onboarding_instance = originating_ao_objects.get()

        zone_in_blanks = False
        if body.zone_info.zone_id == "":
            zone_in_blanks = True
            if not check_flavour_in_i2edge(body.zone_info.flavour_id):
                abort(404, "Flavour id not found at i2edge")
        else:
            # Check zone and flavour provided by the body
            try:
                if not check_zone_and_flavour(body):
                    abort(404, "Flavour for this zone not found at i2edge")
            except Exception as error:
                #abort(422, f"Unable to find zone from i2edge. Error: {error}")
                abort(422, f"Error: {error}")

            # check if exist zone for this federation at Availability Zones of the onboarding
            if not check_zone_by_federation_and_onboarding(body.zone_info.zone_id, onboarding_instance):
                abort(422, f"Zone id not found for this Federation at Availability Zones of the onboarding")

        # check if the provider is the same that the provider of the app id
        if body.app_provider_id != onboarding_instance.orig_ao_app_provider_id:
            abort(404, "Provider does not match with the Provider of the Application Onboarding")

        # check if exist a version in the application deployment with the same app id
        originating_ad_version_objects = OriginatingApplicationDeploymentManagement.objects(
            orig_ad_federation_context_id=federation_context_id,
            orig_ad_app_id=body.app_id,
            orig_ad_app_version=body.app_version
        )
        if originating_ad_version_objects:
            abort(409, "App Version already exists for the App Id in the Application Deployment Management")

        # Create app command at i2edge
        # Retrieve JSON
        instance_id = ""
        instance_id_data = {}
        i2edge_data = fill_app_command_post_i2edge(body, zone_in_blanks)
        try:
            response = i2edge.post_app_command(i2edge_data)
            if response.status_code != 202:
                abort(422, f"Error {response.status_code} - {response.content}")
            instance_id_data = response.json()
        except Exception as error:
            #abort(422, f"Unable to deploy app command at i2edge. Error: {error}")
            abort(422, f"Error: {error}")

        # Get instance id (name) from response
        instance_id = instance_id_data.get("deploy_name")
        # If zone id of the body was in blanks, retrieve zone id from i2edge
        zone_id = ""
        if zone_in_blanks:
            # body_to_send = instance_id_data.get("app_spec")
            # node_selector = body_to_send.get("nodeSelector")
            # zone_id = node_selector.get("feature.node.kubernetes.io/zoneID")
            zone_id = instance_id_data.get("zoneID")

        # Check if exist application deployment by federation, appId and instance Id
        originating_ad_objects = OriginatingApplicationDeploymentManagement.objects(
            orig_ad_federation_context_id=federation_context_id,
            orig_ad_app_id=body.app_id,
            orig_ad_instance_id=instance_id
        )
        if originating_ad_objects:
            # if not is possible to create deployment in FM, delete the app command created
            try:
                response = i2edge.delete_app(instance_id)
                if response.status_code != 200:
                    abort(422, f"Unable to delete app in i2edge when is not possible create deployment in FM. "
                               f"Error {response.status_code} - {response.content}")
            except Exception as error:
                abort(422, "Unable to create Application Deployment Management and delete app in i2edge")
            abort(409, "Application Deployment Management already exist for Federation Context, "
                       "appId and appInstanceId")

        # Convert the original model instance to the MongoEngine document
        deployment_data = fill_application_deployment_mongo_document(federation_context_id, instance_id, body,
                                                                     zone_in_blanks, zone_id)

        # Create a new MongoEngine document and save it to MongoDB
        new_deployment = OriginatingApplicationDeploymentManagement(**deployment_data)
        new_deployment.save()

        zone_response = ""
        if zone_in_blanks:
            zone_response = zone_id
        else:
            zone_response = body.zone_info.zone_id
        response_data = {
            "zoneId": zone_response,
            "appInstIdentifier": instance_id
        }
        deployment_response_data = InlineResponse202.from_dict(response_data)
    elif roleOp == util._ROLE_ORIGINATING_OP:
        try:
            # Extract the token from the header
            bearer_token = util.get_token_from_request(connexion)

            body = ApplicationLcmBody.from_dict(connexion.request.get_json())

            # Find federation at originating OP
            originating_op_objects = OriginatingOperatorPlatformOriginatingOP.objects(id=federation_context_id)
            if not originating_op_objects:
                return "Federation not found", 404
            originating_op_instance = originating_op_objects[0]

            # Create deployment at partner
            deployment_response_data = fm_client.install_app_deployment(originating_op_instance.partner_federation_id,
                                                                        connexion.request.get_json(), bearer_token)
            if "appInstIdentifier" in deployment_response_data:
                install_app_originating_op(federation_context_id, originating_op_instance.partner_federation_id, body,
                                           deployment_response_data)
                return deployment_response_data, 202
            else:
                return deployment_response_data, 422
        except Exception as error:
            return f"Error installing application. Reason: {error}", 422
    else:
        return "Error: Not assigned role to the operator (originating_op|partner_op)", 422

    return deployment_response_data, 202

def remove_app(federation_context_id, app_id, app_instance_id, zone_id):  # noqa: E501
    """Terminate an application instance on a partner OP zone.

     # noqa: E501

    :param federation_context_id:
    :type federation_context_id: dict | bytes
    :param app_id:
    :type app_id: dict | bytes
    :param app_instance_id:
    :type app_instance_id: dict | bytes
    :param zone_id:
    :type zone_id: dict | bytes

    :rtype: None
    """
    if roleOp == util._ROLE_PARTNER_OP:
        # Check if exist Federation Context Id in Operator Platform
        try:
            originating_op_objects = OriginatingOperatorPlatform.objects(id=federation_context_id)
            if not originating_op_objects:
                abort(404, "Federation not found at Operator Platform")
        except Exception as error:
            #abort(422, f"Incorrect value for Federation. Error: {error}")
            abort(422, f"Error: {error}")

        # Check if exist Federation Context Id and App Id in Application Onboarding Management
        originating_ao_objects = OriginatingApplicationOnboardingManagement.objects(
            orig_ao_federation_context_id=federation_context_id,
            orig_ao_app_id=app_id)
        if not originating_ao_objects:
            abort(404, "Federation Context and App Id not Found at Application Onboarding Management")

        # # Check if exist zone id at i2edge
        # try:
        #     if not i2edge.get_zone_by_zone_id(zone_id):
        #         abort(422, "Zone Id not found at i2edge")
        # except Exception as error:
        #     abort(422, f"Unable to find Zone Id at i2edge. Error: {error}")

        onboarding_instance = originating_ao_objects.get()
        # check if exist zone for this federation at Availability Zones of onboarding
        # Because zone id of the deployment can be assigned automatically if we do not specify the zone
        # when create deployment, it has not sense this validation
        #if not check_zone_by_federation_and_onboarding(zone_id, onboarding_instance):
        #    abort(422, f"Zone id not found for this Federation at Availability Zones and onboarding")

        # Check if exist application deployment by federation id, app Id, instance Id and zone Id
        originating_ad_objects = OriginatingApplicationDeploymentManagement.objects(
            orig_ad_federation_context_id=federation_context_id,
            orig_ad_app_id=app_id,
            orig_ad_instance_id=app_instance_id,
            orig_ad_zone_info_zone_id=zone_id
        )
        if not originating_ad_objects:
            abort(404, "Application Deployment Management Not Found by Federation Context, "
                       "appId, appInstanceId and zoneId")

        # Check if exist instance id at i2edge and delete
        response = i2edge.get_app_by_zone_ap_name(zone_id, app_instance_id)
        if response.status_code == 200 or response.status_code == 503:
            # Delete Application command at i2edge
            try:
                response = i2edge.delete_app(app_instance_id)
                if response.status_code == 200:
                    # Delete Application Deployment
                    originating_ad_objects.delete()
                else:
                    abort(422, f"Unable to delete App Command at i2edge. Error {response.status_code} - {response.content}")
            except Exception as error:
                abort(422, f"Unable to delete App Command. Error: {error}")
        else:
            abort(422, f"Unable to delete App Command. Error {response.status_code} - {response.content}")
    elif roleOp == util._ROLE_ORIGINATING_OP:
        # Extract the token from the header
        bearer_token = util.get_token_from_request(connexion)

        # Find federation at originating OP
        originating_op_objects = OriginatingOperatorPlatformOriginatingOP.objects(id=federation_context_id)
        if not originating_op_objects:
            return "Federation not found", 404
        originating_op_instance = originating_op_objects[0]
        # Find application deployment details at partner
        deployment_response_data = fm_client.get_instance_details_deployment(
            originating_op_instance.partner_federation_id,
            app_id, app_instance_id,
            zone_id, bearer_token)

        if "appInstanceState" in deployment_response_data:
            originating_ad_objects = find_instance_details(federation_context_id, app_id, app_instance_id, zone_id)
            if originating_ad_objects:
                # Delete application deployment at partner
                response_data = fm_client.remove_app_deployment(originating_op_instance.partner_federation_id, app_id, app_instance_id,
                                                                zone_id, bearer_token)
                if "termination" in response_data:
                    # If application deployment has been removed well, remove application deployment from originating
                    originating_ad_objects.delete()
                    return response_data, 200
                else:
                    return response_data, 422
            else:
                return "Application Deployment exist at partner operator but not in originating operator", 409
        else:
            if find_instance_details(federation_context_id, app_id, app_instance_id, zone_id):
                return "Application Deployment exist in originating operator but not at partner operator", 409
            else:
                return "Application Deployment not found", 404
    else:
        return "Error: Not assigned role to the operator (originating_op|partner_op)", 200

    return 'Application instance termination request accepted', 200

def fill_application_deployment_mongo_document(federation_context_id, instance_id, body, zone_in_blanks, zone_id):

    zone = ""
    if zone_in_blanks:
        zone = zone_id
    else:
        zone = body.zone_info.zone_id
    deployment_data = {
        "orig_ad_federation_context_id": federation_context_id,
        "orig_ad_instance_id": instance_id,
        "orig_ad_app_id": body.app_id,
        "orig_ad_app_version": body.app_version,
        "orig_ad_app_provider_id": body.app_provider_id,
        "orig_ad_zone_info_zone_id": zone,
        "orig_ad_zone_info_flavour_id": body.zone_info.flavour_id,
        "orig_ad_zone_info_resource_consumption": body.zone_info.resource_consumption,
        "orig_ad_zone_info_res_pool": body.zone_info.res_pool,
        "orig_ad_app_inst_callback_link": body.app_inst_callback_link
    }

    return deployment_data

def check_zone_and_flavour(body):
    correct = True

    zone_data = i2edge.get_zone_by_zone_id(body.zone_info.zone_id)
    if not zone_data:
        return False

    flavours = zone_data.get("flavoursSupported")
    if len(flavours) < 1:
        return False

    found_flavour = False
    for f in flavours:
        if f.get("flavourId") == body.zone_info.flavour_id:
            found_flavour = True
            break
    if not found_flavour:
        return False

    return correct

def check_zone_by_federation_and_onboarding(zone_id, onboarding_instance):
    exist_zone = True

    # check Zones of the Onboarding
    zones = onboarding_instance.orig_ao_app_deployment_zones

    # Check if exist Zone Id in Availability Zones of the onboarding
    if zones and zone_id not in zones:
        exist_zone = False

    return exist_zone

# Get the list of zones with their instances
def get_list_zones_instances(instances_deployment):
    zone_previous = ""
    zones = []
    instances = []
    for query in instances_deployment.order_by('orig_ad_zone_info_zone_id', 'orig_ad_instance_id'):
        if zone_previous == "":
            zone_previous = query.orig_ad_zone_info_zone_id

        if zone_previous != query.orig_ad_zone_info_zone_id:
            zones.append([zone_previous, instances])
            zone_previous = query.orig_ad_zone_info_zone_id
            instances = []

        instances.append(query.orig_ad_instance_id)

    if len(instances) > 0:
        zones.append([zone_previous, instances])

    return zones

def fill_app_command_post_i2edge(body, zone_in_blanks):

    zone_id = ""
    if not zone_in_blanks:
        zone_id = body.zone_info.zone_id
    data = {
        "app_deploy_data": {
            "appId": body.app_id,
            "appProviderId": body.app_provider_id,
            "appVersion": body.app_version,
            "zoneInfo": {
                "flavourId": body.zone_info.flavour_id,
                "zoneId": zone_id
            }
        }
    }

    return data

# Check if exist flavour in some zone of i2edge
def check_flavour_in_i2edge(flavour_id):
    exist = False

    zone_data = i2edge.get_zones()
    if not zone_data:
        return False

    found_flavour = False
    for zone in zone_data:
        if found_flavour:
            break
        flavours = zone.get("flavoursSupported")
        if flavours and len(flavours) > 0:
            for f in flavours:
                 if f.get("flavourId") == flavour_id:
                     exist = True
                     found_flavour = True
                     break
    return exist

def find_instance_state(zone_id, instance_id):
    instance_state = ""

    try:
        response = i2edge.get_app_by_zone_ap_name(zone_id, instance_id)
        if response.status_code != 200:
            return f"Error {response.status_code} - {response.content}"
        data = response.json()
        instance_state = data.get("appInstanceState")
    except Exception as error:
        return f"Error: {error}"

    return instance_state

def create_response_instance_details(zone_id, instance_id):
    response_data = ""

    try:
        response = i2edge.get_app_by_zone_ap_name(zone_id, instance_id)
        data = response.json()

        if isinstance(data, dict):
            list_points_info = []

            for point in data.get("accesspointInfo"):
                access_points = point.get("accessPoints")
                port = access_points.get("port")
                if not port:
                    port = 0
                list_points_info.append(
                    {
                        "interfaceId": point.get("interfaceId"),
                        "accessPoints": {
                            "port": port,
                            "fqdn": access_points.get("fqdn"),
                            "ipv4Addresses": access_points.get("ipv4Addresses"),
                            "ipv6Addresses": []
                        }
                    }
                )

            response_data = {
                "appInstanceState": data.get("appInstanceState"),
                "accesspointInfo": list_points_info
            }
        else:
            response_data = ""

    except:
        response_data = ""

    return response_data


def install_app_originating_op(federation_id, partner_federation_id, body, response_partner):
    # Convert the original model instance to the MongoEngine document
    deployment_data = {
        "orig_ad_federation_context_id": federation_id,
        "orig_ad_instance_id": response_partner.get("appInstIdentifier"),
        "orig_ad_app_id": body.app_id,
        "orig_ad_app_version": body.app_version,
        "orig_ad_app_provider_id": body.app_provider_id,
        "orig_ad_zone_info_zone_id": response_partner.get("zoneId"),
        "orig_ad_zone_info_flavour_id": body.zone_info.flavour_id,
        "orig_ad_zone_info_resource_consumption": body.zone_info.resource_consumption,
        "orig_ad_zone_info_res_pool": body.zone_info.res_pool,
        "orig_ad_app_inst_callback_link": body.app_inst_callback_link,
        "partner_federation_id": partner_federation_id
    }
    # Create a new MongoEngine document and save it to MongoDB
    new_deployment = OriginatingApplicationDeploymentManagementOriginatingOP(**deployment_data)
    new_deployment.save()


def find_all_instances_originating_op(federation_id, app_id, app_provider_id):
    originating_ad_objects = OriginatingApplicationDeploymentManagementOriginatingOP.objects(
        orig_ad_federation_context_id=federation_id,
        orig_ad_app_id=app_id,
        orig_ad_app_provider_id=app_provider_id
    )
    return originating_ad_objects


def find_instance_details(federation_id, app_id, instance_id, zone_id):
    originating_ad_objects = OriginatingApplicationDeploymentManagementOriginatingOP.objects(
        orig_ad_federation_context_id=federation_id,
        orig_ad_app_id=app_id,
        orig_ad_instance_id=instance_id,
        orig_ad_zone_info_zone_id=zone_id
    )
    return originating_ad_objects
