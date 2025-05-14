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


class CompEnvParams(Model):
    def __init__(self, env_var_name: str=None, env_value_type: str=None, env_var_value: str=None, env_var_src: str=None):  # noqa: E501
        """CompEnvParams - a model defined in Swagger

        :param env_var_name: The env_var_name of this CompEnvParams.  # noqa: E501
        :type env_var_name: str
        :param env_value_type: The env_value_type of this CompEnvParams.  # noqa: E501
        :type env_value_type: str
        :param env_var_value: The env_var_value of this CompEnvParams.  # noqa: E501
        :type env_var_value: str
        :param env_var_src: The env_var_src of this CompEnvParams.  # noqa: E501
        :type env_var_src: str
        """
        self.swagger_types = {
            'env_var_name': str,
            'env_value_type': str,
            'env_var_value': str,
            'env_var_src': str
        }

        self.attribute_map = {
            'env_var_name': 'envVarName',
            'env_value_type': 'envValueType',
            'env_var_value': 'envVarValue',
            'env_var_src': 'envVarSrc'
        }
        self._env_var_name = env_var_name
        self._env_value_type = env_value_type
        self._env_var_value = env_var_value
        self._env_var_src = env_var_src

    @classmethod
    def from_dict(cls, dikt) -> 'CompEnvParams':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CompEnvParams of this CompEnvParams.  # noqa: E501
        :rtype: CompEnvParams
        """
        return util.deserialize_model(dikt, cls)

    @property
    def env_var_name(self) -> str:
        """Gets the env_var_name of this CompEnvParams.

        Name of environment variable  # noqa: E501

        :return: The env_var_name of this CompEnvParams.
        :rtype: str
        """
        return self._env_var_name

    @env_var_name.setter
    def env_var_name(self, env_var_name: str):
        """Sets the env_var_name of this CompEnvParams.

        Name of environment variable  # noqa: E501

        :param env_var_name: The env_var_name of this CompEnvParams.
        :type env_var_name: str
        """
        if env_var_name is None:
            raise ValueError("Invalid value for `env_var_name`, must not be `None`")  # noqa: E501

        self._env_var_name = env_var_name

    @property
    def env_value_type(self) -> str:
        """Gets the env_value_type of this CompEnvParams.


        :return: The env_value_type of this CompEnvParams.
        :rtype: str
        """
        return self._env_value_type

    @env_value_type.setter
    def env_value_type(self, env_value_type: str):
        """Sets the env_value_type of this CompEnvParams.


        :param env_value_type: The env_value_type of this CompEnvParams.
        :type env_value_type: str
        """
        allowed_values = ["USER_DEFINED", "PLATFORM_DEFINED_DYNAMIC_PORT", "PLATFORM_DEFINED_DNS", "PLATFORM_DEFINED_IP"]  # noqa: E501
        if env_value_type not in allowed_values:
            raise ValueError(
                "Invalid value for `env_value_type` ({0}), must be one of {1}"
                .format(env_value_type, allowed_values)
            )

        self._env_value_type = env_value_type

    @property
    def env_var_value(self) -> str:
        """Gets the env_var_value of this CompEnvParams.

        Value to be assigned to environment variable  # noqa: E501

        :return: The env_var_value of this CompEnvParams.
        :rtype: str
        """
        return self._env_var_value

    @env_var_value.setter
    def env_var_value(self, env_var_value: str):
        """Sets the env_var_value of this CompEnvParams.

        Value to be assigned to environment variable  # noqa: E501

        :param env_var_value: The env_var_value of this CompEnvParams.
        :type env_var_value: str
        """

        self._env_var_value = env_var_value

    @property
    def env_var_src(self) -> str:
        """Gets the env_var_src of this CompEnvParams.

        Full path of parameter from componentSpec that should be used to generate the environment value. Eg. networkResourceProfile[1]. interfaceId.  # noqa: E501

        :return: The env_var_src of this CompEnvParams.
        :rtype: str
        """
        return self._env_var_src

    @env_var_src.setter
    def env_var_src(self, env_var_src: str):
        """Sets the env_var_src of this CompEnvParams.

        Full path of parameter from componentSpec that should be used to generate the environment value. Eg. networkResourceProfile[1]. interfaceId.  # noqa: E501

        :param env_var_src: The env_var_src of this CompEnvParams.
        :type env_var_src: str
        """

        self._env_var_src = env_var_src
