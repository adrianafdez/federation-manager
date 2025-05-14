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
import json
import six

from models.federation_context_id import FederationContextId  # noqa: E501
from models.problem_details import ProblemDetails  # noqa: E501
from models.zone_identifier import ZoneIdentifier  # noqa: E501
from models.zone_registered_data import ZoneRegisteredData  # noqa: E501
from models.zone_registration_request_data import ZoneRegistrationRequestData  # noqa: E501
from models.zone_registration_response_data import ZoneRegistrationResponseData  # noqa: E501
import util
from models.mongo_document import OriginatingOperatorPlatform
from models.mongo_document import OriginatingZoneInfo
from models.mongo_document import OriginatingApplicationOnboardingManagement
from flask import abort
from clients import i2edge
from configparser import ConfigParser
from clients import fed_manager as fm_client
from models.mongo_document import OriginatingOperatorPlatformOriginatingOP
from models.mongo_document import OriginatingZoneInfoOriginatingOP

CONFIG = ConfigParser()
CONFIG.read("conf/config.cfg")
roleOp = CONFIG.get("partner_op", "role")


def get_zone_data(federation_context_id, zone_id):  # noqa: E501
    """Retrieves details about the computation and network resources that partner OP has reserved for this zone.

     # noqa: E501

    :param federation_context_id:
    :type federation_context_id: dict | bytes
    :param zone_id:
    :type zone_id: dict | bytes

    :rtype: ZoneRegisteredData
    """
    if roleOp == util._ROLE_PARTNER_OP:
        # Check if exist Federation Context Id in Operator Platform
        try:
            originating_op_objects = OriginatingOperatorPlatform.objects(id=federation_context_id)
            if not originating_op_objects:
              abort(404, "Federation not found at Operator Platform")
        except Exception as error:
            abort(422, f"Incorrect value for Federation. Error: {error}")

        # Check if exist Federation Context Id in Availability Zones
        originating_zi_objects = OriginatingZoneInfo.objects(orig_zi_federation_context_id=federation_context_id)
        if not originating_zi_objects:
            abort(404, "Federation Context not found at Availability Zones")

        # Check if exist Zone at i2edge
        try:
            response_data = i2edge.get_zone_by_zone_id(zone_id)

            resource = response_data.get("computeResourceQuotaLimits")
            for d in resource:
                huge = d.get("hugepages")
                for h in huge:
                    page = h.get("pageSize")
                    page = page.replace("Gi", "GB")
                    page = page.replace("Mi", "MB")
                    h["pageSize"] = page
                d["hugepages"] = huge
            response_data["computeResourceQuotaLimits"] = resource
            pass

        except Exception as error:
            abort(422, f"Unable to retrieve zone from i2edge. Error: {error}")
        if not response_data:
            abort(404, "Zone id do not exist at i2edge")

        # check if Zone id is in the list of availability zones of the document
        zones = originating_zi_objects.get()
        if zone_id not in zones.orig_zi_acceptedAvailabilityZones:
            abort(404, "Zone id not found for this Federation Context")

        try:
            zone_response_data = ZoneRegisteredData.from_dict(response_data)
        except Exception as error:
            abort(422, f"Retrieving zone information with issues from i2edge. Error: {error}")
    elif roleOp == util._ROLE_ORIGINATING_OP:
        try:
            # Extract the token from the header
            bearer_token = util.get_token_from_request(connexion)

            # Find federation at originating OP
            originating_op_objects = OriginatingOperatorPlatformOriginatingOP.objects(id=federation_context_id)
            if not originating_op_objects:
                return "Federation not found", 404
            originating_op_instance = originating_op_objects[0]

            zone_response_data = fm_client.get_availability_zones(originating_op_instance.partner_federation_id, zone_id, bearer_token)
            if "zoneId" in zone_response_data:
                if check_zone_in_availability_zones_originating_op(federation_context_id, zone_id):
                    return zone_response_data, 200
                else:
                    return "Zone exist at partner operator but not in originating operator", 409
            else:
                if check_zone_in_availability_zones_originating_op(federation_context_id, zone_id):
                    return "Zone exist in originating operator but not at partner operator", 409
                else:
                    return "Zone not found", 404

        except Exception as error:
            return f"Error while getting Zones. Reason: {error}", 422
    else:
        zone_response_data = {"Error": "Not assigned role to the operator (originating_op|partner_op)"}

    return zone_response_data

def zone_subscribe(body, federation_context_id):  # noqa: E501
    """Originating OP informs partner OP that it is willing to access the specified zones and partner OP shall reserve compute and network resources for these zones.

     # noqa: E501

    :param body:
    :type body: dict | bytes
    :param federation_context_id:
    :type federation_context_id: dict | bytes

    :rtype: ZoneRegistrationResponseData
    """
    if roleOp == util._ROLE_PARTNER_OP:
        # Check if exist Federation Context Id in Operator Platform
        try:
            originating_op_objects = OriginatingOperatorPlatform.objects(id=federation_context_id)
            if not originating_op_objects:
                abort(404, "Federation not found at Operator Platform")
        except Exception as error:
            abort(422, f"Incorrect value for Federation. Error: {error}")

        # Check if exist availability zones in i2edge
        try:
            if not checkAvailabilityZones(body.get("acceptedAvailabilityZones")):
                abort(404, "Availability Zones do not exist at i2edge")
        except Exception as error:
            abort(422, f"Unable to get zones list from i2edge. Error: {error}")

        if connexion.request.is_json:
            try:
                body = ZoneRegistrationRequestData.from_dict(connexion.request.get_json())  # noqa: E501
            except Exception as error:
                abort(422, f"Zone Validation Error. Message: {error}")
        #if connexion.request.is_json:
        #    federation_context_id = FederationContextId.from_dict(connexion.request.get_json())  # noqa: E501

            # Convert the original model instance to the MongoEngine document
            zone_data = {
                "orig_zi_federation_context_id": federation_context_id,
                "orig_zi_acceptedAvailabilityZones": body.accepted_availability_zones,
                "orig_zi_availZoneNotifLink": body.avail_zone_notif_link
            }

            # Verifies this is a new zone request
            all_originating_zones = OriginatingZoneInfo.objects()
            for originating_zi in all_originating_zones:
                if originating_zi.orig_zi_federation_context_id == federation_context_id:
                    abort(409, "Availability Zone already exists for this Federation Context")

            # Create a new MongoEngine document and save it to MongoDB
            new_zone = OriginatingZoneInfo(**zone_data)
            new_zone.save()

            try:
                availability_zones = get_info_availability_zones_from_zones_i2edge(body.accepted_availability_zones)
            except Exception as error:
                abort(422, f"Unable to get zones from i2edge. Error: {error}")
            response_data = {
                "acceptedZoneResourceInfo": availability_zones
            }

            try:
                zone_response_data = ZoneRegistrationResponseData.from_dict(response_data)
            except Exception as error:
                abort(422, f"Retrieving zone information with issues from i2edge. Error: {error}")
    elif roleOp == util._ROLE_ORIGINATING_OP:
        try:
            # Extract the token from the header
            bearer_token = util.get_token_from_request(connexion)

            body = ZoneRegistrationRequestData.from_dict(connexion.request.get_json())

            # Find federation at originating OP
            originating_op_objects = OriginatingOperatorPlatformOriginatingOP.objects(id=federation_context_id)
            if not originating_op_objects:
                return "Federation not found", 404
            originating_op_instance = originating_op_objects[0]

            # Check if exist zones at partner
            if check_zones_in_availability_zones_partner(originating_op_instance.partner_federation_id, body, bearer_token):
                if check_zones_in_availability_zones_originating_op(federation_context_id, body):
                    return "Available zones already exist for this federation", 422
                else:
                    return "Available zones exist in partner operator but not in originating operator", 409
            else:
                if check_zones_in_availability_zones_originating_op(federation_context_id, body):
                    return "Available zones exist in originating operator but not in partner operator", 409
                else:
                    zone_response_data = fm_client.create_availability_zones(originating_op_instance.partner_federation_id,
                                                                             connexion.request.get_json(), bearer_token)
                    # If success create zone in the database saving partner federation id too
                    if "acceptedZoneResourceInfo" in zone_response_data:
                        zone_response_data = create_zone_at_originating_op(bearer_token, federation_context_id,
                                                                   originating_op_instance.partner_federation_id, body)
                        return zone_response_data, 200
                    else:
                        return zone_response_data, 422
        except Exception as error:
            return f"Error while creating Availability Zones. Reason: {error}", 422
    else:
        zone_response_data = {"Error": "Not assigned role to the operator (originating_op|partner_op)"}

    return zone_response_data


def zone_unsubscribe(federation_context_id, zone_id):  # noqa: E501
    """Assert usage of a partner OP zone. Originating OP informs partner OP that it will no longer access the specified zone.

     # noqa: E501

    :param federation_context_id:
    :type federation_context_id: dict | bytes
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
            abort(422, f"Incorrect value for Federation. Error: {error}")

        # Check if exist Federation Context Id in Availability Zones
        originating_zi_objects = OriginatingZoneInfo.objects(orig_zi_federation_context_id=federation_context_id)
        if not originating_zi_objects:
            abort(404, "Federation Context not found at Availability Zones")

        """
        # Check if exist Zone at i2edge
        try:
            response_data = i2edge.get_zone_by_zone_id(zone_id)
        except Exception as error:
            abort(422, f"Unable to get zone from i2edge. Error: {error}")
        if not response_data:
            abort(404, "Zone id do not exist at i2edge")
        """

        # check if Zone id is in the list of availability zones of the document
        zones = originating_zi_objects.get()
        if zone_id not in zones.orig_zi_acceptedAvailabilityZones:
            abort(404, "Zone id not found for this Federation Context")

        # Check if there are onboardings dependents of the zone
        if check_childs_availability_zones(federation_context_id, zone_id):
            abort(409,
                  "Unable to remove Zone. There are onboardings dependent. Remove it and try again ")

        # Get the list of the zones assigned to the federation context
        availability_zones = zones.orig_zi_acceptedAvailabilityZones
        try:
            # To prevent if returns list as a Str
            availability_zones = json.loads(availability_zones)
        except Exception as error:
            print(f"Unable to parse zone list JSON. Error: {error}")

        # Remove from the list the zone id passed as a parameter
        availability_zones.remove(zone_id)

        # If the list of zones becomes empty, we delete the document from the collection
        if len(availability_zones) == 0:
            originating_zi_objects.delete()
        else:
            # The list is not empty and we update the document with the new list
            zones.orig_zi_acceptedAvailabilityZones = availability_zones
            zones.save()
    elif roleOp == util._ROLE_ORIGINATING_OP:
        try:
            # Extract the token from the header
            bearer_token = util.get_token_from_request(connexion)

            # Find federation at originating OP
            originating_op_objects = OriginatingOperatorPlatformOriginatingOP.objects(id=federation_context_id)
            if not originating_op_objects:
                return "Federation not found", 404
            originating_op_instance = originating_op_objects[0]

            zone_response_data = fm_client.get_availability_zones(originating_op_instance.partner_federation_id,
                                                                  zone_id, bearer_token)
            if "zoneId" in zone_response_data:
                if check_zone_in_availability_zones_originating_op(federation_context_id, zone_id):
                    response_data = fm_client.delete_availability_zones(originating_op_instance.partner_federation_id,
                                                                        zone_id, bearer_token)
                    if "deregistered" in response_data:
                        deleteZoneOriginatingOP(federation_context_id, zone_id)
                        return response_data, 200
                    else:
                        return response_data, 422
                else:
                    return "Zone exist at partner operator but not in originating operator", 409
            else:
                if check_zone_in_availability_zones_originating_op(federation_context_id, zone_id):
                    return "Zone exist in originating operator but not at partner operator", 409
                else:
                    return "Zone not found", 404
        except Exception as error:
            return f"Error while deleting Zones. Reason: {error}", 422
    else:
        return "Error: Not assigned role to the operator (originating_op|partner_op)", 422

    return 'Zone deregistered successfully', 200


def checkAvailabilityZones(acceptedAvailabilityZones):

      # Get the zones list from i2edge
      zones = i2edge.get_zones()
      # Creates an array only with zone id from zones list
      zone_id_array = []
      for zone in zones:
          # If the zone value is a dict, is a correct zone, else there is an issue and returns a str
          if isinstance(zone, dict):
            zone_id_array.append(zone.get("zoneId"))
      # remove duplicates
      set_zones = set(zone_id_array)
      zone_id_array = list(set_zones)

      # Compare matches between zones from i2edge and zones declared in the body
      common = set(acceptedAvailabilityZones) & set(zone_id_array)

      # if the matches are equal to the number of zones declared in the body returns True
      if len(common) == len(acceptedAvailabilityZones):
        return True
      else:
        return False


def get_info_availability_zones_from_zones_i2edge(availability_zones):

    # Retrieve zones from i2edge
    info_zones_list = i2edge.get_zones()
    zones_for_federation = []

    # Loop zones assigned to our federation
    for availability_zone in availability_zones:

        # If the availability zone matches with one of the zones of i2edge
        # includes this zone in a table to mount response data
        exit = False
        for zone in info_zones_list:
            # If the zone value is a dict, is a correct zone, else there is an issue and returns a str
            if isinstance(zone, dict):
                if availability_zone == zone.get("zoneId"):
                    zones_for_federation.append(zone)
                    break

    return zones_for_federation

def check_childs_availability_zones(federation_context_id, zone_id):
    found = False

    originating_ao_objects = OriginatingApplicationOnboardingManagement.objects(
        orig_ao_federation_context_id=federation_context_id
    )
    if not originating_ao_objects:
        return False

    instances_onboarding = originating_ao_objects.filter()

    for elem in instances_onboarding:
        list_zones = elem.orig_ao_app_deployment_zones
        for l in list_zones:
            if l == zone_id:
                return True

def create_zone_at_originating_op(bearer_token, federation_context_id, partner_federation_id, body):
    zone_data = {
        "orig_zi_federation_context_id": federation_context_id,
        "orig_zi_acceptedAvailabilityZones": body.accepted_availability_zones,
        "orig_zi_availZoneNotifLink": body.avail_zone_notif_link,
        "partner_federation_id": partner_federation_id
    }

    # Create a new MongoEngine document and save it to MongoDB
    new_zone = OriginatingZoneInfoOriginatingOP(**zone_data)
    new_zone.save()

    try:
        availability_zones = get_info_availability_zones_from_zones_i2edge(body.accepted_availability_zones)
    except Exception as error:
        abort(422, f"Unable to get zones from i2edge. Error: {error}")
    response_data = {
        "acceptedZoneResourceInfo": availability_zones
    }

    return response_data

def deleteZoneOriginatingOP(federation_id, zone_id):
    # Check if exist Federation Context Id in Availability Zones
    originating_zi_objects = OriginatingZoneInfoOriginatingOP.objects(orig_zi_federation_context_id=federation_id)
    if not originating_zi_objects:
        abort(404, "Federation Context not found at Availability Zones")

    zones = originating_zi_objects.get()

    # Get the list of the zones assigned to the federation context
    availability_zones = zones.orig_zi_acceptedAvailabilityZones
    try:
        # To prevent if returns list as a Str
        availability_zones = json.loads(availability_zones)
    except Exception as error:
        print(f"Unable to parse zone list JSON. Error: {error}")

    # Remove from the list the zone id passed as a parameter
    availability_zones.remove(zone_id)

    # If the list of zones becomes empty, we delete the document from the collection
    if len(availability_zones) == 0:
        originating_zi_objects.delete()
    else:
        # The list is not empty and we update the document with the new list
        zones.orig_zi_acceptedAvailabilityZones = availability_zones
        zones.save()

def check_zone_in_availability_zones_originating_op(federation_id, zone_id):
    exist_zone = False

    originating_zi_objects = OriginatingZoneInfoOriginatingOP.objects(orig_zi_federation_context_id=federation_id)
    if originating_zi_objects:
        zones = originating_zi_objects.get()
        if zone_id in zones.orig_zi_acceptedAvailabilityZones:
            exist_zone = True
        else:
            exist_zone = False
    else:
        exist_zone = False

    return exist_zone

def check_zones_in_availability_zones_partner(federation_id, body, token):
    exist = False

    for zone in body.accepted_availability_zones:
        response_data = fm_client.get_availability_zones(federation_id, zone, token)
        if "zoneId" in response_data:
            exist = True

    return exist

def check_zones_in_availability_zones_originating_op(federation_id, body):
    exist = False

    originating_zi_objects = OriginatingZoneInfoOriginatingOP.objects(orig_zi_federation_context_id=federation_id)
    if not originating_zi_objects:
        return False
    zones = originating_zi_objects.get()

    for zone in body.accepted_availability_zones:
        if zone in zones.orig_zi_acceptedAvailabilityZones:
            exist = True

    return exist
