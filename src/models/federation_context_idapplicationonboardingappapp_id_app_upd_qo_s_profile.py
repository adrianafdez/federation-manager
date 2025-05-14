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
import util


class FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile(Model):
    def __init__(self, latency_constraints: str=None, bandwidth_required: int=None, mobility_support: bool=False, multi_user_clients: str=None, no_of_users_per_app_inst: int=1, app_provisioning: bool=True):  # noqa: E501
        """FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile - a model defined in Swagger

        :param latency_constraints: The latency_constraints of this FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile.  # noqa: E501
        :type latency_constraints: str
        :param bandwidth_required: The bandwidth_required of this FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile.  # noqa: E501
        :type bandwidth_required: int
        :param mobility_support: The mobility_support of this FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile.  # noqa: E501
        :type mobility_support: bool
        :param multi_user_clients: The multi_user_clients of this FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile.  # noqa: E501
        :type multi_user_clients: str
        :param no_of_users_per_app_inst: The no_of_users_per_app_inst of this FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile.  # noqa: E501
        :type no_of_users_per_app_inst: int
        :param app_provisioning: The app_provisioning of this FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile.  # noqa: E501
        :type app_provisioning: bool
        """
        self.swagger_types = {
            'latency_constraints': str,
            'bandwidth_required': int,
            'mobility_support': bool,
            'multi_user_clients': str,
            'no_of_users_per_app_inst': int,
            'app_provisioning': bool
        }

        self.attribute_map = {
            'latency_constraints': 'latencyConstraints',
            'bandwidth_required': 'bandwidthRequired',
            'mobility_support': 'mobilitySupport',
            'multi_user_clients': 'multiUserClients',
            'no_of_users_per_app_inst': 'noOfUsersPerAppInst',
            'app_provisioning': 'appProvisioning'
        }
        self._latency_constraints = latency_constraints
        self._bandwidth_required = bandwidth_required
        self._mobility_support = mobility_support
        self._multi_user_clients = multi_user_clients
        self._no_of_users_per_app_inst = no_of_users_per_app_inst
        self._app_provisioning = app_provisioning

    @classmethod
    def from_dict(cls, dikt) -> 'FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The federationContextIdapplicationonboardingappappId_appUpdQoSProfile of this FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile.  # noqa: E501
        :rtype: FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile
        """
        return util.deserialize_model(dikt, cls)

    @property
    def latency_constraints(self) -> str:
        """Gets the latency_constraints of this FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile.

        Latency requirements for the application.Allowed values (non-standardized) are none, low and ultra-low. Ultra-Low may corresponds to range 15 - 30 msec, Low correspond to range 30 - 50 msec. None means 51 and above  # noqa: E501

        :return: The latency_constraints of this FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile.
        :rtype: str
        """
        return self._latency_constraints

    @latency_constraints.setter
    def latency_constraints(self, latency_constraints: str):
        """Sets the latency_constraints of this FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile.

        Latency requirements for the application.Allowed values (non-standardized) are none, low and ultra-low. Ultra-Low may corresponds to range 15 - 30 msec, Low correspond to range 30 - 50 msec. None means 51 and above  # noqa: E501

        :param latency_constraints: The latency_constraints of this FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile.
        :type latency_constraints: str
        """
        allowed_values = ["NONE", "LOW", "ULTRALOW"]  # noqa: E501
        if latency_constraints not in allowed_values:
            raise ValueError(
                "Invalid value for `latency_constraints` ({0}), must be one of {1}"
                .format(latency_constraints, allowed_values)
            )

        self._latency_constraints = latency_constraints

    @property
    def bandwidth_required(self) -> int:
        """Gets the bandwidth_required of this FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile.

        Data transfer bandwidth requirement (minimum limit) for the application. It should in Mbits/sec  # noqa: E501

        :return: The bandwidth_required of this FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile.
        :rtype: int
        """
        return self._bandwidth_required

    @bandwidth_required.setter
    def bandwidth_required(self, bandwidth_required: int):
        """Sets the bandwidth_required of this FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile.

        Data transfer bandwidth requirement (minimum limit) for the application. It should in Mbits/sec  # noqa: E501

        :param bandwidth_required: The bandwidth_required of this FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile.
        :type bandwidth_required: int
        """

        self._bandwidth_required = bandwidth_required

    @property
    def mobility_support(self) -> bool:
        """Gets the mobility_support of this FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile.

        Indicates if an application is sensitive to user mobility and can be relocated. Default is “FALSE”  # noqa: E501

        :return: The mobility_support of this FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile.
        :rtype: bool
        """
        return self._mobility_support

    @mobility_support.setter
    def mobility_support(self, mobility_support: bool):
        """Sets the mobility_support of this FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile.

        Indicates if an application is sensitive to user mobility and can be relocated. Default is “FALSE”  # noqa: E501

        :param mobility_support: The mobility_support of this FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile.
        :type mobility_support: bool
        """

        self._mobility_support = mobility_support

    @property
    def multi_user_clients(self) -> str:
        """Gets the multi_user_clients of this FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile.

        Single user type application are designed to serve just one client. Multi user type application is designed to serve multiple clients  # noqa: E501

        :return: The multi_user_clients of this FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile.
        :rtype: str
        """
        return self._multi_user_clients

    @multi_user_clients.setter
    def multi_user_clients(self, multi_user_clients: str):
        """Sets the multi_user_clients of this FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile.

        Single user type application are designed to serve just one client. Multi user type application is designed to serve multiple clients  # noqa: E501

        :param multi_user_clients: The multi_user_clients of this FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile.
        :type multi_user_clients: str
        """
        allowed_values = ["APP_TYPE_SINGLE_USER", "APP_TYPE_MULTI_USER"]  # noqa: E501
        if multi_user_clients not in allowed_values:
            raise ValueError(
                "Invalid value for `multi_user_clients` ({0}), must be one of {1}"
                .format(multi_user_clients, allowed_values)
            )

        self._multi_user_clients = multi_user_clients

    @property
    def no_of_users_per_app_inst(self) -> int:
        """Gets the no_of_users_per_app_inst of this FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile.

        Maximum no of clients that can connect to an instance of this application. This parameter is relevant only for application of type multi user  # noqa: E501

        :return: The no_of_users_per_app_inst of this FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile.
        :rtype: int
        """
        return self._no_of_users_per_app_inst

    @no_of_users_per_app_inst.setter
    def no_of_users_per_app_inst(self, no_of_users_per_app_inst: int):
        """Sets the no_of_users_per_app_inst of this FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile.

        Maximum no of clients that can connect to an instance of this application. This parameter is relevant only for application of type multi user  # noqa: E501

        :param no_of_users_per_app_inst: The no_of_users_per_app_inst of this FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile.
        :type no_of_users_per_app_inst: int
        """

        self._no_of_users_per_app_inst = no_of_users_per_app_inst

    @property
    def app_provisioning(self) -> bool:
        """Gets the app_provisioning of this FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile.

        Define if application can be instantiated or not  # noqa: E501

        :return: The app_provisioning of this FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile.
        :rtype: bool
        """
        return self._app_provisioning

    @app_provisioning.setter
    def app_provisioning(self, app_provisioning: bool):
        """Sets the app_provisioning of this FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile.

        Define if application can be instantiated or not  # noqa: E501

        :param app_provisioning: The app_provisioning of this FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile.
        :type app_provisioning: bool
        """

        self._app_provisioning = app_provisioning
