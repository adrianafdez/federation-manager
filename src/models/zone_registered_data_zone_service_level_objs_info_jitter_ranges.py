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


class ZoneRegisteredDataZoneServiceLevelObjsInfoJitterRanges(Model):
    def __init__(self, min_jitter: int=None, max_jitter: int=None):  # noqa: E501
        """ZoneRegisteredDataZoneServiceLevelObjsInfoJitterRanges - a model defined in Swagger

        :param min_jitter: The min_jitter of this ZoneRegisteredDataZoneServiceLevelObjsInfoJitterRanges.  # noqa: E501
        :type min_jitter: int
        :param max_jitter: The max_jitter of this ZoneRegisteredDataZoneServiceLevelObjsInfoJitterRanges.  # noqa: E501
        :type max_jitter: int
        """
        self.swagger_types = {
            'min_jitter': int,
            'max_jitter': int
        }

        self.attribute_map = {
            'min_jitter': 'minJitter',
            'max_jitter': 'maxJitter'
        }
        self._min_jitter = min_jitter
        self._max_jitter = max_jitter

    @classmethod
    def from_dict(cls, dikt) -> 'ZoneRegisteredDataZoneServiceLevelObjsInfoJitterRanges':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ZoneRegisteredData_zoneServiceLevelObjsInfo_jitterRanges of this ZoneRegisteredDataZoneServiceLevelObjsInfoJitterRanges.  # noqa: E501
        :rtype: ZoneRegisteredDataZoneServiceLevelObjsInfoJitterRanges
        """
        return util.deserialize_model(dikt, cls)

    @property
    def min_jitter(self) -> int:
        """Gets the min_jitter of this ZoneRegisteredDataZoneServiceLevelObjsInfoJitterRanges.


        :return: The min_jitter of this ZoneRegisteredDataZoneServiceLevelObjsInfoJitterRanges.
        :rtype: int
        """
        return self._min_jitter

    @min_jitter.setter
    def min_jitter(self, min_jitter: int):
        """Sets the min_jitter of this ZoneRegisteredDataZoneServiceLevelObjsInfoJitterRanges.


        :param min_jitter: The min_jitter of this ZoneRegisteredDataZoneServiceLevelObjsInfoJitterRanges.
        :type min_jitter: int
        """

        self._min_jitter = min_jitter

    @property
    def max_jitter(self) -> int:
        """Gets the max_jitter of this ZoneRegisteredDataZoneServiceLevelObjsInfoJitterRanges.

        The maximum limit of network jitter between UC and Edge App in milli seconds.  # noqa: E501

        :return: The max_jitter of this ZoneRegisteredDataZoneServiceLevelObjsInfoJitterRanges.
        :rtype: int
        """
        return self._max_jitter

    @max_jitter.setter
    def max_jitter(self, max_jitter: int):
        """Sets the max_jitter of this ZoneRegisteredDataZoneServiceLevelObjsInfoJitterRanges.

        The maximum limit of network jitter between UC and Edge App in milli seconds.  # noqa: E501

        :param max_jitter: The max_jitter of this ZoneRegisteredDataZoneServiceLevelObjsInfoJitterRanges.
        :type max_jitter: int
        """

        self._max_jitter = max_jitter
