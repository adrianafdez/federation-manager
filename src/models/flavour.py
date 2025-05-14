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
from models.cpu_arch_type import CPUArchType  # noqa: F401,E501
from models.flavour_id import FlavourId  # noqa: F401,E501
from models.gpu_info import GpuInfo  # noqa: F401,E501
from models.huge_page import HugePage  # noqa: F401,E501
from models.os_type import OSType  # noqa: F401,E501
import util


class Flavour(Model):
    def __init__(self, flavour_id: FlavourId=None, cpu_arch_type: CPUArchType=None, supported_os_types: List[OSType]=None, num_cpu: int=None, memory_size: int=None, storage_size: int=None, gpu: List[GpuInfo]=None, fpga: int=None, vpu: int=None, hugepages: List[HugePage]=None, cpu_exclusivity: bool=None):  # noqa: E501
        """Flavour - a model defined in Swagger

        :param flavour_id: The flavour_id of this Flavour.  # noqa: E501
        :type flavour_id: FlavourId
        :param cpu_arch_type: The cpu_arch_type of this Flavour.  # noqa: E501
        :type cpu_arch_type: CPUArchType
        :param supported_os_types: The supported_os_types of this Flavour.  # noqa: E501
        :type supported_os_types: List[OSType]
        :param num_cpu: The num_cpu of this Flavour.  # noqa: E501
        :type num_cpu: int
        :param memory_size: The memory_size of this Flavour.  # noqa: E501
        :type memory_size: int
        :param storage_size: The storage_size of this Flavour.  # noqa: E501
        :type storage_size: int
        :param gpu: The gpu of this Flavour.  # noqa: E501
        :type gpu: List[GpuInfo]
        :param fpga: The fpga of this Flavour.  # noqa: E501
        :type fpga: int
        :param vpu: The vpu of this Flavour.  # noqa: E501
        :type vpu: int
        :param hugepages: The hugepages of this Flavour.  # noqa: E501
        :type hugepages: List[HugePage]
        :param cpu_exclusivity: The cpu_exclusivity of this Flavour.  # noqa: E501
        :type cpu_exclusivity: bool
        """
        self.swagger_types = {
            'flavour_id': FlavourId,
            'cpu_arch_type': CPUArchType,
            'supported_os_types': List[OSType],
            'num_cpu': int,
            'memory_size': int,
            'storage_size': int,
            'gpu': List[GpuInfo],
            'fpga': int,
            'vpu': int,
            'hugepages': List[HugePage],
            'cpu_exclusivity': bool
        }

        self.attribute_map = {
            'flavour_id': 'flavourId',
            'cpu_arch_type': 'cpuArchType',
            'supported_os_types': 'supportedOSTypes',
            'num_cpu': 'numCPU',
            'memory_size': 'memorySize',
            'storage_size': 'storageSize',
            'gpu': 'gpu',
            'fpga': 'fpga',
            'vpu': 'vpu',
            'hugepages': 'hugepages',
            'cpu_exclusivity': 'cpuExclusivity'
        }
        self._flavour_id = flavour_id
        self._cpu_arch_type = cpu_arch_type
        self._supported_os_types = supported_os_types
        self._num_cpu = num_cpu
        self._memory_size = memory_size
        self._storage_size = storage_size
        self._gpu = gpu
        self._fpga = fpga
        self._vpu = vpu
        self._hugepages = hugepages
        self._cpu_exclusivity = cpu_exclusivity

    @classmethod
    def from_dict(cls, dikt) -> 'Flavour':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Flavour of this Flavour.  # noqa: E501
        :rtype: Flavour
        """
        return util.deserialize_model(dikt, cls)

    @property
    def flavour_id(self) -> FlavourId:
        """Gets the flavour_id of this Flavour.


        :return: The flavour_id of this Flavour.
        :rtype: FlavourId
        """
        return self._flavour_id

    @flavour_id.setter
    def flavour_id(self, flavour_id: FlavourId):
        """Sets the flavour_id of this Flavour.


        :param flavour_id: The flavour_id of this Flavour.
        :type flavour_id: FlavourId
        """
        if flavour_id is None:
            raise ValueError("Invalid value for `flavour_id`, must not be `None`")  # noqa: E501

        self._flavour_id = flavour_id

    @property
    def cpu_arch_type(self) -> CPUArchType:
        """Gets the cpu_arch_type of this Flavour.


        :return: The cpu_arch_type of this Flavour.
        :rtype: CPUArchType
        """
        return self._cpu_arch_type

    @cpu_arch_type.setter
    def cpu_arch_type(self, cpu_arch_type: CPUArchType):
        """Sets the cpu_arch_type of this Flavour.


        :param cpu_arch_type: The cpu_arch_type of this Flavour.
        :type cpu_arch_type: CPUArchType
        """
        if cpu_arch_type is None:
            raise ValueError("Invalid value for `cpu_arch_type`, must not be `None`")  # noqa: E501

        self._cpu_arch_type = cpu_arch_type

    @property
    def supported_os_types(self) -> List[OSType]:
        """Gets the supported_os_types of this Flavour.

        A list of operating systems which this flavour configuration can support e.g., RHEL Linux, Ubuntu 18.04 LTS, MS Windows 2012 R2.  # noqa: E501

        :return: The supported_os_types of this Flavour.
        :rtype: List[OSType]
        """
        return self._supported_os_types

    @supported_os_types.setter
    def supported_os_types(self, supported_os_types: List[OSType]):
        """Sets the supported_os_types of this Flavour.

        A list of operating systems which this flavour configuration can support e.g., RHEL Linux, Ubuntu 18.04 LTS, MS Windows 2012 R2.  # noqa: E501

        :param supported_os_types: The supported_os_types of this Flavour.
        :type supported_os_types: List[OSType]
        """
        if supported_os_types is None:
            raise ValueError("Invalid value for `supported_os_types`, must not be `None`")  # noqa: E501

        self._supported_os_types = supported_os_types

    @property
    def num_cpu(self) -> int:
        """Gets the num_cpu of this Flavour.

        Number of available vCPUs  # noqa: E501

        :return: The num_cpu of this Flavour.
        :rtype: int
        """
        return self._num_cpu

    @num_cpu.setter
    def num_cpu(self, num_cpu: int):
        """Sets the num_cpu of this Flavour.

        Number of available vCPUs  # noqa: E501

        :param num_cpu: The num_cpu of this Flavour.
        :type num_cpu: int
        """
        if num_cpu is None:
            raise ValueError("Invalid value for `num_cpu`, must not be `None`")  # noqa: E501

        self._num_cpu = num_cpu

    @property
    def memory_size(self) -> int:
        """Gets the memory_size of this Flavour.

        Amount of RAM in Mbytes  # noqa: E501

        :return: The memory_size of this Flavour.
        :rtype: int
        """
        return self._memory_size

    @memory_size.setter
    def memory_size(self, memory_size: int):
        """Sets the memory_size of this Flavour.

        Amount of RAM in Mbytes  # noqa: E501

        :param memory_size: The memory_size of this Flavour.
        :type memory_size: int
        """
        if memory_size is None:
            raise ValueError("Invalid value for `memory_size`, must not be `None`")  # noqa: E501

        self._memory_size = memory_size

    @property
    def storage_size(self) -> int:
        """Gets the storage_size of this Flavour.

        Amount of disk storage in Gbytes  # noqa: E501

        :return: The storage_size of this Flavour.
        :rtype: int
        """
        return self._storage_size

    @storage_size.setter
    def storage_size(self, storage_size: int):
        """Sets the storage_size of this Flavour.

        Amount of disk storage in Gbytes  # noqa: E501

        :param storage_size: The storage_size of this Flavour.
        :type storage_size: int
        """
        if storage_size is None:
            raise ValueError("Invalid value for `storage_size`, must not be `None`")  # noqa: E501

        self._storage_size = storage_size

    @property
    def gpu(self) -> List[GpuInfo]:
        """Gets the gpu of this Flavour.


        :return: The gpu of this Flavour.
        :rtype: List[GpuInfo]
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu: List[GpuInfo]):
        """Sets the gpu of this Flavour.


        :param gpu: The gpu of this Flavour.
        :type gpu: List[GpuInfo]
        """

        self._gpu = gpu

    @property
    def fpga(self) -> int:
        """Gets the fpga of this Flavour.

        Number of FPGAs  # noqa: E501

        :return: The fpga of this Flavour.
        :rtype: int
        """
        return self._fpga

    @fpga.setter
    def fpga(self, fpga: int):
        """Sets the fpga of this Flavour.

        Number of FPGAs  # noqa: E501

        :param fpga: The fpga of this Flavour.
        :type fpga: int
        """

        self._fpga = fpga

    @property
    def vpu(self) -> int:
        """Gets the vpu of this Flavour.

        Number of Intel VPUs available  # noqa: E501

        :return: The vpu of this Flavour.
        :rtype: int
        """
        return self._vpu

    @vpu.setter
    def vpu(self, vpu: int):
        """Sets the vpu of this Flavour.

        Number of Intel VPUs available  # noqa: E501

        :param vpu: The vpu of this Flavour.
        :type vpu: int
        """

        self._vpu = vpu

    @property
    def hugepages(self) -> List[HugePage]:
        """Gets the hugepages of this Flavour.


        :return: The hugepages of this Flavour.
        :rtype: List[HugePage]
        """
        return self._hugepages

    @hugepages.setter
    def hugepages(self, hugepages: List[HugePage]):
        """Sets the hugepages of this Flavour.


        :param hugepages: The hugepages of this Flavour.
        :type hugepages: List[HugePage]
        """

        self._hugepages = hugepages

    @property
    def cpu_exclusivity(self) -> bool:
        """Gets the cpu_exclusivity of this Flavour.

        Support for exclusive CPUs  # noqa: E501

        :return: The cpu_exclusivity of this Flavour.
        :rtype: bool
        """
        return self._cpu_exclusivity

    @cpu_exclusivity.setter
    def cpu_exclusivity(self, cpu_exclusivity: bool):
        """Sets the cpu_exclusivity of this Flavour.

        Support for exclusive CPUs  # noqa: E501

        :param cpu_exclusivity: The cpu_exclusivity of this Flavour.
        :type cpu_exclusivity: bool
        """

        self._cpu_exclusivity = cpu_exclusivity
