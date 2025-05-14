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
import re  # noqa: F401,E501
import util


class AppMetaData(Model):
    def __init__(self, app_name: str=None, version: str=None, app_description: str=None, mobility_support: bool=False, access_token: str=None, category: str=None):  # noqa: E501
        """AppMetaData - a model defined in Swagger

        :param app_name: The app_name of this AppMetaData.  # noqa: E501
        :type app_name: str
        :param version: The version of this AppMetaData.  # noqa: E501
        :type version: str
        :param app_description: The app_description of this AppMetaData.  # noqa: E501
        :type app_description: str
        :param mobility_support: The mobility_support of this AppMetaData.  # noqa: E501
        :type mobility_support: bool
        :param access_token: The access_token of this AppMetaData.  # noqa: E501
        :type access_token: str
        :param category: The category of this AppMetaData.  # noqa: E501
        :type category: str
        """
        self.swagger_types = {
            'app_name': str,
            'version': str,
            'app_description': str,
            'mobility_support': bool,
            'access_token': str,
            'category': str
        }

        self.attribute_map = {
            'app_name': 'appName',
            'version': 'version',
            'app_description': 'appDescription',
            'mobility_support': 'mobilitySupport',
            'access_token': 'accessToken',
            'category': 'category'
        }
        self._app_name = app_name
        self._version = version
        self._app_description = app_description
        self._mobility_support = mobility_support
        self._access_token = access_token
        self._category = category

    @classmethod
    def from_dict(cls, dikt) -> 'AppMetaData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AppMetaData of this AppMetaData.  # noqa: E501
        :rtype: AppMetaData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_name(self) -> str:
        """Gets the app_name of this AppMetaData.

        Name of the application. Application provider define a human readable name for the application  # noqa: E501

        :return: The app_name of this AppMetaData.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name: str):
        """Sets the app_name of this AppMetaData.

        Name of the application. Application provider define a human readable name for the application  # noqa: E501

        :param app_name: The app_name of this AppMetaData.
        :type app_name: str
        """
        if app_name is None:
            raise ValueError("Invalid value for `app_name`, must not be `None`")  # noqa: E501

        self._app_name = app_name

    @property
    def version(self) -> str:
        """Gets the version of this AppMetaData.

        Version info of the application  # noqa: E501

        :return: The version of this AppMetaData.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str):
        """Sets the version of this AppMetaData.

        Version info of the application  # noqa: E501

        :param version: The version of this AppMetaData.
        :type version: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def app_description(self) -> str:
        """Gets the app_description of this AppMetaData.

        Brief application description provided by application provider  # noqa: E501

        :return: The app_description of this AppMetaData.
        :rtype: str
        """
        return self._app_description

    @app_description.setter
    def app_description(self, app_description: str):
        """Sets the app_description of this AppMetaData.

        Brief application description provided by application provider  # noqa: E501

        :param app_description: The app_description of this AppMetaData.
        :type app_description: str
        """

        self._app_description = app_description

    @property
    def mobility_support(self) -> bool:
        """Gets the mobility_support of this AppMetaData.

        Indicates if an application is sensitive to user mobility and can be relocated. Default is “FALSE”  # noqa: E501

        :return: The mobility_support of this AppMetaData.
        :rtype: bool
        """
        return self._mobility_support

    @mobility_support.setter
    def mobility_support(self, mobility_support: bool):
        """Sets the mobility_support of this AppMetaData.

        Indicates if an application is sensitive to user mobility and can be relocated. Default is “FALSE”  # noqa: E501

        :param mobility_support: The mobility_support of this AppMetaData.
        :type mobility_support: bool
        """

        self._mobility_support = mobility_support

    @property
    def access_token(self) -> str:
        """Gets the access_token of this AppMetaData.

        An application Access key, to be used with UNI interface to authorize UCs Access to a given application  # noqa: E501

        :return: The access_token of this AppMetaData.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token: str):
        """Sets the access_token of this AppMetaData.

        An application Access key, to be used with UNI interface to authorize UCs Access to a given application  # noqa: E501

        :param access_token: The access_token of this AppMetaData.
        :type access_token: str
        """
        if access_token is None:
            raise ValueError("Invalid value for `access_token`, must not be `None`")  # noqa: E501

        self._access_token = access_token

    @property
    def category(self) -> str:
        """Gets the category of this AppMetaData.

        Possible categorization of the application  # noqa: E501

        :return: The category of this AppMetaData.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category: str):
        """Sets the category of this AppMetaData.

        Possible categorization of the application  # noqa: E501

        :param category: The category of this AppMetaData.
        :type category: str
        """
        allowed_values = ["IOT", "HEALTH_CARE", "GAMING", "VIRTUAL_REALITY", "SOCIALIZING", "SURVEILLANCE", "ENTERTAINMENT", "CONNECTIVITY", "PRODUCTIVITY", "SECURITY", "INDUSTRIAL", "EDUCATION", "OTHERS"]  # noqa: E501
        if category not in allowed_values:
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}"
                .format(category, allowed_values)
            )

        self._category = category
