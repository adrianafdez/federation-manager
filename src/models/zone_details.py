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

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from models.base_model_ import Model
from models.geo_location import GeoLocation  # noqa: F401,E501
from models.zone_identifier import ZoneIdentifier  # noqa: F401,E501
import re  # noqa: F401,E501
import util


class ZoneDetails(Model):
    def __init__(self, zone_id: ZoneIdentifier=None, geolocation: GeoLocation=None, geography_details: str=None):  # noqa: E501
        """ZoneDetails - a model defined in Swagger

        :param zone_id: The zone_id of this ZoneDetails.  # noqa: E501
        :type zone_id: ZoneIdentifier
        :param geolocation: The geolocation of this ZoneDetails.  # noqa: E501
        :type geolocation: GeoLocation
        :param geography_details: The geography_details of this ZoneDetails.  # noqa: E501
        :type geography_details: str
        """
        self.swagger_types = {
            'zone_id': ZoneIdentifier,
            'geolocation': GeoLocation,
            'geography_details': str
        }

        self.attribute_map = {
            'zone_id': 'zoneId',
            'geolocation': 'geolocation',
            'geography_details': 'geographyDetails'
        }
        self._zone_id = zone_id
        self._geolocation = geolocation
        self._geography_details = geography_details

    @classmethod
    def from_dict(cls, dikt) -> 'ZoneDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ZoneDetails of this ZoneDetails.  # noqa: E501
        :rtype: ZoneDetails
        """
        return util.deserialize_model(dikt, cls)

    @property
    def zone_id(self) -> ZoneIdentifier:
        """Gets the zone_id of this ZoneDetails.


        :return: The zone_id of this ZoneDetails.
        :rtype: ZoneIdentifier
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id: ZoneIdentifier):
        """Sets the zone_id of this ZoneDetails.


        :param zone_id: The zone_id of this ZoneDetails.
        :type zone_id: ZoneIdentifier
        """
        if zone_id is None:
            raise ValueError("Invalid value for `zone_id`, must not be `None`")  # noqa: E501

        self._zone_id = zone_id

    @property
    def geolocation(self) -> GeoLocation:
        """Gets the geolocation of this ZoneDetails.


        :return: The geolocation of this ZoneDetails.
        :rtype: GeoLocation
        """
        return self._geolocation

    @geolocation.setter
    def geolocation(self, geolocation: GeoLocation):
        """Sets the geolocation of this ZoneDetails.


        :param geolocation: The geolocation of this ZoneDetails.
        :type geolocation: GeoLocation
        """
        if geolocation is None:
            raise ValueError("Invalid value for `geolocation`, must not be `None`")  # noqa: E501

        self._geolocation = geolocation

    @property
    def geography_details(self) -> str:
        """Gets the geography_details of this ZoneDetails.

        Details about cities or state covered by the edge. Details about the type of locality for eg rural, urban, industrial etc. This information is defined in human readable form.  # noqa: E501

        :return: The geography_details of this ZoneDetails.
        :rtype: str
        """
        return self._geography_details

    @geography_details.setter
    def geography_details(self, geography_details: str):
        """Sets the geography_details of this ZoneDetails.

        Details about cities or state covered by the edge. Details about the type of locality for eg rural, urban, industrial etc. This information is defined in human readable form.  # noqa: E501

        :param geography_details: The geography_details of this ZoneDetails.
        :type geography_details: str
        """
        if geography_details is None:
            raise ValueError("Invalid value for `geography_details`, must not be `None`")  # noqa: E501

        self._geography_details = geography_details
