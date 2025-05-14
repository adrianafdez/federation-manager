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
from models.zone_registered_data_zone_service_level_objs_info_jitter_ranges import ZoneRegisteredDataZoneServiceLevelObjsInfoJitterRanges  # noqa: F401,E501
from models.zone_registered_data_zone_service_level_objs_info_latency_ranges import ZoneRegisteredDataZoneServiceLevelObjsInfoLatencyRanges  # noqa: F401,E501
from models.zone_registered_data_zone_service_level_objs_info_throughput_ranges import ZoneRegisteredDataZoneServiceLevelObjsInfoThroughputRanges  # noqa: F401,E501
import util


class ZoneRegisteredDataZoneServiceLevelObjsInfo(Model):
    def __init__(self, latency_ranges: ZoneRegisteredDataZoneServiceLevelObjsInfoLatencyRanges=None, jitter_ranges: ZoneRegisteredDataZoneServiceLevelObjsInfoJitterRanges=None, throughput_ranges: ZoneRegisteredDataZoneServiceLevelObjsInfoThroughputRanges=None):  # noqa: E501
        """ZoneRegisteredDataZoneServiceLevelObjsInfo - a model defined in Swagger

        :param latency_ranges: The latency_ranges of this ZoneRegisteredDataZoneServiceLevelObjsInfo.  # noqa: E501
        :type latency_ranges: ZoneRegisteredDataZoneServiceLevelObjsInfoLatencyRanges
        :param jitter_ranges: The jitter_ranges of this ZoneRegisteredDataZoneServiceLevelObjsInfo.  # noqa: E501
        :type jitter_ranges: ZoneRegisteredDataZoneServiceLevelObjsInfoJitterRanges
        :param throughput_ranges: The throughput_ranges of this ZoneRegisteredDataZoneServiceLevelObjsInfo.  # noqa: E501
        :type throughput_ranges: ZoneRegisteredDataZoneServiceLevelObjsInfoThroughputRanges
        """
        self.swagger_types = {
            'latency_ranges': ZoneRegisteredDataZoneServiceLevelObjsInfoLatencyRanges,
            'jitter_ranges': ZoneRegisteredDataZoneServiceLevelObjsInfoJitterRanges,
            'throughput_ranges': ZoneRegisteredDataZoneServiceLevelObjsInfoThroughputRanges
        }

        self.attribute_map = {
            'latency_ranges': 'latencyRanges',
            'jitter_ranges': 'jitterRanges',
            'throughput_ranges': 'throughputRanges'
        }
        self._latency_ranges = latency_ranges
        self._jitter_ranges = jitter_ranges
        self._throughput_ranges = throughput_ranges

    @classmethod
    def from_dict(cls, dikt) -> 'ZoneRegisteredDataZoneServiceLevelObjsInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ZoneRegisteredData_zoneServiceLevelObjsInfo of this ZoneRegisteredDataZoneServiceLevelObjsInfo.  # noqa: E501
        :rtype: ZoneRegisteredDataZoneServiceLevelObjsInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def latency_ranges(self) -> ZoneRegisteredDataZoneServiceLevelObjsInfoLatencyRanges:
        """Gets the latency_ranges of this ZoneRegisteredDataZoneServiceLevelObjsInfo.


        :return: The latency_ranges of this ZoneRegisteredDataZoneServiceLevelObjsInfo.
        :rtype: ZoneRegisteredDataZoneServiceLevelObjsInfoLatencyRanges
        """
        return self._latency_ranges

    @latency_ranges.setter
    def latency_ranges(self, latency_ranges: ZoneRegisteredDataZoneServiceLevelObjsInfoLatencyRanges):
        """Sets the latency_ranges of this ZoneRegisteredDataZoneServiceLevelObjsInfo.


        :param latency_ranges: The latency_ranges of this ZoneRegisteredDataZoneServiceLevelObjsInfo.
        :type latency_ranges: ZoneRegisteredDataZoneServiceLevelObjsInfoLatencyRanges
        """
        if latency_ranges is None:
            raise ValueError("Invalid value for `latency_ranges`, must not be `None`")  # noqa: E501

        self._latency_ranges = latency_ranges

    @property
    def jitter_ranges(self) -> ZoneRegisteredDataZoneServiceLevelObjsInfoJitterRanges:
        """Gets the jitter_ranges of this ZoneRegisteredDataZoneServiceLevelObjsInfo.


        :return: The jitter_ranges of this ZoneRegisteredDataZoneServiceLevelObjsInfo.
        :rtype: ZoneRegisteredDataZoneServiceLevelObjsInfoJitterRanges
        """
        return self._jitter_ranges

    @jitter_ranges.setter
    def jitter_ranges(self, jitter_ranges: ZoneRegisteredDataZoneServiceLevelObjsInfoJitterRanges):
        """Sets the jitter_ranges of this ZoneRegisteredDataZoneServiceLevelObjsInfo.


        :param jitter_ranges: The jitter_ranges of this ZoneRegisteredDataZoneServiceLevelObjsInfo.
        :type jitter_ranges: ZoneRegisteredDataZoneServiceLevelObjsInfoJitterRanges
        """
        if jitter_ranges is None:
            raise ValueError("Invalid value for `jitter_ranges`, must not be `None`")  # noqa: E501

        self._jitter_ranges = jitter_ranges

    @property
    def throughput_ranges(self) -> ZoneRegisteredDataZoneServiceLevelObjsInfoThroughputRanges:
        """Gets the throughput_ranges of this ZoneRegisteredDataZoneServiceLevelObjsInfo.


        :return: The throughput_ranges of this ZoneRegisteredDataZoneServiceLevelObjsInfo.
        :rtype: ZoneRegisteredDataZoneServiceLevelObjsInfoThroughputRanges
        """
        return self._throughput_ranges

    @throughput_ranges.setter
    def throughput_ranges(self, throughput_ranges: ZoneRegisteredDataZoneServiceLevelObjsInfoThroughputRanges):
        """Sets the throughput_ranges of this ZoneRegisteredDataZoneServiceLevelObjsInfo.


        :param throughput_ranges: The throughput_ranges of this ZoneRegisteredDataZoneServiceLevelObjsInfo.
        :type throughput_ranges: ZoneRegisteredDataZoneServiceLevelObjsInfoThroughputRanges
        """
        if throughput_ranges is None:
            raise ValueError("Invalid value for `throughput_ranges`, must not be `None`")  # noqa: E501

        self._throughput_ranges = throughput_ranges
