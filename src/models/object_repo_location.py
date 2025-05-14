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
from models.uri import Uri  # noqa: F401,E501
import util


class ObjectRepoLocation(Model):
    def __init__(self, repo_url: Uri=None, user_name: str=None, password: str=None, token: str=None):  # noqa: E501
        """ObjectRepoLocation - a model defined in Swagger

        :param repo_url: The repo_url of this ObjectRepoLocation.  # noqa: E501
        :type repo_url: Uri
        :param user_name: The user_name of this ObjectRepoLocation.  # noqa: E501
        :type user_name: str
        :param password: The password of this ObjectRepoLocation.  # noqa: E501
        :type password: str
        :param token: The token of this ObjectRepoLocation.  # noqa: E501
        :type token: str
        """
        self.swagger_types = {
            'repo_url': Uri,
            'user_name': str,
            'password': str,
            'token': str
        }

        self.attribute_map = {
            'repo_url': 'repoURL',
            'user_name': 'userName',
            'password': 'password',
            'token': 'token'
        }
        self._repo_url = repo_url
        self._user_name = user_name
        self._password = password
        self._token = token

    @classmethod
    def from_dict(cls, dikt) -> 'ObjectRepoLocation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ObjectRepoLocation of this ObjectRepoLocation.  # noqa: E501
        :rtype: ObjectRepoLocation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def repo_url(self) -> Uri:
        """Gets the repo_url of this ObjectRepoLocation.


        :return: The repo_url of this ObjectRepoLocation.
        :rtype: Uri
        """
        return self._repo_url

    @repo_url.setter
    def repo_url(self, repo_url: Uri):
        """Sets the repo_url of this ObjectRepoLocation.


        :param repo_url: The repo_url of this ObjectRepoLocation.
        :type repo_url: Uri
        """

        self._repo_url = repo_url

    @property
    def user_name(self) -> str:
        """Gets the user_name of this ObjectRepoLocation.

        Username to access the repository  # noqa: E501

        :return: The user_name of this ObjectRepoLocation.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name: str):
        """Sets the user_name of this ObjectRepoLocation.

        Username to access the repository  # noqa: E501

        :param user_name: The user_name of this ObjectRepoLocation.
        :type user_name: str
        """

        self._user_name = user_name

    @property
    def password(self) -> str:
        """Gets the password of this ObjectRepoLocation.

        Password to access the repository  # noqa: E501

        :return: The password of this ObjectRepoLocation.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this ObjectRepoLocation.

        Password to access the repository  # noqa: E501

        :param password: The password of this ObjectRepoLocation.
        :type password: str
        """

        self._password = password

    @property
    def token(self) -> str:
        """Gets the token of this ObjectRepoLocation.

        Authorization token to access the repository  # noqa: E501

        :return: The token of this ObjectRepoLocation.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token: str):
        """Sets the token of this ObjectRepoLocation.

        Authorization token to access the repository  # noqa: E501

        :param token: The token of this ObjectRepoLocation.
        :type token: str
        """

        self._token = token
