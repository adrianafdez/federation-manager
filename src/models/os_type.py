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


class OSType(Model):
    def __init__(self, architecture: str=None, distribution: str=None, version: str=None, license: str=None):  # noqa: E501
        """OSType - a model defined in Swagger

        :param architecture: The architecture of this OSType.  # noqa: E501
        :type architecture: str
        :param distribution: The distribution of this OSType.  # noqa: E501
        :type distribution: str
        :param version: The version of this OSType.  # noqa: E501
        :type version: str
        :param license: The license of this OSType.  # noqa: E501
        :type license: str
        """
        self.swagger_types = {
            'architecture': str,
            'distribution': str,
            'version': str,
            'license': str
        }

        self.attribute_map = {
            'architecture': 'architecture',
            'distribution': 'distribution',
            'version': 'version',
            'license': 'license'
        }
        self._architecture = architecture
        self._distribution = distribution
        self._version = version
        self._license = license

    @classmethod
    def from_dict(cls, dikt) -> 'OSType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OSType of this OSType.  # noqa: E501
        :rtype: OSType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def architecture(self) -> str:
        """Gets the architecture of this OSType.


        :return: The architecture of this OSType.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture: str):
        """Sets the architecture of this OSType.


        :param architecture: The architecture of this OSType.
        :type architecture: str
        """
        allowed_values = ["x86_64", "x86"]  # noqa: E501
        if architecture not in allowed_values:
            raise ValueError(
                "Invalid value for `architecture` ({0}), must be one of {1}"
                .format(architecture, allowed_values)
            )

        self._architecture = architecture

    @property
    def distribution(self) -> str:
        """Gets the distribution of this OSType.


        :return: The distribution of this OSType.
        :rtype: str
        """
        return self._distribution

    @distribution.setter
    def distribution(self, distribution: str):
        """Sets the distribution of this OSType.


        :param distribution: The distribution of this OSType.
        :type distribution: str
        """
        allowed_values = ["RHEL", "UBUNTU", "COREOS", "FEDORA", "WINDOWS", "OTHER"]  # noqa: E501
        if distribution not in allowed_values:
            raise ValueError(
                "Invalid value for `distribution` ({0}), must be one of {1}"
                .format(distribution, allowed_values)
            )

        self._distribution = distribution

    @property
    def version(self) -> str:
        """Gets the version of this OSType.


        :return: The version of this OSType.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str):
        """Sets the version of this OSType.


        :param version: The version of this OSType.
        :type version: str
        """
        allowed_values = ["OS_VERSION_UBUNTU_2204_LTS", "OS_VERSION_RHEL_8", "OS_VERSION_RHEL_7", "OS_VERSION_DEBIAN_11", "OS_VERSION_COREOS_STABLE", "OS_MS_WINDOWS_2012_R2", "OTHER"]  # noqa: E501
        if version not in allowed_values:
            raise ValueError(
                "Invalid value for `version` ({0}), must be one of {1}"
                .format(version, allowed_values)
            )

        self._version = version

    @property
    def license(self) -> str:
        """Gets the license of this OSType.


        :return: The license of this OSType.
        :rtype: str
        """
        return self._license

    @license.setter
    def license(self, license: str):
        """Sets the license of this OSType.


        :param license: The license of this OSType.
        :type license: str
        """
        allowed_values = ["OS_LICENSE_TYPE_FREE", "OS_LICENSE_TYPE_ON_DEMAND", "NOT_SPECIFIED"]  # noqa: E501
        if license not in allowed_values:
            raise ValueError(
                "Invalid value for `license` ({0}), must be one of {1}"
                .format(license, allowed_values)
            )

        self._license = license
