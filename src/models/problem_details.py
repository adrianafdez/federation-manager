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
from models.invalid_param import InvalidParam  # noqa: F401,E501
import util


class ProblemDetails(Model):
    def __init__(self, title: str=None, detail: str=None, cause: str=None, invalid_params: List[InvalidParam]=None):  # noqa: E501
        """ProblemDetails - a model defined in Swagger

        :param title: The title of this ProblemDetails.  # noqa: E501
        :type title: str
        :param detail: The detail of this ProblemDetails.  # noqa: E501
        :type detail: str
        :param cause: The cause of this ProblemDetails.  # noqa: E501
        :type cause: str
        :param invalid_params: The invalid_params of this ProblemDetails.  # noqa: E501
        :type invalid_params: List[InvalidParam]
        """
        self.swagger_types = {
            'title': str,
            'detail': str,
            'cause': str,
            'invalid_params': List[InvalidParam]
        }

        self.attribute_map = {
            'title': 'title',
            'detail': 'detail',
            'cause': 'cause',
            'invalid_params': 'invalidParams'
        }
        self._title = title
        self._detail = detail
        self._cause = cause
        self._invalid_params = invalid_params

    @classmethod
    def from_dict(cls, dikt) -> 'ProblemDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ProblemDetails of this ProblemDetails.  # noqa: E501
        :rtype: ProblemDetails
        """
        return util.deserialize_model(dikt, cls)

    @property
    def title(self) -> str:
        """Gets the title of this ProblemDetails.


        :return: The title of this ProblemDetails.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this ProblemDetails.


        :param title: The title of this ProblemDetails.
        :type title: str
        """

        self._title = title

    @property
    def detail(self) -> str:
        """Gets the detail of this ProblemDetails.


        :return: The detail of this ProblemDetails.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail: str):
        """Sets the detail of this ProblemDetails.


        :param detail: The detail of this ProblemDetails.
        :type detail: str
        """

        self._detail = detail

    @property
    def cause(self) -> str:
        """Gets the cause of this ProblemDetails.


        :return: The cause of this ProblemDetails.
        :rtype: str
        """
        return self._cause

    @cause.setter
    def cause(self, cause: str):
        """Sets the cause of this ProblemDetails.


        :param cause: The cause of this ProblemDetails.
        :type cause: str
        """

        self._cause = cause

    @property
    def invalid_params(self) -> List[InvalidParam]:
        """Gets the invalid_params of this ProblemDetails.


        :return: The invalid_params of this ProblemDetails.
        :rtype: List[InvalidParam]
        """
        return self._invalid_params

    @invalid_params.setter
    def invalid_params(self, invalid_params: List[InvalidParam]):
        """Sets the invalid_params of this ProblemDetails.


        :param invalid_params: The invalid_params of this ProblemDetails.
        :type invalid_params: List[InvalidParam]
        """

        self._invalid_params = invalid_params
