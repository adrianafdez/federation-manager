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
from models.service_endpoint import ServiceEndpoint  # noqa: F401,E501
import re  # noqa: F401,E501
import util


class InlineResponse2008AccesspointInfo(Model):
    def __init__(self, interface_id: str=None, access_points: ServiceEndpoint=None):  # noqa: E501
        """InlineResponse2008AccesspointInfo - a model defined in Swagger

        :param interface_id: The interface_id of this InlineResponse2008AccesspointInfo.  # noqa: E501
        :type interface_id: str
        :param access_points: The access_points of this InlineResponse2008AccesspointInfo.  # noqa: E501
        :type access_points: ServiceEndpoint
        """
        self.swagger_types = {
            'interface_id': str,
            'access_points': ServiceEndpoint
        }

        self.attribute_map = {
            'interface_id': 'interfaceId',
            'access_points': 'accessPoints'
        }
        self._interface_id = interface_id
        self._access_points = access_points

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2008AccesspointInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_8_accesspointInfo of this InlineResponse2008AccesspointInfo.  # noqa: E501
        :rtype: InlineResponse2008AccesspointInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def interface_id(self) -> str:
        """Gets the interface_id of this InlineResponse2008AccesspointInfo.

        This is the interface identifier that app provider defines when application is onboarded.  # noqa: E501

        :return: The interface_id of this InlineResponse2008AccesspointInfo.
        :rtype: str
        """
        return self._interface_id

    @interface_id.setter
    def interface_id(self, interface_id: str):
        """Sets the interface_id of this InlineResponse2008AccesspointInfo.

        This is the interface identifier that app provider defines when application is onboarded.  # noqa: E501

        :param interface_id: The interface_id of this InlineResponse2008AccesspointInfo.
        :type interface_id: str
        """
        if interface_id is None:
            raise ValueError("Invalid value for `interface_id`, must not be `None`")  # noqa: E501

        self._interface_id = interface_id

    @property
    def access_points(self) -> ServiceEndpoint:
        """Gets the access_points of this InlineResponse2008AccesspointInfo.


        :return: The access_points of this InlineResponse2008AccesspointInfo.
        :rtype: ServiceEndpoint
        """
        return self._access_points

    @access_points.setter
    def access_points(self, access_points: ServiceEndpoint):
        """Sets the access_points of this InlineResponse2008AccesspointInfo.


        :param access_points: The access_points of this InlineResponse2008AccesspointInfo.
        :type access_points: ServiceEndpoint
        """
        if access_points is None:
            raise ValueError("Invalid value for `access_points`, must not be `None`")  # noqa: E501

        self._access_points = access_points
