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


class InvalidParam(Model):
    def __init__(self, param: str=None, reason: str=None):  # noqa: E501
        """InvalidParam - a model defined in Swagger

        :param param: The param of this InvalidParam.  # noqa: E501
        :type param: str
        :param reason: The reason of this InvalidParam.  # noqa: E501
        :type reason: str
        """
        self.swagger_types = {
            'param': str,
            'reason': str
        }

        self.attribute_map = {
            'param': 'param',
            'reason': 'reason'
        }
        self._param = param
        self._reason = reason

    @classmethod
    def from_dict(cls, dikt) -> 'InvalidParam':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InvalidParam of this InvalidParam.  # noqa: E501
        :rtype: InvalidParam
        """
        return util.deserialize_model(dikt, cls)

    @property
    def param(self) -> str:
        """Gets the param of this InvalidParam.


        :return: The param of this InvalidParam.
        :rtype: str
        """
        return self._param

    @param.setter
    def param(self, param: str):
        """Sets the param of this InvalidParam.


        :param param: The param of this InvalidParam.
        :type param: str
        """
        if param is None:
            raise ValueError("Invalid value for `param`, must not be `None`")  # noqa: E501

        self._param = param

    @property
    def reason(self) -> str:
        """Gets the reason of this InvalidParam.


        :return: The reason of this InvalidParam.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason: str):
        """Sets the reason of this InvalidParam.


        :param reason: The reason of this InvalidParam.
        :type reason: str
        """

        self._reason = reason
