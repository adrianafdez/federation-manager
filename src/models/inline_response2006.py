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
from models.app_provider_id import AppProviderId  # noqa: F401,E501
from models.cpu_arch_type import CPUArchType  # noqa: F401,E501
from models.file_id import FileId  # noqa: F401,E501
from models.object_repo_location import ObjectRepoLocation  # noqa: F401,E501
from models.os_type import OSType  # noqa: F401,E501
from models.virt_image_type import VirtImageType  # noqa: F401,E501
import re  # noqa: F401,E501
import util


class InlineResponse2006(Model):
    def __init__(self, file_id: FileId=None, app_provider_id: AppProviderId=None, file_name: str=None, file_description: str=None, file_version_info: str=None, file_type: VirtImageType=None, checksum: str=None, img_os_type: OSType=None, img_ins_set_arch: CPUArchType=None, repo_type: str=None, file_repo_location: ObjectRepoLocation=None):  # noqa: E501
        """InlineResponse2006 - a model defined in Swagger

        :param file_id: The file_id of this InlineResponse2006.  # noqa: E501
        :type file_id: FileId
        :param app_provider_id: The app_provider_id of this InlineResponse2006.  # noqa: E501
        :type app_provider_id: AppProviderId
        :param file_name: The file_name of this InlineResponse2006.  # noqa: E501
        :type file_name: str
        :param file_description: The file_description of this InlineResponse2006.  # noqa: E501
        :type file_description: str
        :param file_version_info: The file_version_info of this InlineResponse2006.  # noqa: E501
        :type file_version_info: str
        :param file_type: The file_type of this InlineResponse2006.  # noqa: E501
        :type file_type: VirtImageType
        :param checksum: The checksum of this InlineResponse2006.  # noqa: E501
        :type checksum: str
        :param img_os_type: The img_os_type of this InlineResponse2006.  # noqa: E501
        :type img_os_type: OSType
        :param img_ins_set_arch: The img_ins_set_arch of this InlineResponse2006.  # noqa: E501
        :type img_ins_set_arch: CPUArchType
        :param repo_type: The repo_type of this InlineResponse2006.  # noqa: E501
        :type repo_type: str
        :param file_repo_location: The file_repo_location of this InlineResponse2006.  # noqa: E501
        :type file_repo_location: ObjectRepoLocation
        """
        self.swagger_types = {
            'file_id': FileId,
            'app_provider_id': AppProviderId,
            'file_name': str,
            'file_description': str,
            'file_version_info': str,
            'file_type': VirtImageType,
            'checksum': str,
            'img_os_type': OSType,
            'img_ins_set_arch': CPUArchType,
            'repo_type': str,
            'file_repo_location': ObjectRepoLocation
        }

        self.attribute_map = {
            'file_id': 'fileId',
            'app_provider_id': 'appProviderId',
            'file_name': 'fileName',
            'file_description': 'fileDescription',
            'file_version_info': 'fileVersionInfo',
            'file_type': 'fileType',
            'checksum': 'checksum',
            'img_os_type': 'imgOSType',
            'img_ins_set_arch': 'imgInsSetArch',
            'repo_type': 'repoType',
            'file_repo_location': 'fileRepoLocation'
        }
        self._file_id = file_id
        self._app_provider_id = app_provider_id
        self._file_name = file_name
        self._file_description = file_description
        self._file_version_info = file_version_info
        self._file_type = file_type
        self._checksum = checksum
        self._img_os_type = img_os_type
        self._img_ins_set_arch = img_ins_set_arch
        self._repo_type = repo_type
        self._file_repo_location = file_repo_location

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2006':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_6 of this InlineResponse2006.  # noqa: E501
        :rtype: InlineResponse2006
        """
        return util.deserialize_model(dikt, cls)

    @property
    def file_id(self) -> FileId:
        """Gets the file_id of this InlineResponse2006.


        :return: The file_id of this InlineResponse2006.
        :rtype: FileId
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id: FileId):
        """Sets the file_id of this InlineResponse2006.


        :param file_id: The file_id of this InlineResponse2006.
        :type file_id: FileId
        """
        if file_id is None:
            raise ValueError("Invalid value for `file_id`, must not be `None`")  # noqa: E501

        self._file_id = file_id

    @property
    def app_provider_id(self) -> AppProviderId:
        """Gets the app_provider_id of this InlineResponse2006.


        :return: The app_provider_id of this InlineResponse2006.
        :rtype: AppProviderId
        """
        return self._app_provider_id

    @app_provider_id.setter
    def app_provider_id(self, app_provider_id: AppProviderId):
        """Sets the app_provider_id of this InlineResponse2006.


        :param app_provider_id: The app_provider_id of this InlineResponse2006.
        :type app_provider_id: AppProviderId
        """
        if app_provider_id is None:
            raise ValueError("Invalid value for `app_provider_id`, must not be `None`")  # noqa: E501

        self._app_provider_id = app_provider_id

    @property
    def file_name(self) -> str:
        """Gets the file_name of this InlineResponse2006.

        Name of the image file.   App provides specifies this name when image is uploaded on originating OP over NBI.  # noqa: E501

        :return: The file_name of this InlineResponse2006.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name: str):
        """Sets the file_name of this InlineResponse2006.

        Name of the image file.   App provides specifies this name when image is uploaded on originating OP over NBI.  # noqa: E501

        :param file_name: The file_name of this InlineResponse2006.
        :type file_name: str
        """
        if file_name is None:
            raise ValueError("Invalid value for `file_name`, must not be `None`")  # noqa: E501

        self._file_name = file_name

    @property
    def file_description(self) -> str:
        """Gets the file_description of this InlineResponse2006.

        Brief description about the image file.  # noqa: E501

        :return: The file_description of this InlineResponse2006.
        :rtype: str
        """
        return self._file_description

    @file_description.setter
    def file_description(self, file_description: str):
        """Sets the file_description of this InlineResponse2006.

        Brief description about the image file.  # noqa: E501

        :param file_description: The file_description of this InlineResponse2006.
        :type file_description: str
        """

        self._file_description = file_description

    @property
    def file_version_info(self) -> str:
        """Gets the file_version_info of this InlineResponse2006.

        File version information  # noqa: E501

        :return: The file_version_info of this InlineResponse2006.
        :rtype: str
        """
        return self._file_version_info

    @file_version_info.setter
    def file_version_info(self, file_version_info: str):
        """Sets the file_version_info of this InlineResponse2006.

        File version information  # noqa: E501

        :param file_version_info: The file_version_info of this InlineResponse2006.
        :type file_version_info: str
        """
        if file_version_info is None:
            raise ValueError("Invalid value for `file_version_info`, must not be `None`")  # noqa: E501

        self._file_version_info = file_version_info

    @property
    def file_type(self) -> VirtImageType:
        """Gets the file_type of this InlineResponse2006.


        :return: The file_type of this InlineResponse2006.
        :rtype: VirtImageType
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type: VirtImageType):
        """Sets the file_type of this InlineResponse2006.


        :param file_type: The file_type of this InlineResponse2006.
        :type file_type: VirtImageType
        """
        if file_type is None:
            raise ValueError("Invalid value for `file_type`, must not be `None`")  # noqa: E501

        self._file_type = file_type

    @property
    def checksum(self) -> str:
        """Gets the checksum of this InlineResponse2006.

        MD5 checksum for VM and file-based images, sha256 digest for containers  # noqa: E501

        :return: The checksum of this InlineResponse2006.
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum: str):
        """Sets the checksum of this InlineResponse2006.

        MD5 checksum for VM and file-based images, sha256 digest for containers  # noqa: E501

        :param checksum: The checksum of this InlineResponse2006.
        :type checksum: str
        """

        self._checksum = checksum

    @property
    def img_os_type(self) -> OSType:
        """Gets the img_os_type of this InlineResponse2006.


        :return: The img_os_type of this InlineResponse2006.
        :rtype: OSType
        """
        return self._img_os_type

    @img_os_type.setter
    def img_os_type(self, img_os_type: OSType):
        """Sets the img_os_type of this InlineResponse2006.


        :param img_os_type: The img_os_type of this InlineResponse2006.
        :type img_os_type: OSType
        """
        if img_os_type is None:
            raise ValueError("Invalid value for `img_os_type`, must not be `None`")  # noqa: E501

        self._img_os_type = img_os_type

    @property
    def img_ins_set_arch(self) -> CPUArchType:
        """Gets the img_ins_set_arch of this InlineResponse2006.


        :return: The img_ins_set_arch of this InlineResponse2006.
        :rtype: CPUArchType
        """
        return self._img_ins_set_arch

    @img_ins_set_arch.setter
    def img_ins_set_arch(self, img_ins_set_arch: CPUArchType):
        """Sets the img_ins_set_arch of this InlineResponse2006.


        :param img_ins_set_arch: The img_ins_set_arch of this InlineResponse2006.
        :type img_ins_set_arch: CPUArchType
        """
        if img_ins_set_arch is None:
            raise ValueError("Invalid value for `img_ins_set_arch`, must not be `None`")  # noqa: E501

        self._img_ins_set_arch = img_ins_set_arch

    @property
    def repo_type(self) -> str:
        """Gets the repo_type of this InlineResponse2006.

        Artefact or file repository location. PUBLICREPO is used of public URLs like GitHub, Helm repo, docker registry etc., PRIVATEREPO is used for private repo managed by the application developer, UPLOAD is for the case when artefact/file is uploaded from MEC web portal.  OP should pull the image from ‘repoUrl' immediately after receiving the request and then send back the response. In case the repoURL corresponds to a docker registry, use docker v2 http api to do the pull.  # noqa: E501

        :return: The repo_type of this InlineResponse2006.
        :rtype: str
        """
        return self._repo_type

    @repo_type.setter
    def repo_type(self, repo_type: str):
        """Sets the repo_type of this InlineResponse2006.

        Artefact or file repository location. PUBLICREPO is used of public URLs like GitHub, Helm repo, docker registry etc., PRIVATEREPO is used for private repo managed by the application developer, UPLOAD is for the case when artefact/file is uploaded from MEC web portal.  OP should pull the image from ‘repoUrl' immediately after receiving the request and then send back the response. In case the repoURL corresponds to a docker registry, use docker v2 http api to do the pull.  # noqa: E501

        :param repo_type: The repo_type of this InlineResponse2006.
        :type repo_type: str
        """
        allowed_values = ["PRIVATEREPO", "PUBLICREPO", "UPLOAD"]  # noqa: E501
        if repo_type not in allowed_values:
            raise ValueError(
                "Invalid value for `repo_type` ({0}), must be one of {1}"
                .format(repo_type, allowed_values)
            )

        self._repo_type = repo_type

    @property
    def file_repo_location(self) -> ObjectRepoLocation:
        """Gets the file_repo_location of this InlineResponse2006.


        :return: The file_repo_location of this InlineResponse2006.
        :rtype: ObjectRepoLocation
        """
        return self._file_repo_location

    @file_repo_location.setter
    def file_repo_location(self, file_repo_location: ObjectRepoLocation):
        """Sets the file_repo_location of this InlineResponse2006.


        :param file_repo_location: The file_repo_location of this InlineResponse2006.
        :type file_repo_location: ObjectRepoLocation
        """

        self._file_repo_location = file_repo_location
