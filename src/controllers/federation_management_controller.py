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
from models.federation_context_id import FederationContextId  # noqa: E501
from models.federation_context_id_partner_body import FederationContextIdPartnerBody  # noqa: E501
from models.federation_request_data import FederationRequestData  # noqa: E501
from models.mongo_document import OriginatingOperatorPlatform
from models.mongo_document import OriginatingOperatorPlatformUpdate
from models.federation_response_data import FederationResponseData  # noqa: E501
from models.inline_response2001 import InlineResponse2001  # noqa: E501
from models.inline_response2002 import InlineResponse2002  # noqa: E501
from models.problem_details import ProblemDetails  # noqa: E501
from models.mongo_document import OriginatingZoneInfo
from models.mongo_document import OriginatingArtefactManagement
from configparser import ConfigParser
from flask import abort
from clients import i2edge
from clients import fed_manager as fm_client
import util
from models.mongo_document import OriginatingOperatorPlatformOriginatingOP
from models.mongo_document import OriginatingOperatorPlatformUpdateOriginatingOP

CONFIG = ConfigParser()
CONFIG.read("conf/config.cfg")
partnerOPFederationId = CONFIG.get("op_data", "partnerOPFederationId")
partnerOPCountryCode = CONFIG.get("op_data", "partnerOPCountryCode")
partnerOPMobileNetworkCode_MCC = CONFIG.get("op_data", "partnerOPMobileNetworkCode_MCC")
partnerOPMobileNetworkCode_MNC = CONFIG.get("op_data", "partnerOPMobileNetworkCode_MNC")
partnerOPFixedNetworkCode = CONFIG.get("op_data", "partnerOPFixedNetworkCode")
platformCaps = CONFIG.get("op_data", "platformCaps")
roleOp = CONFIG.get("partner_op", "role")


def create_federation(body):  # noqa: E501
    """Creates one direction federation with partner operator platform.

     # noqa: E501

    :param body:
    :type body: dict | bytes

    :rtype: FederationResponseData
    """
    # Extract the token from the header
    bearer_token = util.get_token_from_request(connexion)

    if connexion.request.is_json:
        try:
            body = FederationRequestData.from_dict(connexion.request.get_json())  # noqa: E501
        except Exception as error:
            abort(422, f"Federation Validation Error. Message: {error}")

        if roleOp == util._ROLE_PARTNER_OP:
            # Convert the original model instance to the MongoEngine document
            federation_data = {
                "orig_op_federation_id": body.orig_op_federation_id,
                "orig_op_country_code": body.orig_op_country_code,
                "orig_op_mobile_network_codes_mcc": body.orig_op_mobile_network_codes.mcc,
                "orig_op_mobile_network_codes_mncs": body.orig_op_mobile_network_codes.mncs,
                "orig_op_fixed_network_codes": body.orig_op_fixed_network_codes,
                "initial_date": body.initial_date,
                "partner_status_link": body.partner_status_link,
                "partner_callback_credentials_token_url": body.partner_callback_credentials.token_url,
                "partner_callback_credentials_client_id": body.partner_callback_credentials.client_id,
                "partner_callback_credentials_client_secret": body.partner_callback_credentials.client_secret,
                "partner_bearer_token": bearer_token
            }

            # Verifies this is a new federation request
            all_originating_ops = OriginatingOperatorPlatform.objects()
            for originating_op in all_originating_ops:
                if originating_op.partner_bearer_token == bearer_token:
                    abort(409, "Federation already exists")

            # Create a new MongoEngine document and save it to MongoDB
            new_federation = OriginatingOperatorPlatform(**federation_data)
            new_federation.save()

            # Retrieve zone list from i2edge
            try:
                zones_list = prepareOfferedAvailabilityZones()
            except:
                abort(422, "Unable to get zones list from i2edge")

            response_data = {
                "federationContextId": str(new_federation.id),
                "partnerOPFederationId": partnerOPFederationId,
                "partnerOPCountryCode": partnerOPCountryCode,
                "partnerOPMobileNetworkCodes": {
                    "mcc": partnerOPMobileNetworkCode_MCC,
                    "mncs": [
                        partnerOPMobileNetworkCode_MNC
                    ]
                },
                "partnerOPFixedNetworkCodes": [
                    partnerOPFixedNetworkCode
                ],
                "platformCaps": [],
                "edgeDiscoveryServiceEndPoint": {},
                "lcmServiceEndPoint": {},
                "offeredAvailabilityZones": zones_list
            }
            federation_response_data = FederationResponseData.from_dict(response_data)
        elif roleOp == util._ROLE_ORIGINATING_OP:
            try:
                # Call partner FM
                federation_response_data = fm_client.create_federation(bearer_token, connexion.request.get_json())
                # If success create federation in the database saving partner federation id too
                if federation_response_data.get("federationContextId"):
                    federation_response_data = create_federation_at_originating_op(bearer_token, body,
                                                                               federation_response_data)
                    return federation_response_data, 200
                else:
                    return federation_response_data, 422
            except Exception as error:
                federation_response_data = {f"Error while creating Federation. Reason: {error}"}
        else:
            federation_response_data = {"Error": "Not assigned role to the operator (originating_op|partner_op)"}

    return federation_response_data, 200


def get_federation_details(federation_context_id):  # noqa: E501
    """Retrieves details about the federation context with the partner OP. The response shall provide info about the zones offered by the partner, partner OP network codes, information about edge discovery and LCM service etc.

     # noqa: E501

    :param federation_context_id:
    :type federation_context_id: dict | bytes

    :rtype: InlineResponse2001
    """
    if roleOp == util._ROLE_PARTNER_OP:
        try:
            originating_op_objects = OriginatingOperatorPlatform.objects(id=federation_context_id)
            if not originating_op_objects:
                abort(404, "Federation not found")
            originating_op_instance = originating_op_objects[0]
        except Exception as error:
            abort(422, f"Incorrect value for Federation. Error: {error}")

        # Retrieve zone list from i2edge
        try:
            zones_list = prepareOfferedAvailabilityZones()
        except:
            abort(422, "Unable to get zones list from i2edge")

        response_data = {
            "edgeDiscoveryServiceEndPoint": {},
            "lcmServiceEndPoint": {},
            "allowedMobileNetworkIds": {
                "mcc": originating_op_instance.orig_op_mobile_network_codes_mcc,
                "mncs": originating_op_instance.orig_op_mobile_network_codes_mncs
            },
            "allowedFixedNetworkIds": originating_op_instance.orig_op_fixed_network_codes,
            "offeredAvailabilityZones": zones_list
        }
        federation_response_data = InlineResponse2001.from_dict(response_data)
    elif roleOp == util._ROLE_ORIGINATING_OP:
        try:
            # Extract the token from the header
            bearer_token = util.get_token_from_request(connexion)

            # Find federation at originating OP
            originating_op_objects = OriginatingOperatorPlatformOriginatingOP.objects(id=federation_context_id)
            if not originating_op_objects:
                return "Federation not found", 404
            originating_op_instance = originating_op_objects[0]

            federation_response_data = fm_client.get_federation(originating_op_instance.partner_federation_id, bearer_token)
            if "edgeDiscoveryServiceEndPoint" in federation_response_data:
                return federation_response_data, 200
            else:
                return f"Conflict between originating operator and partner operator. Reason: {federation_response_data}", 422
        except Exception as error:
            return f"Error while getting Federation. Reason: {error}", 422
    else:
        federation_response_data = {"Error": "Not assigned role to the operator (originating_op|partner_op)"}

    return federation_response_data


def update_federation(body, federation_context_id):  # noqa: E501
    """API used by the Originating OP towards the partner OP, to update the parameters associated to the existing federation

     # noqa: E501

    :param body: Details about changes origination OP wished to apply
    :type body: dict | bytes
    :param federation_context_id:
    :type federation_context_id: dict | bytes

    :rtype: InlineResponse2001
    """
    if roleOp == util._ROLE_PARTNER_OP:
        try:
            originating_op_objects = OriginatingOperatorPlatform.objects(id=federation_context_id)
            if not originating_op_objects:
                abort(404, "Federation not found")
            originating_op_instance = originating_op_objects[0]
        except Exception as error:
            abort(422, f"Incorrect value for Federation. Error: {error}")

        if connexion.request.is_json:
            try:
                body = FederationContextIdPartnerBody.from_dict(connexion.request.get_json())  # noqa: E501
            except Exception as error:
                abort(422, f"Federation Validation Error. Message: {error}")

            partner_update_data = {
                "object_type": body.object_type,
                "operation_type": body.operation_type,
                "modification_date": body.modification_date,
                "add_mobile_network_ids_mcc": body.add_mobile_network_ids.mcc,
                "add_mobile_network_ids_mncs": body.add_mobile_network_ids.mncs,
                "remove_mobile_network_ids_mcc": body.remove_mobile_network_ids.mcc,
                "remove_mobile_network_ids_mncs": body.remove_mobile_network_ids.mncs,
                "add_fixed_network_ids": body.add_fixed_network_ids,
                "remove_fixed_network_ids": body.remove_fixed_network_ids,
                "federation_context_id": originating_op_instance
            }

            # originating_op_instance.orig_op_mobile_network_codes_mncs = mncs
            #
            # # Save the changes to the database
            # originating_op_instance.save()

            if body.object_type == "MOBILE_NETWORK_CODES":
                mncs = originating_op_instance.orig_op_mobile_network_codes_mncs
                if body.operation_type == "ADD_CODES":
                    if body.add_mobile_network_ids.mcc != originating_op_instance.orig_op_mobile_network_codes_mcc:
                        abort(409, "MCC does not match with the one registered")
                    mncs.extend(body.add_mobile_network_ids.mncs)
                    originating_op_instance.update(set__orig_op_mobile_network_codes_mncs=mncs)
                elif body.operation_type == "REMOVE_CODES":
                    if body.remove_mobile_network_ids.mcc != originating_op_instance.orig_op_mobile_network_codes_mcc:
                        abort(409, "MCC does not match with the one registered")
                    mncs = [code for code in mncs if code not in body.remove_mobile_network_ids.mncs]
                    originating_op_instance.update(set__orig_op_mobile_network_codes_mncs=mncs)
                elif body.operation_type == "UPDATE_CODES":
                    originating_op_instance.update(set__orig_op_mobile_network_codes_mcc=body.add_mobile_network_ids.mcc)
                    mncs = body.add_mobile_network_ids.mncs
                    if body.remove_mobile_network_ids.mcc == body.add_mobile_network_ids.mcc:
                        mncs = [code for code in body.add_mobile_network_ids.mncs if code not in body.remove_mobile_network_ids.mncs]
                    originating_op_instance.update(set__orig_op_mobile_network_codes_mncs=mncs)
            elif body.object_type == "FIXED_NETWORK_CODES":
                original_fixed_codes = originating_op_instance.orig_op_fixed_network_codes
                if body.operation_type == "ADD_CODES":
                    fixed_codes = original_fixed_codes
                    fixed_codes.extend(body.add_fixed_network_ids)
                    originating_op_instance.update(set__orig_op_fixed_network_codes=fixed_codes)
                if body.operation_type == "REMOVE_CODES":
                    fixed_codes = [code for code in original_fixed_codes if code not in body.remove_fixed_network_ids]
                    originating_op_instance.update(set__orig_op_fixed_network_codes=fixed_codes)
                elif body.operation_type == "UPDATE_CODES":
                    fixed_codes = [code for code in body.add_fixed_network_ids if code not in body.remove_fixed_network_ids]
                    originating_op_instance.update(set__orig_op_fixed_network_codes=fixed_codes)

            # Create a new MongoEngine document and save it to MongoDB
            new_partner_update = OriginatingOperatorPlatformUpdate(**partner_update_data)
            new_partner_update.save()

            # Retrieve zone list from i2edge
            try:
                zones_list = prepareOfferedAvailabilityZones()
            except:
                abort(422, "Unable to get zones list from i2edge")

            response_data = {
                "edgeDiscoveryServiceEndPoint": {},
                "lcmServiceEndPoint": {},
                "allowedMobileNetworkIds": {
                    "mcc": originating_op_instance.orig_op_mobile_network_codes_mcc,
                    "mncs": originating_op_instance.orig_op_mobile_network_codes_mncs
                },
                "allowedFixedNetworkIds": originating_op_instance.orig_op_fixed_network_codes,
                "offeredAvailabilityZones": zones_list
            }
            federation_response_data = InlineResponse2001.from_dict(response_data)
    elif roleOp == util._ROLE_ORIGINATING_OP:
        try:
            # Extract the token from the header
            bearer_token = util.get_token_from_request(connexion)

            # Find federation at originating OP
            originating_op_objects = OriginatingOperatorPlatformOriginatingOP.objects(id=federation_context_id)
            if not originating_op_objects:
                return "Federation not found", 404
            originating_op_instance = originating_op_objects[0]

            federation_response_data = fm_client.update_federation(bearer_token, originating_op_instance.partner_federation_id,
                                                                    connexion.request.get_json())
            # If success update federation in the database saving partner federation id too
            if "edgeDiscoveryServiceEndPoint" in federation_response_data:
                body = FederationContextIdPartnerBody.from_dict(connexion.request.get_json())
                federation_response_data = update_federation_at_originating_op(bearer_token, originating_op_instance,
                                                                               body, federation_response_data)
                return federation_response_data, 200
            else:
                return f"Conflict between originating operator and partner operator. Reason: {federation_response_data}", 422
        except Exception as error:
            return f"Error while updating Federation. Reason: {error}", 422
    else:
        federation_response_data = {"Error": "Not assigned role to the operator (originating_op|partner_op)"}

    return federation_response_data


def delete_federation_details(federation_context_id):  # noqa: E501
    """Remove existing federation with the partner OP

     # noqa: E501

    :param federation_context_id:
    :type federation_context_id: dict | bytes

    :rtype: None
    """
    if roleOp == util._ROLE_PARTNER_OP:
        try:
            originating_op_objects = OriginatingOperatorPlatform.objects(id=federation_context_id)
            if not originating_op_objects:
                abort(404, "Federation not found")
            originating_op_instance = originating_op_objects[0]
        except Exception as error:
            abort(422, f"Incorrect value for Federation. Error: {error}")

        # Check if there are zones or artefacts dependents of the federation
        if check_childs_federation(federation_context_id):
            abort(409,
                  "Unable to remove Federation. There are availability zones dependent. Remove it and try again ")

        # Delete all the federation updates related to federation
        id_federation = originating_op_instance.id
        originating_op_instance_update_objects = OriginatingOperatorPlatformUpdate.objects()
        for o in originating_op_instance_update_objects:
            try:
                if o.federation_context_id.pk == id_federation:
                    o.delete()
            except:
                pass

        # Delete Federation
        originating_op_instance.delete()
    elif roleOp == util._ROLE_ORIGINATING_OP:
        try:
            # Extract the token from the header
            bearer_token = util.get_token_from_request(connexion)

            # Find federation at originating OP
            originating_op_objects = OriginatingOperatorPlatformOriginatingOP.objects(id=federation_context_id)
            if not originating_op_objects:
                return "Federation not found", 404
            originating_op_instance = originating_op_objects[0]

            response_data = fm_client.delete_federation(originating_op_instance.partner_federation_id, bearer_token)
            if "removed" in response_data:
                deleteFederationOriginatingOP(originating_op_instance)
                return response_data, 200
            else:
                return f"Conflict between originating operator and partner operator. Reason: {response_data}", 422
        except Exception as error:
            return f"Error while deleting Federation. Reason: {error}", 422
    else:
        return "Error: Not assigned role to the operator (originating_op|partner_op)", 200

    return 'Federation removed successfully', 200


def get_federation_context_id():  # noqa: E501
    """Retrieves the existing federationContextId with partner operator platform.

     # noqa: E501


    :rtype: InlineResponse2002
    """
    # Access the Authorization header
    authorization_header = connexion.request.headers.get('Authorization')

    # Check if the header is present and starts with 'Bearer'
    if authorization_header and authorization_header.startswith('Bearer '):
        # Extract the token from the header
        bearer_token = authorization_header.split(' ')[1]

    originating_op_objects = OriginatingOperatorPlatform.objects(partner_bearer_token=bearer_token)
    if not originating_op_objects:
        abort(404, "Federation not found")
    originating_op_instance = originating_op_objects[0]
    federation_context_id_data = {
        "federationContextId": str(originating_op_instance.id)
    }
    federation_context_id = FederationContextId.from_dict(federation_context_id_data)

    return federation_context_id


def prepareOfferedAvailabilityZones():
    """
    # Get the zones list from i2edge
    zones = i2edge.get_zones_list()
    # Creates an array only with zone id from zones list
    zone_id_array = []
    for zone in zones:
        # If the zone value is a dict, is a correct zone, else there is an issue and returns a str
        if isinstance(zone, dict):
            zone_id_array.append(zone.get("zoneId"))

    # remove duplicates
    set_zones = set(zone_id_array)
    zone_id_array = list(set_zones)

    offered_zones_array = []

    for zone_id in zone_id_array:

        # If the availability zone matches with one of the zones of i2edge
        # includes this zone in a table to mount response data
        for zone in zones:
            if zone_id == zone.get("zoneId"):
                zone_data = {
                    "zoneId": zone.get("zoneId"),
                    "geographyDetails": zone.get("geographyDetails"),
                    "geolocation": zone.get("geolocation")
                }
                offered_zones_array.append(zone_data)
                break
    """
    offered_zones_array = []

    # Get the zones list from i2edge
    zones = i2edge.get_zones()
    for zone in zones:
        # If the zone value is a dict, is a correct zone, else there is an issue and returns a str
        if isinstance(zone, dict):
            geolocation = zone.get("geolocation").replace("_", ",")

            array_numbers = geolocation.split(",")
            numberone  = float(array_numbers[0])
            numbertwo = float(array_numbers[1])
            numberone_4 = f"{numberone:.4f}"
            numbertwo_4 = f"{numbertwo:.4f}"

            geolocation = f"{numberone_4},{numbertwo_4}"  # 4 decimals

            zone_data = {
                "zoneId": zone.get("zoneId"),
                "geographyDetails": zone.get("geographyDetails"),
                "geolocation": geolocation
            }
            offered_zones_array.append(zone_data)

    return offered_zones_array

def check_childs_federation(federation_context_id):
    found = False

    # Check zones
    originating_az_objects = OriginatingZoneInfo.objects(
        orig_zi_federation_context_id=federation_context_id
    )
    if originating_az_objects:
        return True

    # Check Artefacts
    originating_am_objects = OriginatingArtefactManagement.objects(
        orig_am_federation_context_id=federation_context_id)

    if originating_am_objects:
        return True

    return found

def create_federation_at_originating_op(bearer_token, body, federation_response_data):
    federation_data = {
        "orig_op_federation_id": body.orig_op_federation_id,
        "orig_op_country_code": body.orig_op_country_code,
        "orig_op_mobile_network_codes_mcc": body.orig_op_mobile_network_codes.mcc,
        "orig_op_mobile_network_codes_mncs": body.orig_op_mobile_network_codes.mncs,
        "orig_op_fixed_network_codes": body.orig_op_fixed_network_codes,
        "initial_date": body.initial_date,
        "partner_status_link": body.partner_status_link,
        "partner_callback_credentials_token_url": body.partner_callback_credentials.token_url,
        "partner_callback_credentials_client_id": body.partner_callback_credentials.client_id,
        "partner_callback_credentials_client_secret": body.partner_callback_credentials.client_secret,
        "partner_bearer_token": bearer_token,
        "partner_federation_id": federation_response_data.get("federationContextId")
    }

    # Create a new MongoEngine document and save it to MongoDB
    new_federation = OriginatingOperatorPlatformOriginatingOP(**federation_data)
    new_federation.save()

    # Retrieve zone list from i2edge
    try:
        zones_list = prepareOfferedAvailabilityZones()
    except:
        abort(422, "Unable to get zones list from i2edge")

    response_data = {
        "federationContextId": str(new_federation.id),
        "partnerOPFederationId": partnerOPFederationId,
        "partnerOPCountryCode": partnerOPCountryCode,
        "partnerOPMobileNetworkCodes": {
            "mcc": partnerOPMobileNetworkCode_MCC,
            "mncs": [
                partnerOPMobileNetworkCode_MNC
            ]
        },
        "partnerOPFixedNetworkCodes": [
            partnerOPFixedNetworkCode
        ],
        "platformCaps": [
            platformCaps
        ],
        "edgeDiscoveryServiceEndPoint": {},
        "lcmServiceEndPoint": {},
        "offeredAvailabilityZones": zones_list
    }

    return response_data

def update_federation_at_originating_op(bearer_token, originating_op_instance, body, federation_response_data):
    partner_update_data = {
        "object_type": body.object_type,
        "operation_type": body.operation_type,
        "modification_date": body.modification_date,
        "add_mobile_network_ids_mcc": body.add_mobile_network_ids.mcc,
        "add_mobile_network_ids_mncs": body.add_mobile_network_ids.mncs,
        "remove_mobile_network_ids_mcc": body.remove_mobile_network_ids.mcc,
        "remove_mobile_network_ids_mncs": body.remove_mobile_network_ids.mncs,
        "add_fixed_network_ids": body.add_fixed_network_ids,
        "remove_fixed_network_ids": body.remove_fixed_network_ids,
        "federation_context_id": originating_op_instance,
        "partner_federation_id": originating_op_instance.partner_federation_id
    }

    # Create a new MongoEngine document and save it to MongoDB
    new_federation = OriginatingOperatorPlatformUpdateOriginatingOP(**partner_update_data)
    new_federation.save()

    # Retrieve zone list from i2edge
    try:
        zones_list = prepareOfferedAvailabilityZones()
    except:
        abort(422, "Unable to get zones list from i2edge")

    response_data = {
        "edgeDiscoveryServiceEndPoint": {},
        "lcmServiceEndPoint": {},
        "allowedMobileNetworkIds": {
            "mcc": originating_op_instance.orig_op_mobile_network_codes_mcc,
            "mncs": originating_op_instance.orig_op_mobile_network_codes_mncs
        },
        "allowedFixedNetworkIds": originating_op_instance.orig_op_fixed_network_codes,
        "offeredAvailabilityZones": zones_list
    }

    return response_data

def deleteFederationOriginatingOP(originating_op_instance):
    # Delete all the federation updates related to federation
    id_federation = originating_op_instance.id
    originating_op_instance_update_objects = OriginatingOperatorPlatformUpdateOriginatingOP.objects()
    for o in originating_op_instance_update_objects:
        try:
            if o.federation_context_id.pk == id_federation:
                o.delete()
        except:
            pass

    # Delete Federation
    originating_op_instance.delete()
