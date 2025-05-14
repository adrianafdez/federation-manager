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


class DeploymentConfig(Model):
    def __init__(self, config_type: str=None, contents: str=None):  # noqa: E501
        """DeploymentConfig - a model defined in Swagger

        :param config_type: The config_type of this DeploymentConfig.  # noqa: E501
        :type config_type: str
        :param contents: The contents of this DeploymentConfig.  # noqa: E501
        :type contents: str
        """
        self.swagger_types = {
            'config_type': str,
            'contents': str
        }

        self.attribute_map = {
            'config_type': 'configType',
            'contents': 'contents'
        }
        self._config_type = config_type
        self._contents = contents

    @classmethod
    def from_dict(cls, dikt) -> 'DeploymentConfig':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DeploymentConfig of this DeploymentConfig.  # noqa: E501
        :rtype: DeploymentConfig
        """
        return util.deserialize_model(dikt, cls)

    @property
    def config_type(self) -> str:
        """Gets the config_type of this DeploymentConfig.

        Config type.  # noqa: E501

        :return: The config_type of this DeploymentConfig.
        :rtype: str
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type: str):
        """Sets the config_type of this DeploymentConfig.

        Config type.  # noqa: E501

        :param config_type: The config_type of this DeploymentConfig.
        :type config_type: str
        """
        allowed_values = ["DOCKER_COMPOSE", "KUBERNETES_MANIFEST", "CLOUD_INIT", "HELM_VALUES"]  # noqa: E501
        if config_type not in allowed_values:
            raise ValueError(
                "Invalid value for `config_type` ({0}), must be one of {1}"
                .format(config_type, allowed_values)
            )

        self._config_type = config_type

    @property
    def contents(self) -> str:
        """Gets the contents of this DeploymentConfig.

        Contents of the configuration.  # noqa: E501

        :return: The contents of this DeploymentConfig.
        :rtype: str
        """
        return self._contents

    @contents.setter
    def contents(self, contents: str):
        """Sets the contents of this DeploymentConfig.

        Contents of the configuration.  # noqa: E501

        :param contents: The contents of this DeploymentConfig.
        :type contents: str
        """
        if contents is None:
            raise ValueError("Invalid value for `contents`, must not be `None`")  # noqa: E501

        self._contents = contents
