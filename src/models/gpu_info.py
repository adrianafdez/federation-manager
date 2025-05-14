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


class GpuInfo(Model):
    def __init__(self, gpu_vendor_type: str=None, gpu_mode_name: str=None, gpu_memory: int=None, num_gpu: int=None):  # noqa: E501
        """GpuInfo - a model defined in Swagger

        :param gpu_vendor_type: The gpu_vendor_type of this GpuInfo.  # noqa: E501
        :type gpu_vendor_type: str
        :param gpu_mode_name: The gpu_mode_name of this GpuInfo.  # noqa: E501
        :type gpu_mode_name: str
        :param gpu_memory: The gpu_memory of this GpuInfo.  # noqa: E501
        :type gpu_memory: int
        :param num_gpu: The num_gpu of this GpuInfo.  # noqa: E501
        :type num_gpu: int
        """
        self.swagger_types = {
            'gpu_vendor_type': str,
            'gpu_mode_name': str,
            'gpu_memory': int,
            'num_gpu': int
        }

        self.attribute_map = {
            'gpu_vendor_type': 'gpuVendorType',
            'gpu_mode_name': 'gpuModeName',
            'gpu_memory': 'gpuMemory',
            'num_gpu': 'numGPU'
        }
        self._gpu_vendor_type = gpu_vendor_type
        self._gpu_mode_name = gpu_mode_name
        self._gpu_memory = gpu_memory
        self._num_gpu = num_gpu

    @classmethod
    def from_dict(cls, dikt) -> 'GpuInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GpuInfo of this GpuInfo.  # noqa: E501
        :rtype: GpuInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def gpu_vendor_type(self) -> str:
        """Gets the gpu_vendor_type of this GpuInfo.

        GPU vendor name e.g. NVIDIA, AMD etc.  # noqa: E501

        :return: The gpu_vendor_type of this GpuInfo.
        :rtype: str
        """
        return self._gpu_vendor_type

    @gpu_vendor_type.setter
    def gpu_vendor_type(self, gpu_vendor_type: str):
        """Sets the gpu_vendor_type of this GpuInfo.

        GPU vendor name e.g. NVIDIA, AMD etc.  # noqa: E501

        :param gpu_vendor_type: The gpu_vendor_type of this GpuInfo.
        :type gpu_vendor_type: str
        """
        if gpu_vendor_type != "":
            allowed_values = ["GPU_PROVIDER_NVIDIA", "GPU_PROVIDER_AMD"]  # noqa: E501
            if gpu_vendor_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `gpu_vendor_type` ({0}), must be one of {1}"
                    .format(gpu_vendor_type, allowed_values)
                )

        self._gpu_vendor_type = gpu_vendor_type

    @property
    def gpu_mode_name(self) -> str:
        """Gets the gpu_mode_name of this GpuInfo.

        Model name corresponding to vendorType may include info e.g. for NVIDIA, model name could be “Tesla M60”, “Tesla V100” etc.  # noqa: E501

        :return: The gpu_mode_name of this GpuInfo.
        :rtype: str
        """
        return self._gpu_mode_name

    @gpu_mode_name.setter
    def gpu_mode_name(self, gpu_mode_name: str):
        """Sets the gpu_mode_name of this GpuInfo.

        Model name corresponding to vendorType may include info e.g. for NVIDIA, model name could be “Tesla M60”, “Tesla V100” etc.  # noqa: E501

        :param gpu_mode_name: The gpu_mode_name of this GpuInfo.
        :type gpu_mode_name: str
        """
        if gpu_mode_name is None:
            raise ValueError("Invalid value for `gpu_mode_name`, must not be `None`")  # noqa: E501

        self._gpu_mode_name = gpu_mode_name

    @property
    def gpu_memory(self) -> int:
        """Gets the gpu_memory of this GpuInfo.

        GPU memory in Mbytes  # noqa: E501

        :return: The gpu_memory of this GpuInfo.
        :rtype: int
        """
        return self._gpu_memory

    @gpu_memory.setter
    def gpu_memory(self, gpu_memory: int):
        """Sets the gpu_memory of this GpuInfo.

        GPU memory in Mbytes  # noqa: E501

        :param gpu_memory: The gpu_memory of this GpuInfo.
        :type gpu_memory: int
        """
        if gpu_memory is None:
            raise ValueError("Invalid value for `gpu_memory`, must not be `None`")  # noqa: E501

        self._gpu_memory = gpu_memory

    @property
    def num_gpu(self) -> int:
        """Gets the num_gpu of this GpuInfo.

        Number of GPUs  # noqa: E501

        :return: The num_gpu of this GpuInfo.
        :rtype: int
        """
        return self._num_gpu

    @num_gpu.setter
    def num_gpu(self, num_gpu: int):
        """Sets the num_gpu of this GpuInfo.

        Number of GPUs  # noqa: E501

        :param num_gpu: The num_gpu of this GpuInfo.
        :type num_gpu: int
        """
        if num_gpu is None:
            raise ValueError("Invalid value for `num_gpu`, must not be `None`")  # noqa: E501

        self._num_gpu = num_gpu
