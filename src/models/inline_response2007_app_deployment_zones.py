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
from models.country_code import CountryCode  # noqa: F401,E501
from models.zone_identifier import ZoneIdentifier  # noqa: F401,E501
import re  # noqa: F401,E501
import util


class InlineResponse2007AppDeploymentZones(Model):
    def __init__(self, country_code: CountryCode=None, zone_info: ZoneIdentifier=None):  # noqa: E501
        """InlineResponse2007AppDeploymentZones - a model defined in Swagger

        :param country_code: The country_code of this InlineResponse2007AppDeploymentZones.  # noqa: E501
        :type country_code: CountryCode
        :param zone_info: The zone_info of this InlineResponse2007AppDeploymentZones.  # noqa: E501
        :type zone_info: ZoneIdentifier
        """
        self.swagger_types = {
            'country_code': CountryCode,
            'zone_info': ZoneIdentifier
        }

        self.attribute_map = {
            'country_code': 'countryCode',
            'zone_info': 'zoneInfo'
        }
        self._country_code = country_code
        self._zone_info = zone_info

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2007AppDeploymentZones':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_7_appDeploymentZones of this InlineResponse2007AppDeploymentZones.  # noqa: E501
        :rtype: InlineResponse2007AppDeploymentZones
        """
        return util.deserialize_model(dikt, cls)

    @property
    def country_code(self) -> CountryCode:
        """Gets the country_code of this InlineResponse2007AppDeploymentZones.


        :return: The country_code of this InlineResponse2007AppDeploymentZones.
        :rtype: CountryCode
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code: CountryCode):
        """Sets the country_code of this InlineResponse2007AppDeploymentZones.


        :param country_code: The country_code of this InlineResponse2007AppDeploymentZones.
        :type country_code: CountryCode
        """
        if country_code is None:
            raise ValueError("Invalid value for `country_code`, must not be `None`")  # noqa: E501

        self._country_code = country_code

    @property
    def zone_info(self) -> ZoneIdentifier:
        """Gets the zone_info of this InlineResponse2007AppDeploymentZones.


        :return: The zone_info of this InlineResponse2007AppDeploymentZones.
        :rtype: ZoneIdentifier
        """
        return self._zone_info

    @zone_info.setter
    def zone_info(self, zone_info: ZoneIdentifier):
        """Sets the zone_info of this InlineResponse2007AppDeploymentZones.


        :param zone_info: The zone_info of this InlineResponse2007AppDeploymentZones.
        :type zone_info: ZoneIdentifier
        """
        if zone_info is None:
            raise ValueError("Invalid value for `zone_info`, must not be `None`")  # noqa: E501

        self._zone_info = zone_info
