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
from models.inline_response2008_accesspoint_info import InlineResponse2008AccesspointInfo  # noqa: F401,E501
from models.instance_state import InstanceState  # noqa: F401,E501
import util


class InlineResponse2008(Model):
    def __init__(self, app_instance_state: InstanceState=None, accesspoint_info: List[InlineResponse2008AccesspointInfo]=None):  # noqa: E501
        """InlineResponse2008 - a model defined in Swagger

        :param app_instance_state: The app_instance_state of this InlineResponse2008.  # noqa: E501
        :type app_instance_state: InstanceState
        :param accesspoint_info: The accesspoint_info of this InlineResponse2008.  # noqa: E501
        :type accesspoint_info: List[InlineResponse2008AccesspointInfo]
        """
        self.swagger_types = {
            'app_instance_state': InstanceState,
            'accesspoint_info': List[InlineResponse2008AccesspointInfo]
        }

        self.attribute_map = {
            'app_instance_state': 'appInstanceState',
            'accesspoint_info': 'accesspointInfo'
        }
        self._app_instance_state = app_instance_state
        self._accesspoint_info = accesspoint_info

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2008':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_8 of this InlineResponse2008.  # noqa: E501
        :rtype: InlineResponse2008
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_instance_state(self) -> InstanceState:
        """Gets the app_instance_state of this InlineResponse2008.


        :return: The app_instance_state of this InlineResponse2008.
        :rtype: InstanceState
        """
        return self._app_instance_state

    @app_instance_state.setter
    def app_instance_state(self, app_instance_state: InstanceState):
        """Sets the app_instance_state of this InlineResponse2008.


        :param app_instance_state: The app_instance_state of this InlineResponse2008.
        :type app_instance_state: InstanceState
        """

        self._app_instance_state = app_instance_state

    @property
    def accesspoint_info(self) -> List[InlineResponse2008AccesspointInfo]:
        """Gets the accesspoint_info of this InlineResponse2008.

        Information about the IP and Port exposed by the OP. Application clients shall use these access points to reach this application instance  # noqa: E501

        :return: The accesspoint_info of this InlineResponse2008.
        :rtype: List[InlineResponse2008AccesspointInfo]
        """
        return self._accesspoint_info

    @accesspoint_info.setter
    def accesspoint_info(self, accesspoint_info: List[InlineResponse2008AccesspointInfo]):
        """Sets the accesspoint_info of this InlineResponse2008.

        Information about the IP and Port exposed by the OP. Application clients shall use these access points to reach this application instance  # noqa: E501

        :param accesspoint_info: The accesspoint_info of this InlineResponse2008.
        :type accesspoint_info: List[InlineResponse2008AccesspointInfo]
        """

        self._accesspoint_info = accesspoint_info
