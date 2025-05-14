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


class ZoneRegisteredDataZoneServiceLevelObjsInfoLatencyRanges(Model):
    def __init__(self, min_latency: int=None, max_latency: int=None):  # noqa: E501
        """ZoneRegisteredDataZoneServiceLevelObjsInfoLatencyRanges - a model defined in Swagger

        :param min_latency: The min_latency of this ZoneRegisteredDataZoneServiceLevelObjsInfoLatencyRanges.  # noqa: E501
        :type min_latency: int
        :param max_latency: The max_latency of this ZoneRegisteredDataZoneServiceLevelObjsInfoLatencyRanges.  # noqa: E501
        :type max_latency: int
        """
        self.swagger_types = {
            'min_latency': int,
            'max_latency': int
        }

        self.attribute_map = {
            'min_latency': 'minLatency',
            'max_latency': 'maxLatency'
        }
        self._min_latency = min_latency
        self._max_latency = max_latency

    @classmethod
    def from_dict(cls, dikt) -> 'ZoneRegisteredDataZoneServiceLevelObjsInfoLatencyRanges':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ZoneRegisteredData_zoneServiceLevelObjsInfo_latencyRanges of this ZoneRegisteredDataZoneServiceLevelObjsInfoLatencyRanges.  # noqa: E501
        :rtype: ZoneRegisteredDataZoneServiceLevelObjsInfoLatencyRanges
        """
        return util.deserialize_model(dikt, cls)

    @property
    def min_latency(self) -> int:
        """Gets the min_latency of this ZoneRegisteredDataZoneServiceLevelObjsInfoLatencyRanges.

        The time for data/packet to reach from UC to edge application. It represent mínimum latency in milli seconds that may exist between UCs and edge apps in this zone but it can be higher in actual.  # noqa: E501

        :return: The min_latency of this ZoneRegisteredDataZoneServiceLevelObjsInfoLatencyRanges.
        :rtype: int
        """
        return self._min_latency

    @min_latency.setter
    def min_latency(self, min_latency: int):
        """Sets the min_latency of this ZoneRegisteredDataZoneServiceLevelObjsInfoLatencyRanges.

        The time for data/packet to reach from UC to edge application. It represent mínimum latency in milli seconds that may exist between UCs and edge apps in this zone but it can be higher in actual.  # noqa: E501

        :param min_latency: The min_latency of this ZoneRegisteredDataZoneServiceLevelObjsInfoLatencyRanges.
        :type min_latency: int
        """

        self._min_latency = min_latency

    @property
    def max_latency(self) -> int:
        """Gets the max_latency of this ZoneRegisteredDataZoneServiceLevelObjsInfoLatencyRanges.

        The maximum limit of latency between UC and Edge App in milli seconds.  # noqa: E501

        :return: The max_latency of this ZoneRegisteredDataZoneServiceLevelObjsInfoLatencyRanges.
        :rtype: int
        """
        return self._max_latency

    @max_latency.setter
    def max_latency(self, max_latency: int):
        """Sets the max_latency of this ZoneRegisteredDataZoneServiceLevelObjsInfoLatencyRanges.

        The maximum limit of latency between UC and Edge App in milli seconds.  # noqa: E501

        :param max_latency: The max_latency of this ZoneRegisteredDataZoneServiceLevelObjsInfoLatencyRanges.
        :type max_latency: int
        """

        self._max_latency = max_latency
