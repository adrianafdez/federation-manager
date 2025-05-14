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


class ZoneRegisteredDataZoneServiceLevelObjsInfoThroughputRanges(Model):
    def __init__(self, min_throughput: int=None, max_throughput: int=None):  # noqa: E501
        """ZoneRegisteredDataZoneServiceLevelObjsInfoThroughputRanges - a model defined in Swagger

        :param min_throughput: The min_throughput of this ZoneRegisteredDataZoneServiceLevelObjsInfoThroughputRanges.  # noqa: E501
        :type min_throughput: int
        :param max_throughput: The max_throughput of this ZoneRegisteredDataZoneServiceLevelObjsInfoThroughputRanges.  # noqa: E501
        :type max_throughput: int
        """
        self.swagger_types = {
            'min_throughput': int,
            'max_throughput': int
        }

        self.attribute_map = {
            'min_throughput': 'minThroughput',
            'max_throughput': 'maxThroughput'
        }
        self._min_throughput = min_throughput
        self._max_throughput = max_throughput

    @classmethod
    def from_dict(cls, dikt) -> 'ZoneRegisteredDataZoneServiceLevelObjsInfoThroughputRanges':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ZoneRegisteredData_zoneServiceLevelObjsInfo_throughputRanges of this ZoneRegisteredDataZoneServiceLevelObjsInfoThroughputRanges.  # noqa: E501
        :rtype: ZoneRegisteredDataZoneServiceLevelObjsInfoThroughputRanges
        """
        return util.deserialize_model(dikt, cls)

    @property
    def min_throughput(self) -> int:
        """Gets the min_throughput of this ZoneRegisteredDataZoneServiceLevelObjsInfoThroughputRanges.

        The minimum limit of network throughput between UC and Edge App in Mega bits per seconds (Mbps).  # noqa: E501

        :return: The min_throughput of this ZoneRegisteredDataZoneServiceLevelObjsInfoThroughputRanges.
        :rtype: int
        """
        return self._min_throughput

    @min_throughput.setter
    def min_throughput(self, min_throughput: int):
        """Sets the min_throughput of this ZoneRegisteredDataZoneServiceLevelObjsInfoThroughputRanges.

        The minimum limit of network throughput between UC and Edge App in Mega bits per seconds (Mbps).  # noqa: E501

        :param min_throughput: The min_throughput of this ZoneRegisteredDataZoneServiceLevelObjsInfoThroughputRanges.
        :type min_throughput: int
        """

        self._min_throughput = min_throughput

    @property
    def max_throughput(self) -> int:
        """Gets the max_throughput of this ZoneRegisteredDataZoneServiceLevelObjsInfoThroughputRanges.

        The maximum limit of network throughput between UC and Edge App in Mega bits per seconds (Mbps).  # noqa: E501

        :return: The max_throughput of this ZoneRegisteredDataZoneServiceLevelObjsInfoThroughputRanges.
        :rtype: int
        """
        return self._max_throughput

    @max_throughput.setter
    def max_throughput(self, max_throughput: int):
        """Sets the max_throughput of this ZoneRegisteredDataZoneServiceLevelObjsInfoThroughputRanges.

        The maximum limit of network throughput between UC and Edge App in Mega bits per seconds (Mbps).  # noqa: E501

        :param max_throughput: The max_throughput of this ZoneRegisteredDataZoneServiceLevelObjsInfoThroughputRanges.
        :type max_throughput: int
        """

        self._max_throughput = max_throughput
