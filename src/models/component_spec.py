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
from models.command_line_params import CommandLineParams  # noqa: F401,E501
from models.comp_env_params import CompEnvParams  # noqa: F401,E501
from models.compute_resource_info import ComputeResourceInfo  # noqa: F401,E501
from models.deployment_config import DeploymentConfig  # noqa: F401,E501
from models.file_id import FileId  # noqa: F401,E501
from models.interface_details import InterfaceDetails  # noqa: F401,E501
from models.persistent_volume_details import PersistentVolumeDetails  # noqa: F401,E501
import re  # noqa: F401,E501
import util


class ComponentSpec(Model):
    def __init__(self, component_name: str=None, images: List[FileId]=None, num_of_instances: int=None, restart_policy: str=None, command_line_params: CommandLineParams=None, exposed_interfaces: List[InterfaceDetails]=None, compute_resource_profile: ComputeResourceInfo=None, comp_env_params: List[CompEnvParams]=None, deployment_config: DeploymentConfig=None, persistent_volumes: List[PersistentVolumeDetails]=None):  # noqa: E501
        """ComponentSpec - a model defined in Swagger

        :param component_name: The component_name of this ComponentSpec.  # noqa: E501
        :type component_name: str
        :param images: The images of this ComponentSpec.  # noqa: E501
        :type images: List[FileId]
        :param num_of_instances: The num_of_instances of this ComponentSpec.  # noqa: E501
        :type num_of_instances: int
        :param restart_policy: The restart_policy of this ComponentSpec.  # noqa: E501
        :type restart_policy: str
        :param command_line_params: The command_line_params of this ComponentSpec.  # noqa: E501
        :type command_line_params: CommandLineParams
        :param exposed_interfaces: The exposed_interfaces of this ComponentSpec.  # noqa: E501
        :type exposed_interfaces: List[InterfaceDetails]
        :param compute_resource_profile: The compute_resource_profile of this ComponentSpec.  # noqa: E501
        :type compute_resource_profile: ComputeResourceInfo
        :param comp_env_params: The comp_env_params of this ComponentSpec.  # noqa: E501
        :type comp_env_params: List[CompEnvParams]
        :param deployment_config: The deployment_config of this ComponentSpec.  # noqa: E501
        :type deployment_config: DeploymentConfig
        :param persistent_volumes: The persistent_volumes of this ComponentSpec.  # noqa: E501
        :type persistent_volumes: List[PersistentVolumeDetails]
        """
        self.swagger_types = {
            'component_name': str,
            'images': List[FileId],
            'num_of_instances': int,
            'restart_policy': str,
            'command_line_params': CommandLineParams,
            'exposed_interfaces': List[InterfaceDetails],
            'compute_resource_profile': ComputeResourceInfo,
            'comp_env_params': List[CompEnvParams],
            'deployment_config': DeploymentConfig,
            'persistent_volumes': List[PersistentVolumeDetails]
        }

        self.attribute_map = {
            'component_name': 'componentName',
            'images': 'images',
            'num_of_instances': 'numOfInstances',
            'restart_policy': 'restartPolicy',
            'command_line_params': 'commandLineParams',
            'exposed_interfaces': 'exposedInterfaces',
            'compute_resource_profile': 'computeResourceProfile',
            'comp_env_params': 'compEnvParams',
            'deployment_config': 'deploymentConfig',
            'persistent_volumes': 'persistentVolumes'
        }
        self._component_name = component_name
        self._images = images
        self._num_of_instances = num_of_instances
        self._restart_policy = restart_policy
        self._command_line_params = command_line_params
        self._exposed_interfaces = exposed_interfaces
        self._compute_resource_profile = compute_resource_profile
        self._comp_env_params = comp_env_params
        self._deployment_config = deployment_config
        self._persistent_volumes = persistent_volumes

    @classmethod
    def from_dict(cls, dikt) -> 'ComponentSpec':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ComponentSpec of this ComponentSpec.  # noqa: E501
        :rtype: ComponentSpec
        """
        return util.deserialize_model(dikt, cls)

    @property
    def component_name(self) -> str:
        """Gets the component_name of this ComponentSpec.

        Must be a valid RFC 1035 label name.  Component name must be unique with an application  # noqa: E501

        :return: The component_name of this ComponentSpec.
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name: str):
        """Sets the component_name of this ComponentSpec.

        Must be a valid RFC 1035 label name.  Component name must be unique with an application  # noqa: E501

        :param component_name: The component_name of this ComponentSpec.
        :type component_name: str
        """
        if component_name is None:
            raise ValueError("Invalid value for `component_name`, must not be `None`")  # noqa: E501

        self._component_name = component_name

    @property
    def images(self) -> List[FileId]:
        """Gets the images of this ComponentSpec.

        List of all images associated with the component. Images are specified using the file identifiers. Partner OP provides these images using file upload api.  # noqa: E501

        :return: The images of this ComponentSpec.
        :rtype: List[FileId]
        """
        return self._images

    @images.setter
    def images(self, images: List[FileId]):
        """Sets the images of this ComponentSpec.

        List of all images associated with the component. Images are specified using the file identifiers. Partner OP provides these images using file upload api.  # noqa: E501

        :param images: The images of this ComponentSpec.
        :type images: List[FileId]
        """
        if images is None:
            raise ValueError("Invalid value for `images`, must not be `None`")  # noqa: E501

        self._images = images

    @property
    def num_of_instances(self) -> int:
        """Gets the num_of_instances of this ComponentSpec.

        Number of component instances to be launched.  # noqa: E501

        :return: The num_of_instances of this ComponentSpec.
        :rtype: int
        """
        return self._num_of_instances

    @num_of_instances.setter
    def num_of_instances(self, num_of_instances: int):
        """Sets the num_of_instances of this ComponentSpec.

        Number of component instances to be launched.  # noqa: E501

        :param num_of_instances: The num_of_instances of this ComponentSpec.
        :type num_of_instances: int
        """
        if num_of_instances is None:
            raise ValueError("Invalid value for `num_of_instances`, must not be `None`")  # noqa: E501

        self._num_of_instances = num_of_instances

    @property
    def restart_policy(self) -> str:
        """Gets the restart_policy of this ComponentSpec.

        How the platform shall handle component failure  # noqa: E501

        :return: The restart_policy of this ComponentSpec.
        :rtype: str
        """
        return self._restart_policy

    @restart_policy.setter
    def restart_policy(self, restart_policy: str):
        """Sets the restart_policy of this ComponentSpec.

        How the platform shall handle component failure  # noqa: E501

        :param restart_policy: The restart_policy of this ComponentSpec.
        :type restart_policy: str
        """
        allowed_values = ["RESTART_POLICY_ALWAYS", "RESTART_POLICY_NEVER"]  # noqa: E501
        if restart_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `restart_policy` ({0}), must be one of {1}"
                .format(restart_policy, allowed_values)
            )

        self._restart_policy = restart_policy

    @property
    def command_line_params(self) -> CommandLineParams:
        """Gets the command_line_params of this ComponentSpec.


        :return: The command_line_params of this ComponentSpec.
        :rtype: CommandLineParams
        """
        return self._command_line_params

    @command_line_params.setter
    def command_line_params(self, command_line_params: CommandLineParams):
        """Sets the command_line_params of this ComponentSpec.


        :param command_line_params: The command_line_params of this ComponentSpec.
        :type command_line_params: CommandLineParams
        """

        self._command_line_params = command_line_params

    @property
    def exposed_interfaces(self) -> List[InterfaceDetails]:
        """Gets the exposed_interfaces of this ComponentSpec.

        Each application component exposes some ports either for external users or for inter component communication. Application provider is required to specify which ports are to be exposed and the type of traffic that will flow through these ports.  # noqa: E501

        :return: The exposed_interfaces of this ComponentSpec.
        :rtype: List[InterfaceDetails]
        """
        return self._exposed_interfaces

    @exposed_interfaces.setter
    def exposed_interfaces(self, exposed_interfaces: List[InterfaceDetails]):
        """Sets the exposed_interfaces of this ComponentSpec.

        Each application component exposes some ports either for external users or for inter component communication. Application provider is required to specify which ports are to be exposed and the type of traffic that will flow through these ports.  # noqa: E501

        :param exposed_interfaces: The exposed_interfaces of this ComponentSpec.
        :type exposed_interfaces: List[InterfaceDetails]
        """

        self._exposed_interfaces = exposed_interfaces

    @property
    def compute_resource_profile(self) -> ComputeResourceInfo:
        """Gets the compute_resource_profile of this ComponentSpec.


        :return: The compute_resource_profile of this ComponentSpec.
        :rtype: ComputeResourceInfo
        """
        return self._compute_resource_profile

    @compute_resource_profile.setter
    def compute_resource_profile(self, compute_resource_profile: ComputeResourceInfo):
        """Sets the compute_resource_profile of this ComponentSpec.


        :param compute_resource_profile: The compute_resource_profile of this ComponentSpec.
        :type compute_resource_profile: ComputeResourceInfo
        """
        if compute_resource_profile is None:
            raise ValueError("Invalid value for `compute_resource_profile`, must not be `None`")  # noqa: E501

        self._compute_resource_profile = compute_resource_profile

    @property
    def comp_env_params(self) -> List[CompEnvParams]:
        """Gets the comp_env_params of this ComponentSpec.


        :return: The comp_env_params of this ComponentSpec.
        :rtype: List[CompEnvParams]
        """
        return self._comp_env_params

    @comp_env_params.setter
    def comp_env_params(self, comp_env_params: List[CompEnvParams]):
        """Sets the comp_env_params of this ComponentSpec.


        :param comp_env_params: The comp_env_params of this ComponentSpec.
        :type comp_env_params: List[CompEnvParams]
        """

        self._comp_env_params = comp_env_params

    @property
    def deployment_config(self) -> DeploymentConfig:
        """Gets the deployment_config of this ComponentSpec.


        :return: The deployment_config of this ComponentSpec.
        :rtype: DeploymentConfig
        """
        return self._deployment_config

    @deployment_config.setter
    def deployment_config(self, deployment_config: DeploymentConfig):
        """Sets the deployment_config of this ComponentSpec.


        :param deployment_config: The deployment_config of this ComponentSpec.
        :type deployment_config: DeploymentConfig
        """

        self._deployment_config = deployment_config

    @property
    def persistent_volumes(self) -> List[PersistentVolumeDetails]:
        """Gets the persistent_volumes of this ComponentSpec.

        The ephemeral volume a container process may need to temporary store internal data  # noqa: E501

        :return: The persistent_volumes of this ComponentSpec.
        :rtype: List[PersistentVolumeDetails]
        """
        return self._persistent_volumes

    @persistent_volumes.setter
    def persistent_volumes(self, persistent_volumes: List[PersistentVolumeDetails]):
        """Sets the persistent_volumes of this ComponentSpec.

        The ephemeral volume a container process may need to temporary store internal data  # noqa: E501

        :param persistent_volumes: The persistent_volumes of this ComponentSpec.
        :type persistent_volumes: List[PersistentVolumeDetails]
        """

        self._persistent_volumes = persistent_volumes
