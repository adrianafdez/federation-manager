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
from models.instance_identifier import InstanceIdentifier  # noqa: F401,E501
from models.zone_identifier import ZoneIdentifier  # noqa: F401,E501
import re  # noqa: F401,E501
import util


class InlineResponse202(Model):
    def __init__(self, zone_id: ZoneIdentifier=None, app_inst_identifier: InstanceIdentifier=None):  # noqa: E501
        """InlineResponse202 - a model defined in Swagger

        :param zone_id: The zone_id of this InlineResponse202.  # noqa: E501
        :type zone_id: ZoneIdentifier
        :param app_inst_identifier: The app_inst_identifier of this InlineResponse202.  # noqa: E501
        :type app_inst_identifier: InstanceIdentifier
        """
        self.swagger_types = {
            'zone_id': ZoneIdentifier,
            'app_inst_identifier': InstanceIdentifier
        }

        self.attribute_map = {
            'zone_id': 'zoneId',
            'app_inst_identifier': 'appInstIdentifier'
        }
        self._zone_id = zone_id
        self._app_inst_identifier = app_inst_identifier

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse202':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_202 of this InlineResponse202.  # noqa: E501
        :rtype: InlineResponse202
        """
        return util.deserialize_model(dikt, cls)

    @property
    def zone_id(self) -> ZoneIdentifier:
        """Gets the zone_id of this InlineResponse202.


        :return: The zone_id of this InlineResponse202.
        :rtype: ZoneIdentifier
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id: ZoneIdentifier):
        """Sets the zone_id of this InlineResponse202.


        :param zone_id: The zone_id of this InlineResponse202.
        :type zone_id: ZoneIdentifier
        """
        if zone_id is None:
            raise ValueError("Invalid value for `zone_id`, must not be `None`")  # noqa: E501

        self._zone_id = zone_id

    @property
    def app_inst_identifier(self) -> InstanceIdentifier:
        """Gets the app_inst_identifier of this InlineResponse202.


        :return: The app_inst_identifier of this InlineResponse202.
        :rtype: InstanceIdentifier
        """
        return self._app_inst_identifier

    @app_inst_identifier.setter
    def app_inst_identifier(self, app_inst_identifier: InstanceIdentifier):
        """Sets the app_inst_identifier of this InlineResponse202.


        :param app_inst_identifier: The app_inst_identifier of this InlineResponse202.
        :type app_inst_identifier: InstanceIdentifier
        """
        if app_inst_identifier is None:
            raise ValueError("Invalid value for `app_inst_identifier`, must not be `None`")  # noqa: E501

        self._app_inst_identifier = app_inst_identifier
