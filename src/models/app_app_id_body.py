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
from models.federation_context_idapplicationonboardingappapp_id_app_component_specs import FederationContextIdapplicationonboardingappappIdAppComponentSpecs  # noqa: F401,E501
from models.federation_context_idapplicationonboardingappapp_id_app_upd_qo_s_profile import FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile  # noqa: F401,E501
import util


class AppAppIdBody(Model):
    def __init__(self, app_upd_qo_s_profile: FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile=None, app_component_specs: List[FederationContextIdapplicationonboardingappappIdAppComponentSpecs]=None):  # noqa: E501
        """AppAppIdBody - a model defined in Swagger

        :param app_upd_qo_s_profile: The app_upd_qo_s_profile of this AppAppIdBody.  # noqa: E501
        :type app_upd_qo_s_profile: FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile
        :param app_component_specs: The app_component_specs of this AppAppIdBody.  # noqa: E501
        :type app_component_specs: List[FederationContextIdapplicationonboardingappappIdAppComponentSpecs]
        """
        self.swagger_types = {
            'app_upd_qo_s_profile': FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile,
            'app_component_specs': List[FederationContextIdapplicationonboardingappappIdAppComponentSpecs]
        }

        self.attribute_map = {
            'app_upd_qo_s_profile': 'appUpdQoSProfile',
            'app_component_specs': 'appComponentSpecs'
        }
        self._app_upd_qo_s_profile = app_upd_qo_s_profile
        self._app_component_specs = app_component_specs

    @classmethod
    def from_dict(cls, dikt) -> 'AppAppIdBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The app_appId_body of this AppAppIdBody.  # noqa: E501
        :rtype: AppAppIdBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_upd_qo_s_profile(self) -> FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile:
        """Gets the app_upd_qo_s_profile of this AppAppIdBody.


        :return: The app_upd_qo_s_profile of this AppAppIdBody.
        :rtype: FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile
        """
        return self._app_upd_qo_s_profile

    @app_upd_qo_s_profile.setter
    def app_upd_qo_s_profile(self, app_upd_qo_s_profile: FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile):
        """Sets the app_upd_qo_s_profile of this AppAppIdBody.


        :param app_upd_qo_s_profile: The app_upd_qo_s_profile of this AppAppIdBody.
        :type app_upd_qo_s_profile: FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile
        """

        self._app_upd_qo_s_profile = app_upd_qo_s_profile

    @property
    def app_component_specs(self) -> List[FederationContextIdapplicationonboardingappappIdAppComponentSpecs]:
        """Gets the app_component_specs of this AppAppIdBody.

        An application may consist of more than one component. Each component is associated with a descriptor and may exposes its services externally or internally.  App providers are required to provide details about all these components, their associated descriptors and their DNS names.  # noqa: E501

        :return: The app_component_specs of this AppAppIdBody.
        :rtype: List[FederationContextIdapplicationonboardingappappIdAppComponentSpecs]
        """
        return self._app_component_specs

    @app_component_specs.setter
    def app_component_specs(self, app_component_specs: List[FederationContextIdapplicationonboardingappappIdAppComponentSpecs]):
        """Sets the app_component_specs of this AppAppIdBody.

        An application may consist of more than one component. Each component is associated with a descriptor and may exposes its services externally or internally.  App providers are required to provide details about all these components, their associated descriptors and their DNS names.  # noqa: E501

        :param app_component_specs: The app_component_specs of this AppAppIdBody.
        :type app_component_specs: List[FederationContextIdapplicationonboardingappappIdAppComponentSpecs]
        """

        self._app_component_specs = app_component_specs
