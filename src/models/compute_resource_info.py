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
from models.gpu_info import GpuInfo  # noqa: F401,E501
from models.huge_page import HugePage  # noqa: F401,E501
from models.vcpu import Vcpu  # noqa: F401,E501
import re  # noqa: F401,E501
import util


class ComputeResourceInfo(Model):
    def __init__(self, cpu_arch_type: str=None, num_cpu: Vcpu=None, memory: int=None, disk_storage: int=None, gpu: List[GpuInfo]=None, vpu: int=None, fpga: int=None, hugepages: List[HugePage]=None, cpu_exclusivity: bool=None):  # noqa: E501
        """ComputeResourceInfo - a model defined in Swagger

        :param cpu_arch_type: The cpu_arch_type of this ComputeResourceInfo.  # noqa: E501
        :type cpu_arch_type: str
        :param num_cpu: The num_cpu of this ComputeResourceInfo.  # noqa: E501
        :type num_cpu: Vcpu
        :param memory: The memory of this ComputeResourceInfo.  # noqa: E501
        :type memory: int
        :param disk_storage: The disk_storage of this ComputeResourceInfo.  # noqa: E501
        :type disk_storage: int
        :param gpu: The gpu of this ComputeResourceInfo.  # noqa: E501
        :type gpu: List[GpuInfo]
        :param vpu: The vpu of this ComputeResourceInfo.  # noqa: E501
        :type vpu: int
        :param fpga: The fpga of this ComputeResourceInfo.  # noqa: E501
        :type fpga: int
        :param hugepages: The hugepages of this ComputeResourceInfo.  # noqa: E501
        :type hugepages: List[HugePage]
        :param cpu_exclusivity: The cpu_exclusivity of this ComputeResourceInfo.  # noqa: E501
        :type cpu_exclusivity: bool
        """
        self.swagger_types = {
            'cpu_arch_type': str,
            'num_cpu': Vcpu,
            'memory': int,
            'disk_storage': int,
            'gpu': List[GpuInfo],
            'vpu': int,
            'fpga': int,
            'hugepages': List[HugePage],
            'cpu_exclusivity': bool
        }

        self.attribute_map = {
            'cpu_arch_type': 'cpuArchType',
            'num_cpu': 'numCPU',
            'memory': 'memory',
            'disk_storage': 'diskStorage',
            'gpu': 'gpu',
            'vpu': 'vpu',
            'fpga': 'fpga',
            'hugepages': 'hugepages',
            'cpu_exclusivity': 'cpuExclusivity'
        }
        self._cpu_arch_type = cpu_arch_type
        self._num_cpu = num_cpu
        self._memory = memory
        self._disk_storage = disk_storage
        self._gpu = gpu
        self._vpu = vpu
        self._fpga = fpga
        self._hugepages = hugepages
        self._cpu_exclusivity = cpu_exclusivity

    @classmethod
    def from_dict(cls, dikt) -> 'ComputeResourceInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ComputeResourceInfo of this ComputeResourceInfo.  # noqa: E501
        :rtype: ComputeResourceInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cpu_arch_type(self) -> str:
        """Gets the cpu_arch_type of this ComputeResourceInfo.

        CPU Instruction Set Architecture (ISA) E.g., Intel, Arm etc.  # noqa: E501

        :return: The cpu_arch_type of this ComputeResourceInfo.
        :rtype: str
        """
        return self._cpu_arch_type

    @cpu_arch_type.setter
    def cpu_arch_type(self, cpu_arch_type: str):
        """Sets the cpu_arch_type of this ComputeResourceInfo.

        CPU Instruction Set Architecture (ISA) E.g., Intel, Arm etc.  # noqa: E501

        :param cpu_arch_type: The cpu_arch_type of this ComputeResourceInfo.
        :type cpu_arch_type: str
        """
        allowed_values = ["ISA_X86_64", "ISA_ARM_64"]  # noqa: E501
        if cpu_arch_type not in allowed_values:
            raise ValueError(
                "Invalid value for `cpu_arch_type` ({0}), must be one of {1}"
                .format(cpu_arch_type, allowed_values)
            )

        self._cpu_arch_type = cpu_arch_type

    @property
    def num_cpu(self) -> Vcpu:
        """Gets the num_cpu of this ComputeResourceInfo.


        :return: The num_cpu of this ComputeResourceInfo.
        :rtype: Vcpu
        """
        return self._num_cpu

    @num_cpu.setter
    def num_cpu(self, num_cpu: Vcpu):
        """Sets the num_cpu of this ComputeResourceInfo.


        :param num_cpu: The num_cpu of this ComputeResourceInfo.
        :type num_cpu: Vcpu
        """
        if num_cpu is None:
            raise ValueError("Invalid value for `num_cpu`, must not be `None`")  # noqa: E501

        self._num_cpu = num_cpu

    @property
    def memory(self) -> int:
        """Gets the memory of this ComputeResourceInfo.

        Amount of RAM in Mbytes  # noqa: E501

        :return: The memory of this ComputeResourceInfo.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory: int):
        """Sets the memory of this ComputeResourceInfo.

        Amount of RAM in Mbytes  # noqa: E501

        :param memory: The memory of this ComputeResourceInfo.
        :type memory: int
        """
        if memory is None:
            raise ValueError("Invalid value for `memory`, must not be `None`")  # noqa: E501

        self._memory = memory

    @property
    def disk_storage(self) -> int:
        """Gets the disk_storage of this ComputeResourceInfo.

        Amount of disk storage in Gbytes for a given ISA type  # noqa: E501

        :return: The disk_storage of this ComputeResourceInfo.
        :rtype: int
        """
        return self._disk_storage

    @disk_storage.setter
    def disk_storage(self, disk_storage: int):
        """Sets the disk_storage of this ComputeResourceInfo.

        Amount of disk storage in Gbytes for a given ISA type  # noqa: E501

        :param disk_storage: The disk_storage of this ComputeResourceInfo.
        :type disk_storage: int
        """

        self._disk_storage = disk_storage

    @property
    def gpu(self) -> List[GpuInfo]:
        """Gets the gpu of this ComputeResourceInfo.


        :return: The gpu of this ComputeResourceInfo.
        :rtype: List[GpuInfo]
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu: List[GpuInfo]):
        """Sets the gpu of this ComputeResourceInfo.


        :param gpu: The gpu of this ComputeResourceInfo.
        :type gpu: List[GpuInfo]
        """

        self._gpu = gpu

    @property
    def vpu(self) -> int:
        """Gets the vpu of this ComputeResourceInfo.

        Number of Intel VPUs available for a given ISA type  # noqa: E501

        :return: The vpu of this ComputeResourceInfo.
        :rtype: int
        """
        return self._vpu

    @vpu.setter
    def vpu(self, vpu: int):
        """Sets the vpu of this ComputeResourceInfo.

        Number of Intel VPUs available for a given ISA type  # noqa: E501

        :param vpu: The vpu of this ComputeResourceInfo.
        :type vpu: int
        """

        self._vpu = vpu

    @property
    def fpga(self) -> int:
        """Gets the fpga of this ComputeResourceInfo.

        Number of FPGAs available for a given ISA type  # noqa: E501

        :return: The fpga of this ComputeResourceInfo.
        :rtype: int
        """
        return self._fpga

    @fpga.setter
    def fpga(self, fpga: int):
        """Sets the fpga of this ComputeResourceInfo.

        Number of FPGAs available for a given ISA type  # noqa: E501

        :param fpga: The fpga of this ComputeResourceInfo.
        :type fpga: int
        """

        self._fpga = fpga

    @property
    def hugepages(self) -> List[HugePage]:
        """Gets the hugepages of this ComputeResourceInfo.


        :return: The hugepages of this ComputeResourceInfo.
        :rtype: List[HugePage]
        """
        return self._hugepages

    @hugepages.setter
    def hugepages(self, hugepages: List[HugePage]):
        """Sets the hugepages of this ComputeResourceInfo.


        :param hugepages: The hugepages of this ComputeResourceInfo.
        :type hugepages: List[HugePage]
        """

        self._hugepages = hugepages

    @property
    def cpu_exclusivity(self) -> bool:
        """Gets the cpu_exclusivity of this ComputeResourceInfo.

        Support for exclusive CPUs  # noqa: E501

        :return: The cpu_exclusivity of this ComputeResourceInfo.
        :rtype: bool
        """
        return self._cpu_exclusivity

    @cpu_exclusivity.setter
    def cpu_exclusivity(self, cpu_exclusivity: bool):
        """Sets the cpu_exclusivity of this ComputeResourceInfo.

        Support for exclusive CPUs  # noqa: E501

        :param cpu_exclusivity: The cpu_exclusivity of this ComputeResourceInfo.
        :type cpu_exclusivity: bool
        """

        self._cpu_exclusivity = cpu_exclusivity
