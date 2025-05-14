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
from models.app_component_specs import AppComponentSpecs  # noqa: F401,E501
from models.app_identifier import AppIdentifier  # noqa: F401,E501
from models.app_meta_data import AppMetaData  # noqa: F401,E501
from models.app_provider_id import AppProviderId  # noqa: F401,E501
from models.app_qo_s_profile import AppQoSProfile  # noqa: F401,E501
from models.inline_response2007_app_deployment_zones import InlineResponse2007AppDeploymentZones  # noqa: F401,E501
import re  # noqa: F401,E501
import util


class InlineResponse2007(Model):
    def __init__(self, app_id: AppIdentifier=None, app_provider_id: AppProviderId=None, app_deployment_zones: List[InlineResponse2007AppDeploymentZones]=None, app_meta_data: AppMetaData=None, app_qo_s_profile: AppQoSProfile=None, app_component_specs: AppComponentSpecs=None):  # noqa: E501
        """InlineResponse2007 - a model defined in Swagger

        :param app_id: The app_id of this InlineResponse2007.  # noqa: E501
        :type app_id: AppIdentifier
        :param app_provider_id: The app_provider_id of this InlineResponse2007.  # noqa: E501
        :type app_provider_id: AppProviderId
        :param app_deployment_zones: The app_deployment_zones of this InlineResponse2007.  # noqa: E501
        :type app_deployment_zones: List[InlineResponse2007AppDeploymentZones]
        :param app_meta_data: The app_meta_data of this InlineResponse2007.  # noqa: E501
        :type app_meta_data: AppMetaData
        :param app_qo_s_profile: The app_qo_s_profile of this InlineResponse2007.  # noqa: E501
        :type app_qo_s_profile: AppQoSProfile
        :param app_component_specs: The app_component_specs of this InlineResponse2007.  # noqa: E501
        :type app_component_specs: AppComponentSpecs
        """
        self.swagger_types = {
            'app_id': AppIdentifier,
            'app_provider_id': AppProviderId,
            'app_deployment_zones': List[InlineResponse2007AppDeploymentZones],
            'app_meta_data': AppMetaData,
            'app_qo_s_profile': AppQoSProfile,
            'app_component_specs': AppComponentSpecs
        }

        self.attribute_map = {
            'app_id': 'appId',
            'app_provider_id': 'appProviderId',
            'app_deployment_zones': 'appDeploymentZones',
            'app_meta_data': 'appMetaData',
            'app_qo_s_profile': 'appQoSProfile',
            'app_component_specs': 'appComponentSpecs'
        }
        self._app_id = app_id
        self._app_provider_id = app_provider_id
        self._app_deployment_zones = app_deployment_zones
        self._app_meta_data = app_meta_data
        self._app_qo_s_profile = app_qo_s_profile
        self._app_component_specs = app_component_specs

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2007':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_7 of this InlineResponse2007.  # noqa: E501
        :rtype: InlineResponse2007
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_id(self) -> AppIdentifier:
        """Gets the app_id of this InlineResponse2007.


        :return: The app_id of this InlineResponse2007.
        :rtype: AppIdentifier
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id: AppIdentifier):
        """Sets the app_id of this InlineResponse2007.


        :param app_id: The app_id of this InlineResponse2007.
        :type app_id: AppIdentifier
        """
        if app_id is None:
            raise ValueError("Invalid value for `app_id`, must not be `None`")  # noqa: E501

        self._app_id = app_id

    @property
    def app_provider_id(self) -> AppProviderId:
        """Gets the app_provider_id of this InlineResponse2007.


        :return: The app_provider_id of this InlineResponse2007.
        :rtype: AppProviderId
        """
        return self._app_provider_id

    @app_provider_id.setter
    def app_provider_id(self, app_provider_id: AppProviderId):
        """Sets the app_provider_id of this InlineResponse2007.


        :param app_provider_id: The app_provider_id of this InlineResponse2007.
        :type app_provider_id: AppProviderId
        """
        if app_provider_id is None:
            raise ValueError("Invalid value for `app_provider_id`, must not be `None`")  # noqa: E501

        self._app_provider_id = app_provider_id

    @property
    def app_deployment_zones(self) -> List[InlineResponse2007AppDeploymentZones]:
        """Gets the app_deployment_zones of this InlineResponse2007.

        Details about partner OP zones where the application should be made available;  This field when specified will instruct the OP to restrict application instantiation only on the listed zones.  # noqa: E501

        :return: The app_deployment_zones of this InlineResponse2007.
        :rtype: List[InlineResponse2007AppDeploymentZones]
        """
        return self._app_deployment_zones

    @app_deployment_zones.setter
    def app_deployment_zones(self, app_deployment_zones: List[InlineResponse2007AppDeploymentZones]):
        """Sets the app_deployment_zones of this InlineResponse2007.

        Details about partner OP zones where the application should be made available;  This field when specified will instruct the OP to restrict application instantiation only on the listed zones.  # noqa: E501

        :param app_deployment_zones: The app_deployment_zones of this InlineResponse2007.
        :type app_deployment_zones: List[InlineResponse2007AppDeploymentZones]
        """
        if app_deployment_zones is None:
            raise ValueError("Invalid value for `app_deployment_zones`, must not be `None`")  # noqa: E501

        self._app_deployment_zones = app_deployment_zones

    @property
    def app_meta_data(self) -> AppMetaData:
        """Gets the app_meta_data of this InlineResponse2007.


        :return: The app_meta_data of this InlineResponse2007.
        :rtype: AppMetaData
        """
        return self._app_meta_data

    @app_meta_data.setter
    def app_meta_data(self, app_meta_data: AppMetaData):
        """Sets the app_meta_data of this InlineResponse2007.


        :param app_meta_data: The app_meta_data of this InlineResponse2007.
        :type app_meta_data: AppMetaData
        """
        if app_meta_data is None:
            raise ValueError("Invalid value for `app_meta_data`, must not be `None`")  # noqa: E501

        self._app_meta_data = app_meta_data

    @property
    def app_qo_s_profile(self) -> AppQoSProfile:
        """Gets the app_qo_s_profile of this InlineResponse2007.


        :return: The app_qo_s_profile of this InlineResponse2007.
        :rtype: AppQoSProfile
        """
        return self._app_qo_s_profile

    @app_qo_s_profile.setter
    def app_qo_s_profile(self, app_qo_s_profile: AppQoSProfile):
        """Sets the app_qo_s_profile of this InlineResponse2007.


        :param app_qo_s_profile: The app_qo_s_profile of this InlineResponse2007.
        :type app_qo_s_profile: AppQoSProfile
        """
        if app_qo_s_profile is None:
            raise ValueError("Invalid value for `app_qo_s_profile`, must not be `None`")  # noqa: E501

        self._app_qo_s_profile = app_qo_s_profile

    @property
    def app_component_specs(self) -> AppComponentSpecs:
        """Gets the app_component_specs of this InlineResponse2007.


        :return: The app_component_specs of this InlineResponse2007.
        :rtype: AppComponentSpecs
        """
        return self._app_component_specs

    @app_component_specs.setter
    def app_component_specs(self, app_component_specs: AppComponentSpecs):
        """Sets the app_component_specs of this InlineResponse2007.


        :param app_component_specs: The app_component_specs of this InlineResponse2007.
        :type app_component_specs: AppComponentSpecs
        """
        if app_component_specs is None:
            raise ValueError("Invalid value for `app_component_specs`, must not be `None`")  # noqa: E501

        self._app_component_specs = app_component_specs
