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
from models.app_identifier import AppIdentifier  # noqa: F401,E501
from models.app_provider_id import AppProviderId  # noqa: F401,E501
from models.federation_context_idapplicationlcm_zone_info import FederationContextIdapplicationlcmZoneInfo  # noqa: F401,E501
from models.uri import Uri  # noqa: F401,E501
import re  # noqa: F401,E501
import util


class ApplicationLcmBody(Model):
    def __init__(self, app_id: AppIdentifier=None, app_version: str=None, app_provider_id: AppProviderId=None, zone_info: FederationContextIdapplicationlcmZoneInfo=None, app_inst_callback_link: Uri=None):  # noqa: E501
        """ApplicationLcmBody - a model defined in Swagger

        :param app_id: The app_id of this ApplicationLcmBody.  # noqa: E501
        :type app_id: AppIdentifier
        :param app_version: The app_version of this ApplicationLcmBody.  # noqa: E501
        :type app_version: str
        :param app_provider_id: The app_provider_id of this ApplicationLcmBody.  # noqa: E501
        :type app_provider_id: AppProviderId
        :param zone_info: The zone_info of this ApplicationLcmBody.  # noqa: E501
        :type zone_info: FederationContextIdapplicationlcmZoneInfo
        :param app_inst_callback_link: The app_inst_callback_link of this ApplicationLcmBody.  # noqa: E501
        :type app_inst_callback_link: Uri
        """
        self.swagger_types = {
            'app_id': AppIdentifier,
            'app_version': str,
            'app_provider_id': AppProviderId,
            'zone_info': FederationContextIdapplicationlcmZoneInfo,
            'app_inst_callback_link': Uri
        }

        self.attribute_map = {
            'app_id': 'appId',
            'app_version': 'appVersion',
            'app_provider_id': 'appProviderId',
            'zone_info': 'zoneInfo',
            'app_inst_callback_link': 'appInstCallbackLink'
        }
        self._app_id = app_id
        self._app_version = app_version
        self._app_provider_id = app_provider_id
        self._zone_info = zone_info
        self._app_inst_callback_link = app_inst_callback_link

    @classmethod
    def from_dict(cls, dikt) -> 'ApplicationLcmBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The application_lcm_body of this ApplicationLcmBody.  # noqa: E501
        :rtype: ApplicationLcmBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_id(self) -> AppIdentifier:
        """Gets the app_id of this ApplicationLcmBody.


        :return: The app_id of this ApplicationLcmBody.
        :rtype: AppIdentifier
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id: AppIdentifier):
        """Sets the app_id of this ApplicationLcmBody.


        :param app_id: The app_id of this ApplicationLcmBody.
        :type app_id: AppIdentifier
        """
        if app_id is None:
            raise ValueError("Invalid value for `app_id`, must not be `None`")  # noqa: E501

        self._app_id = app_id

    @property
    def app_version(self) -> str:
        """Gets the app_version of this ApplicationLcmBody.

        Version info of the application  # noqa: E501

        :return: The app_version of this ApplicationLcmBody.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version: str):
        """Sets the app_version of this ApplicationLcmBody.

        Version info of the application  # noqa: E501

        :param app_version: The app_version of this ApplicationLcmBody.
        :type app_version: str
        """
        if app_version is None:
            raise ValueError("Invalid value for `app_version`, must not be `None`")  # noqa: E501

        self._app_version = app_version

    @property
    def app_provider_id(self) -> AppProviderId:
        """Gets the app_provider_id of this ApplicationLcmBody.


        :return: The app_provider_id of this ApplicationLcmBody.
        :rtype: AppProviderId
        """
        return self._app_provider_id

    @app_provider_id.setter
    def app_provider_id(self, app_provider_id: AppProviderId):
        """Sets the app_provider_id of this ApplicationLcmBody.


        :param app_provider_id: The app_provider_id of this ApplicationLcmBody.
        :type app_provider_id: AppProviderId
        """
        if app_provider_id is None:
            raise ValueError("Invalid value for `app_provider_id`, must not be `None`")  # noqa: E501

        self._app_provider_id = app_provider_id

    @property
    def zone_info(self) -> FederationContextIdapplicationlcmZoneInfo:
        """Gets the zone_info of this ApplicationLcmBody.


        :return: The zone_info of this ApplicationLcmBody.
        :rtype: FederationContextIdapplicationlcmZoneInfo
        """
        return self._zone_info

    @zone_info.setter
    def zone_info(self, zone_info: FederationContextIdapplicationlcmZoneInfo):
        """Sets the zone_info of this ApplicationLcmBody.


        :param zone_info: The zone_info of this ApplicationLcmBody.
        :type zone_info: FederationContextIdapplicationlcmZoneInfo
        """
        if zone_info is None:
            raise ValueError("Invalid value for `zone_info`, must not be `None`")  # noqa: E501

        self._zone_info = zone_info

    @property
    def app_inst_callback_link(self) -> Uri:
        """Gets the app_inst_callback_link of this ApplicationLcmBody.


        :return: The app_inst_callback_link of this ApplicationLcmBody.
        :rtype: Uri
        """
        return self._app_inst_callback_link

    @app_inst_callback_link.setter
    def app_inst_callback_link(self, app_inst_callback_link: Uri):
        """Sets the app_inst_callback_link of this ApplicationLcmBody.


        :param app_inst_callback_link: The app_inst_callback_link of this ApplicationLcmBody.
        :type app_inst_callback_link: Uri
        """
        if app_inst_callback_link is None:
            raise ValueError("Invalid value for `app_inst_callback_link`, must not be `None`")  # noqa: E501

        self._app_inst_callback_link = app_inst_callback_link
