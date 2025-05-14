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
from models.federation_context_idapplicationlcmappapp_idapp_providerapp_provider_id_app_instance_info import FederationContextIdapplicationlcmappappIdappProviderappProviderIdAppInstanceInfo  # noqa: F401,E501
from models.zone_identifier import ZoneIdentifier  # noqa: F401,E501
import re  # noqa: F401,E501
import util


class InlineResponse2009(Model):
    def __init__(self, zone_id: ZoneIdentifier=None, app_instance_info: List[FederationContextIdapplicationlcmappappIdappProviderappProviderIdAppInstanceInfo]=None):  # noqa: E501
        """InlineResponse2009 - a model defined in Swagger

        :param zone_id: The zone_id of this InlineResponse2009.  # noqa: E501
        :type zone_id: ZoneIdentifier
        :param app_instance_info: The app_instance_info of this InlineResponse2009.  # noqa: E501
        :type app_instance_info: List[FederationContextIdapplicationlcmappappIdappProviderappProviderIdAppInstanceInfo]
        """
        self.swagger_types = {
            'zone_id': ZoneIdentifier,
            'app_instance_info': List[FederationContextIdapplicationlcmappappIdappProviderappProviderIdAppInstanceInfo]
        }

        self.attribute_map = {
            'zone_id': 'zoneId',
            'app_instance_info': 'appInstanceInfo'
        }
        self._zone_id = zone_id
        self._app_instance_info = app_instance_info

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2009':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_9 of this InlineResponse2009.  # noqa: E501
        :rtype: InlineResponse2009
        """
        return util.deserialize_model(dikt, cls)

    @property
    def zone_id(self) -> ZoneIdentifier:
        """Gets the zone_id of this InlineResponse2009.


        :return: The zone_id of this InlineResponse2009.
        :rtype: ZoneIdentifier
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id: ZoneIdentifier):
        """Sets the zone_id of this InlineResponse2009.


        :param zone_id: The zone_id of this InlineResponse2009.
        :type zone_id: ZoneIdentifier
        """
        if zone_id is None:
            raise ValueError("Invalid value for `zone_id`, must not be `None`")  # noqa: E501

        self._zone_id = zone_id

    @property
    def app_instance_info(self) -> List[FederationContextIdapplicationlcmappappIdappProviderappProviderIdAppInstanceInfo]:
        """Gets the app_instance_info of this InlineResponse2009.


        :return: The app_instance_info of this InlineResponse2009.
        :rtype: List[FederationContextIdapplicationlcmappappIdappProviderappProviderIdAppInstanceInfo]
        """
        return self._app_instance_info

    @app_instance_info.setter
    def app_instance_info(self, app_instance_info: List[FederationContextIdapplicationlcmappappIdappProviderappProviderIdAppInstanceInfo]):
        """Sets the app_instance_info of this InlineResponse2009.


        :param app_instance_info: The app_instance_info of this InlineResponse2009.
        :type app_instance_info: List[FederationContextIdapplicationlcmappappIdappProviderappProviderIdAppInstanceInfo]
        """
        if app_instance_info is None:
            raise ValueError("Invalid value for `app_instance_info`, must not be `None`")  # noqa: E501

        self._app_instance_info = app_instance_info
