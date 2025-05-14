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
from models.zone_registered_data import ZoneRegisteredData  # noqa: F401,E501
import util


class ZoneRegistrationResponseData(Model):
    def __init__(self, accepted_zone_resource_info: List[ZoneRegisteredData]=None):  # noqa: E501
        """ZoneRegistrationResponseData - a model defined in Swagger

        :param accepted_zone_resource_info: The accepted_zone_resource_info of this ZoneRegistrationResponseData.  # noqa: E501
        :type accepted_zone_resource_info: List[ZoneRegisteredData]
        """
        self.swagger_types = {
            'accepted_zone_resource_info': List[ZoneRegisteredData]
        }

        self.attribute_map = {
            'accepted_zone_resource_info': 'acceptedZoneResourceInfo'
        }
        self._accepted_zone_resource_info = accepted_zone_resource_info

    @classmethod
    def from_dict(cls, dikt) -> 'ZoneRegistrationResponseData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ZoneRegistrationResponseData of this ZoneRegistrationResponseData.  # noqa: E501
        :rtype: ZoneRegistrationResponseData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def accepted_zone_resource_info(self) -> List[ZoneRegisteredData]:
        """Gets the accepted_zone_resource_info of this ZoneRegistrationResponseData.


        :return: The accepted_zone_resource_info of this ZoneRegistrationResponseData.
        :rtype: List[ZoneRegisteredData]
        """
        return self._accepted_zone_resource_info

    @accepted_zone_resource_info.setter
    def accepted_zone_resource_info(self, accepted_zone_resource_info: List[ZoneRegisteredData]):
        """Sets the accepted_zone_resource_info of this ZoneRegistrationResponseData.


        :param accepted_zone_resource_info: The accepted_zone_resource_info of this ZoneRegistrationResponseData.
        :type accepted_zone_resource_info: List[ZoneRegisteredData]
        """
        if accepted_zone_resource_info is None:
            raise ValueError("Invalid value for `accepted_zone_resource_info`, must not be `None`")  # noqa: E501

        self._accepted_zone_resource_info = accepted_zone_resource_info
