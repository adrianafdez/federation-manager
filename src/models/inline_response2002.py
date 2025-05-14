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
from models.federation_context_id import FederationContextId  # noqa: F401,E501
import re  # noqa: F401,E501
import util


class InlineResponse2002(Model):
    def __init__(self, federation_context_id: FederationContextId=None):  # noqa: E501
        """InlineResponse2002 - a model defined in Swagger

        :param federation_context_id: The federation_context_id of this InlineResponse2002.  # noqa: E501
        :type federation_context_id: FederationContextId
        """
        self.swagger_types = {
            'federation_context_id': FederationContextId
        }

        self.attribute_map = {
            'federation_context_id': 'FederationContextId'
        }
        self._federation_context_id = federation_context_id

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2002':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_2 of this InlineResponse2002.  # noqa: E501
        :rtype: InlineResponse2002
        """
        return util.deserialize_model(dikt, cls)

    @property
    def federation_context_id(self) -> FederationContextId:
        """Gets the federation_context_id of this InlineResponse2002.


        :return: The federation_context_id of this InlineResponse2002.
        :rtype: FederationContextId
        """
        return self._federation_context_id

    @federation_context_id.setter
    def federation_context_id(self, federation_context_id: FederationContextId):
        """Sets the federation_context_id of this InlineResponse2002.


        :param federation_context_id: The federation_context_id of this InlineResponse2002.
        :type federation_context_id: FederationContextId
        """
        if federation_context_id is None:
            raise ValueError("Invalid value for `federation_context_id`, must not be `None`")  # noqa: E501

        self._federation_context_id = federation_context_id
