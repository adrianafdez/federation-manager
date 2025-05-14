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


class CallbackCredentials(Model):
    def __init__(self, token_url: Uri=None, client_id: str=None, client_secret: str=None):  # noqa: E501
        """CallbackCredentials - a model defined in Swagger

        :param token_url: The token_url of this CallbackCredentials.  # noqa: E501
        :type token_url: Uri
        :param client_id: The client_id of this CallbackCredentials.  # noqa: E501
        :type client_id: str
        :param client_secret: The client_secret of this CallbackCredentials.  # noqa: E501
        :type client_secret: str
        """
        self.swagger_types = {
            'token_url': Uri,
            'client_id': str,
            'client_secret': str
        }

        self.attribute_map = {
            'token_url': 'tokenUrl',
            'client_id': 'clientId',
            'client_secret': 'clientSecret'
        }
        self._token_url = token_url
        self._client_id = client_id
        self._client_secret = client_secret

    @classmethod
    def from_dict(cls, dikt) -> 'CallbackCredentials':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CallbackCredentials of this CallbackCredentials.  # noqa: E501
        :rtype: CallbackCredentials
        """
        return util.deserialize_model(dikt, cls)

    @property
    def token_url(self) -> Uri:
        """Gets the token_url of this CallbackCredentials.


        :return: The token_url of this CallbackCredentials.
        :rtype: Uri
        """
        return self._token_url

    @token_url.setter
    def token_url(self, token_url: Uri):
        """Sets the token_url of this CallbackCredentials.


        :param token_url: The token_url of this CallbackCredentials.
        :type token_url: Uri
        """
        if token_url is None:
            raise ValueError("Invalid value for `token_url`, must not be `None`")  # noqa: E501

        self._token_url = token_url

    @property
    def client_id(self) -> str:
        """Gets the client_id of this CallbackCredentials.

        Client id for oauth2 client credentials flow.  # noqa: E501

        :return: The client_id of this CallbackCredentials.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id: str):
        """Sets the client_id of this CallbackCredentials.

        Client id for oauth2 client credentials flow.  # noqa: E501

        :param client_id: The client_id of this CallbackCredentials.
        :type client_id: str
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def client_secret(self) -> str:
        """Gets the client_secret of this CallbackCredentials.

        Client secret for oauth2 client credentials flow.  # noqa: E501

        :return: The client_secret of this CallbackCredentials.
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret: str):
        """Sets the client_secret of this CallbackCredentials.

        Client secret for oauth2 client credentials flow.  # noqa: E501

        :param client_secret: The client_secret of this CallbackCredentials.
        :type client_secret: str
        """
        if client_secret is None:
            raise ValueError("Invalid value for `client_secret`, must not be `None`")  # noqa: E501

        self._client_secret = client_secret
