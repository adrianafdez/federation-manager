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
from models.instance_state import InstanceState  # noqa: F401,E501
import re  # noqa: F401,E501
import util


class FederationContextIdapplicationlcmappappIdappProviderappProviderIdAppInstanceInfo(Model):
    def __init__(self, app_inst_identifier: InstanceIdentifier=None, app_instance_state: InstanceState=None):  # noqa: E501
        """FederationContextIdapplicationlcmappappIdappProviderappProviderIdAppInstanceInfo - a model defined in Swagger

        :param app_inst_identifier: The app_inst_identifier of this FederationContextIdapplicationlcmappappIdappProviderappProviderIdAppInstanceInfo.  # noqa: E501
        :type app_inst_identifier: InstanceIdentifier
        :param app_instance_state: The app_instance_state of this FederationContextIdapplicationlcmappappIdappProviderappProviderIdAppInstanceInfo.  # noqa: E501
        :type app_instance_state: InstanceState
        """
        self.swagger_types = {
            'app_inst_identifier': InstanceIdentifier,
            'app_instance_state': InstanceState
        }

        self.attribute_map = {
            'app_inst_identifier': 'appInstIdentifier',
            'app_instance_state': 'appInstanceState'
        }
        self._app_inst_identifier = app_inst_identifier
        self._app_instance_state = app_instance_state

    @classmethod
    def from_dict(cls, dikt) -> 'FederationContextIdapplicationlcmappappIdappProviderappProviderIdAppInstanceInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The federationContextIdapplicationlcmappappIdappProviderappProviderId_appInstanceInfo of this FederationContextIdapplicationlcmappappIdappProviderappProviderIdAppInstanceInfo.  # noqa: E501
        :rtype: FederationContextIdapplicationlcmappappIdappProviderappProviderIdAppInstanceInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_inst_identifier(self) -> InstanceIdentifier:
        """Gets the app_inst_identifier of this FederationContextIdapplicationlcmappappIdappProviderappProviderIdAppInstanceInfo.


        :return: The app_inst_identifier of this FederationContextIdapplicationlcmappappIdappProviderappProviderIdAppInstanceInfo.
        :rtype: InstanceIdentifier
        """
        return self._app_inst_identifier

    @app_inst_identifier.setter
    def app_inst_identifier(self, app_inst_identifier: InstanceIdentifier):
        """Sets the app_inst_identifier of this FederationContextIdapplicationlcmappappIdappProviderappProviderIdAppInstanceInfo.


        :param app_inst_identifier: The app_inst_identifier of this FederationContextIdapplicationlcmappappIdappProviderappProviderIdAppInstanceInfo.
        :type app_inst_identifier: InstanceIdentifier
        """
        if app_inst_identifier is None:
            raise ValueError("Invalid value for `app_inst_identifier`, must not be `None`")  # noqa: E501

        self._app_inst_identifier = app_inst_identifier

    @property
    def app_instance_state(self) -> InstanceState:
        """Gets the app_instance_state of this FederationContextIdapplicationlcmappappIdappProviderappProviderIdAppInstanceInfo.


        :return: The app_instance_state of this FederationContextIdapplicationlcmappappIdappProviderappProviderIdAppInstanceInfo.
        :rtype: InstanceState
        """
        return self._app_instance_state

    @app_instance_state.setter
    def app_instance_state(self, app_instance_state: InstanceState):
        """Sets the app_instance_state of this FederationContextIdapplicationlcmappappIdappProviderappProviderIdAppInstanceInfo.


        :param app_instance_state: The app_instance_state of this FederationContextIdapplicationlcmappappIdappProviderappProviderIdAppInstanceInfo.
        :type app_instance_state: InstanceState
        """
        if app_instance_state is None:
            raise ValueError("Invalid value for `app_instance_state`, must not be `None`")  # noqa: E501

        self._app_instance_state = app_instance_state
