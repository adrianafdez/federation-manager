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
from models.artefact_id import ArtefactId  # noqa: F401,E501
from models.object_repo_location import ObjectRepoLocation  # noqa: F401,E501
import re  # noqa: F401,E501
import util


class InlineResponse2005(Model):
    def __init__(self, artefact_id: ArtefactId=None, app_provider_id: AppProviderId=None, artefact_name: str=None, artefact_description: str=None, artefact_version_info: str=None, artefact_virt_type: str=None, artefact_file_name: str=None, artefact_file_format: str=None, artefact_descriptor_type: str=None, repo_type: str=None, artefact_repo_location: ObjectRepoLocation=None):  # noqa: E501
        """InlineResponse2005 - a model defined in Swagger

        :param artefact_id: The artefact_id of this InlineResponse2005.  # noqa: E501
        :type artefact_id: ArtefactId
        :param app_provider_id: The app_provider_id of this InlineResponse2005.  # noqa: E501
        :type app_provider_id: AppProviderId
        :param artefact_name: The artefact_name of this InlineResponse2005.  # noqa: E501
        :type artefact_name: str
        :param artefact_description: The artefact_description of this InlineResponse2005.  # noqa: E501
        :type artefact_description: str
        :param artefact_version_info: The artefact_version_info of this InlineResponse2005.  # noqa: E501
        :type artefact_version_info: str
        :param artefact_virt_type: The artefact_virt_type of this InlineResponse2005.  # noqa: E501
        :type artefact_virt_type: str
        :param artefact_file_name: The artefact_file_name of this InlineResponse2005.  # noqa: E501
        :type artefact_file_name: str
        :param artefact_file_format: The artefact_file_format of this InlineResponse2005.  # noqa: E501
        :type artefact_file_format: str
        :param artefact_descriptor_type: The artefact_descriptor_type of this InlineResponse2005.  # noqa: E501
        :type artefact_descriptor_type: str
        :param repo_type: The repo_type of this InlineResponse2005.  # noqa: E501
        :type repo_type: str
        :param artefact_repo_location: The artefact_repo_location of this InlineResponse2005.  # noqa: E501
        :type artefact_repo_location: ObjectRepoLocation
        """
        self.swagger_types = {
            'artefact_id': ArtefactId,
            'app_provider_id': AppProviderId,
            'artefact_name': str,
            'artefact_description': str,
            'artefact_version_info': str,
            'artefact_virt_type': str,
            'artefact_file_name': str,
            'artefact_file_format': str,
            'artefact_descriptor_type': str,
            'repo_type': str,
            'artefact_repo_location': ObjectRepoLocation
        }

        self.attribute_map = {
            'artefact_id': 'artefactId',
            'app_provider_id': 'appProviderId',
            'artefact_name': 'artefactName',
            'artefact_description': 'artefactDescription',
            'artefact_version_info': 'artefactVersionInfo',
            'artefact_virt_type': 'artefactVirtType',
            'artefact_file_name': 'artefactFileName',
            'artefact_file_format': 'artefactFileFormat',
            'artefact_descriptor_type': 'artefactDescriptorType',
            'repo_type': 'repoType',
            'artefact_repo_location': 'artefactRepoLocation'
        }
        self._artefact_id = artefact_id
        self._app_provider_id = app_provider_id
        self._artefact_name = artefact_name
        self._artefact_description = artefact_description
        self._artefact_version_info = artefact_version_info
        self._artefact_virt_type = artefact_virt_type
        self._artefact_file_name = artefact_file_name
        self._artefact_file_format = artefact_file_format
        self._artefact_descriptor_type = artefact_descriptor_type
        self._repo_type = repo_type
        self._artefact_repo_location = artefact_repo_location

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2005':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_5 of this InlineResponse2005.  # noqa: E501
        :rtype: InlineResponse2005
        """
        return util.deserialize_model(dikt, cls)

    @property
    def artefact_id(self) -> ArtefactId:
        """Gets the artefact_id of this InlineResponse2005.


        :return: The artefact_id of this InlineResponse2005.
        :rtype: ArtefactId
        """
        return self._artefact_id

    @artefact_id.setter
    def artefact_id(self, artefact_id: ArtefactId):
        """Sets the artefact_id of this InlineResponse2005.


        :param artefact_id: The artefact_id of this InlineResponse2005.
        :type artefact_id: ArtefactId
        """
        if artefact_id is None:
            raise ValueError("Invalid value for `artefact_id`, must not be `None`")  # noqa: E501

        self._artefact_id = artefact_id

    @property
    def app_provider_id(self) -> AppProviderId:
        """Gets the app_provider_id of this InlineResponse2005.


        :return: The app_provider_id of this InlineResponse2005.
        :rtype: AppProviderId
        """
        return self._app_provider_id

    @app_provider_id.setter
    def app_provider_id(self, app_provider_id: AppProviderId):
        """Sets the app_provider_id of this InlineResponse2005.


        :param app_provider_id: The app_provider_id of this InlineResponse2005.
        :type app_provider_id: AppProviderId
        """
        if app_provider_id is None:
            raise ValueError("Invalid value for `app_provider_id`, must not be `None`")  # noqa: E501

        self._app_provider_id = app_provider_id

    @property
    def artefact_name(self) -> str:
        """Gets the artefact_name of this InlineResponse2005.

        Name of the artefact.  # noqa: E501

        :return: The artefact_name of this InlineResponse2005.
        :rtype: str
        """
        return self._artefact_name

    @artefact_name.setter
    def artefact_name(self, artefact_name: str):
        """Sets the artefact_name of this InlineResponse2005.

        Name of the artefact.  # noqa: E501

        :param artefact_name: The artefact_name of this InlineResponse2005.
        :type artefact_name: str
        """
        if artefact_name is None:
            raise ValueError("Invalid value for `artefact_name`, must not be `None`")  # noqa: E501

        self._artefact_name = artefact_name

    @property
    def artefact_description(self) -> str:
        """Gets the artefact_description of this InlineResponse2005.

        Brief description of the artefact by the application provider  # noqa: E501

        :return: The artefact_description of this InlineResponse2005.
        :rtype: str
        """
        return self._artefact_description

    @artefact_description.setter
    def artefact_description(self, artefact_description: str):
        """Sets the artefact_description of this InlineResponse2005.

        Brief description of the artefact by the application provider  # noqa: E501

        :param artefact_description: The artefact_description of this InlineResponse2005.
        :type artefact_description: str
        """

        self._artefact_description = artefact_description

    @property
    def artefact_version_info(self) -> str:
        """Gets the artefact_version_info of this InlineResponse2005.

        Artefact version information  # noqa: E501

        :return: The artefact_version_info of this InlineResponse2005.
        :rtype: str
        """
        return self._artefact_version_info

    @artefact_version_info.setter
    def artefact_version_info(self, artefact_version_info: str):
        """Sets the artefact_version_info of this InlineResponse2005.

        Artefact version information  # noqa: E501

        :param artefact_version_info: The artefact_version_info of this InlineResponse2005.
        :type artefact_version_info: str
        """
        if artefact_version_info is None:
            raise ValueError("Invalid value for `artefact_version_info`, must not be `None`")  # noqa: E501

        self._artefact_version_info = artefact_version_info

    @property
    def artefact_virt_type(self) -> str:
        """Gets the artefact_virt_type of this InlineResponse2005.


        :return: The artefact_virt_type of this InlineResponse2005.
        :rtype: str
        """
        return self._artefact_virt_type

    @artefact_virt_type.setter
    def artefact_virt_type(self, artefact_virt_type: str):
        """Sets the artefact_virt_type of this InlineResponse2005.


        :param artefact_virt_type: The artefact_virt_type of this InlineResponse2005.
        :type artefact_virt_type: str
        """
        allowed_values = ["VM_TYPE", "CONTAINER_TYPE"]  # noqa: E501
        if artefact_virt_type not in allowed_values:
            raise ValueError(
                "Invalid value for `artefact_virt_type` ({0}), must be one of {1}"
                .format(artefact_virt_type, allowed_values)
            )

        self._artefact_virt_type = artefact_virt_type

    @property
    def artefact_file_name(self) -> str:
        """Gets the artefact_file_name of this InlineResponse2005.

        Name of the file.  # noqa: E501

        :return: The artefact_file_name of this InlineResponse2005.
        :rtype: str
        """
        return self._artefact_file_name

    @artefact_file_name.setter
    def artefact_file_name(self, artefact_file_name: str):
        """Sets the artefact_file_name of this InlineResponse2005.

        Name of the file.  # noqa: E501

        :param artefact_file_name: The artefact_file_name of this InlineResponse2005.
        :type artefact_file_name: str
        """

        self._artefact_file_name = artefact_file_name

    @property
    def artefact_file_format(self) -> str:
        """Gets the artefact_file_format of this InlineResponse2005.

        Artefacts like Helm charts or Terraform scripts may need compressed format.  # noqa: E501

        :return: The artefact_file_format of this InlineResponse2005.
        :rtype: str
        """
        return self._artefact_file_format

    @artefact_file_format.setter
    def artefact_file_format(self, artefact_file_format: str):
        """Sets the artefact_file_format of this InlineResponse2005.

        Artefacts like Helm charts or Terraform scripts may need compressed format.  # noqa: E501

        :param artefact_file_format: The artefact_file_format of this InlineResponse2005.
        :type artefact_file_format: str
        """
        allowed_values = ["WINZIP", "TAR", "TEXT", "TARGZ"]  # noqa: E501
        if artefact_file_format not in allowed_values:
            raise ValueError(
                "Invalid value for `artefact_file_format` ({0}), must be one of {1}"
                .format(artefact_file_format, allowed_values)
            )

        self._artefact_file_format = artefact_file_format

    @property
    def artefact_descriptor_type(self) -> str:
        """Gets the artefact_descriptor_type of this InlineResponse2005.

        Type of descriptor present in the artefact.  App provider can either define either a Helm chart or a Terraform script or container spec.  # noqa: E501

        :return: The artefact_descriptor_type of this InlineResponse2005.
        :rtype: str
        """
        return self._artefact_descriptor_type

    @artefact_descriptor_type.setter
    def artefact_descriptor_type(self, artefact_descriptor_type: str):
        """Sets the artefact_descriptor_type of this InlineResponse2005.

        Type of descriptor present in the artefact.  App provider can either define either a Helm chart or a Terraform script or container spec.  # noqa: E501

        :param artefact_descriptor_type: The artefact_descriptor_type of this InlineResponse2005.
        :type artefact_descriptor_type: str
        """
        allowed_values = ["HELM", "TERRAFORM", "ANSIBLE", "SHELL", "COMPONENTSPEC"]  # noqa: E501
        if artefact_descriptor_type not in allowed_values:
            raise ValueError(
                "Invalid value for `artefact_descriptor_type` ({0}), must be one of {1}"
                .format(artefact_descriptor_type, allowed_values)
            )

        self._artefact_descriptor_type = artefact_descriptor_type

    @property
    def repo_type(self) -> str:
        """Gets the repo_type of this InlineResponse2005.

        Artefact or file repository location. PUBLICREPO is used of public URLs like GitHub, Helm repo, docker registry etc., PRIVATEREPO is used for private repo managed by the application developer, UPLOAD is for the case when artefact/file is uploaded from MEC web portal.  OP should pull the image from ‘repoUrl' immediately after receiving the request and then send back the response. In case the repoURL corresponds to a docker registry, use docker v2 http api to do the pull.  # noqa: E501

        :return: The repo_type of this InlineResponse2005.
        :rtype: str
        """
        return self._repo_type

    @repo_type.setter
    def repo_type(self, repo_type: str):
        """Sets the repo_type of this InlineResponse2005.

        Artefact or file repository location. PUBLICREPO is used of public URLs like GitHub, Helm repo, docker registry etc., PRIVATEREPO is used for private repo managed by the application developer, UPLOAD is for the case when artefact/file is uploaded from MEC web portal.  OP should pull the image from ‘repoUrl' immediately after receiving the request and then send back the response. In case the repoURL corresponds to a docker registry, use docker v2 http api to do the pull.  # noqa: E501

        :param repo_type: The repo_type of this InlineResponse2005.
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
    def artefact_repo_location(self) -> ObjectRepoLocation:
        """Gets the artefact_repo_location of this InlineResponse2005.


        :return: The artefact_repo_location of this InlineResponse2005.
        :rtype: ObjectRepoLocation
        """
        return self._artefact_repo_location

    @artefact_repo_location.setter
    def artefact_repo_location(self, artefact_repo_location: ObjectRepoLocation):
        """Sets the artefact_repo_location of this InlineResponse2005.


        :param artefact_repo_location: The artefact_repo_location of this InlineResponse2005.
        :type artefact_repo_location: ObjectRepoLocation
        """

        self._artefact_repo_location = artefact_repo_location
