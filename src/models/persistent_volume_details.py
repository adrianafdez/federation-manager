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


class PersistentVolumeDetails(Model):
    def __init__(self, volume_size: str=None, volume_mount_path: str=None, volume_name: str=None, ephemeral_type: bool=False, access_mode: str='RW', sharing_policy: str='EXCLUSIVE'):  # noqa: E501
        """PersistentVolumeDetails - a model defined in Swagger

        :param volume_size: The volume_size of this PersistentVolumeDetails.  # noqa: E501
        :type volume_size: str
        :param volume_mount_path: The volume_mount_path of this PersistentVolumeDetails.  # noqa: E501
        :type volume_mount_path: str
        :param volume_name: The volume_name of this PersistentVolumeDetails.  # noqa: E501
        :type volume_name: str
        :param ephemeral_type: The ephemeral_type of this PersistentVolumeDetails.  # noqa: E501
        :type ephemeral_type: bool
        :param access_mode: The access_mode of this PersistentVolumeDetails.  # noqa: E501
        :type access_mode: str
        :param sharing_policy: The sharing_policy of this PersistentVolumeDetails.  # noqa: E501
        :type sharing_policy: str
        """
        self.swagger_types = {
            'volume_size': str,
            'volume_mount_path': str,
            'volume_name': str,
            'ephemeral_type': bool,
            'access_mode': str,
            'sharing_policy': str
        }

        self.attribute_map = {
            'volume_size': 'volumeSize',
            'volume_mount_path': 'volumeMountPath',
            'volume_name': 'volumeName',
            'ephemeral_type': 'ephemeralType',
            'access_mode': 'accessMode',
            'sharing_policy': 'sharingPolicy'
        }
        self._volume_size = volume_size
        self._volume_mount_path = volume_mount_path
        self._volume_name = volume_name
        self._ephemeral_type = ephemeral_type
        self._access_mode = access_mode
        self._sharing_policy = sharing_policy

    @classmethod
    def from_dict(cls, dikt) -> 'PersistentVolumeDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PersistentVolumeDetails of this PersistentVolumeDetails.  # noqa: E501
        :rtype: PersistentVolumeDetails
        """
        return util.deserialize_model(dikt, cls)

    @property
    def volume_size(self) -> str:
        """Gets the volume_size of this PersistentVolumeDetails.

        size of the volume given by user (10GB, 20GB, 50 GB or 100GB)  # noqa: E501

        :return: The volume_size of this PersistentVolumeDetails.
        :rtype: str
        """
        return self._volume_size

    @volume_size.setter
    def volume_size(self, volume_size: str):
        """Sets the volume_size of this PersistentVolumeDetails.

        size of the volume given by user (10GB, 20GB, 50 GB or 100GB)  # noqa: E501

        :param volume_size: The volume_size of this PersistentVolumeDetails.
        :type volume_size: str
        """
        allowed_values = ["10Gi", "20Gi", "50Gi", "100Gi"]  # noqa: E501
        if volume_size not in allowed_values:
            raise ValueError(
                "Invalid value for `volume_size` ({0}), must be one of {1}"
                .format(volume_size, allowed_values)
            )

        self._volume_size = volume_size

    @property
    def volume_mount_path(self) -> str:
        """Gets the volume_mount_path of this PersistentVolumeDetails.

        Defines the mount path of the volume  # noqa: E501

        :return: The volume_mount_path of this PersistentVolumeDetails.
        :rtype: str
        """
        return self._volume_mount_path

    @volume_mount_path.setter
    def volume_mount_path(self, volume_mount_path: str):
        """Sets the volume_mount_path of this PersistentVolumeDetails.

        Defines the mount path of the volume  # noqa: E501

        :param volume_mount_path: The volume_mount_path of this PersistentVolumeDetails.
        :type volume_mount_path: str
        """
        if volume_mount_path is None:
            raise ValueError("Invalid value for `volume_mount_path`, must not be `None`")  # noqa: E501

        self._volume_mount_path = volume_mount_path

    @property
    def volume_name(self) -> str:
        """Gets the volume_name of this PersistentVolumeDetails.

        Human readable name for the volume  # noqa: E501

        :return: The volume_name of this PersistentVolumeDetails.
        :rtype: str
        """
        return self._volume_name

    @volume_name.setter
    def volume_name(self, volume_name: str):
        """Sets the volume_name of this PersistentVolumeDetails.

        Human readable name for the volume  # noqa: E501

        :param volume_name: The volume_name of this PersistentVolumeDetails.
        :type volume_name: str
        """
        if volume_name is None:
            raise ValueError("Invalid value for `volume_name`, must not be `None`")  # noqa: E501

        self._volume_name = volume_name

    @property
    def ephemeral_type(self) -> bool:
        """Gets the ephemeral_type of this PersistentVolumeDetails.

        It indicates the ephemeral storage on the node and contents are not preserved if containers restarts  # noqa: E501

        :return: The ephemeral_type of this PersistentVolumeDetails.
        :rtype: bool
        """
        return self._ephemeral_type

    @ephemeral_type.setter
    def ephemeral_type(self, ephemeral_type: bool):
        """Sets the ephemeral_type of this PersistentVolumeDetails.

        It indicates the ephemeral storage on the node and contents are not preserved if containers restarts  # noqa: E501

        :param ephemeral_type: The ephemeral_type of this PersistentVolumeDetails.
        :type ephemeral_type: bool
        """

        self._ephemeral_type = ephemeral_type

    @property
    def access_mode(self) -> str:
        """Gets the access_mode of this PersistentVolumeDetails.

        Values are RW (read/write) and RO (read-only)l  # noqa: E501

        :return: The access_mode of this PersistentVolumeDetails.
        :rtype: str
        """
        return self._access_mode

    @access_mode.setter
    def access_mode(self, access_mode: str):
        """Sets the access_mode of this PersistentVolumeDetails.

        Values are RW (read/write) and RO (read-only)l  # noqa: E501

        :param access_mode: The access_mode of this PersistentVolumeDetails.
        :type access_mode: str
        """
        allowed_values = ["RW", "RO"]  # noqa: E501
        if access_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `access_mode` ({0}), must be one of {1}"
                .format(access_mode, allowed_values)
            )

        self._access_mode = access_mode

    @property
    def sharing_policy(self) -> str:
        """Gets the sharing_policy of this PersistentVolumeDetails.

        Exclusive or Shared. If shared, then in case of multiple containers same volume will be shared across the containers.  # noqa: E501

        :return: The sharing_policy of this PersistentVolumeDetails.
        :rtype: str
        """
        return self._sharing_policy

    @sharing_policy.setter
    def sharing_policy(self, sharing_policy: str):
        """Sets the sharing_policy of this PersistentVolumeDetails.

        Exclusive or Shared. If shared, then in case of multiple containers same volume will be shared across the containers.  # noqa: E501

        :param sharing_policy: The sharing_policy of this PersistentVolumeDetails.
        :type sharing_policy: str
        """
        allowed_values = ["EXCLUSIVE", "SHARED"]  # noqa: E501
        if sharing_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `sharing_policy` ({0}), must be one of {1}"
                .format(sharing_policy, allowed_values)
            )

        self._sharing_policy = sharing_policy
