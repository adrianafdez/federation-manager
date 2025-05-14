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
from models.uri import Uri  # noqa: F401,E501
from models.zone_identifier import ZoneIdentifier  # noqa: F401,E501
import util


class ZoneRegistrationRequestData(Model):
    def __init__(self, accepted_availability_zones: List[ZoneIdentifier]=None, avail_zone_notif_link: Uri=None):  # noqa: E501
        """ZoneRegistrationRequestData - a model defined in Swagger

        :param accepted_availability_zones: The accepted_availability_zones of this ZoneRegistrationRequestData.  # noqa: E501
        :type accepted_availability_zones: List[ZoneIdentifier]
        :param avail_zone_notif_link: The avail_zone_notif_link of this ZoneRegistrationRequestData.  # noqa: E501
        :type avail_zone_notif_link: Uri
        """
        self.swagger_types = {
            'accepted_availability_zones': List[ZoneIdentifier],
            'avail_zone_notif_link': Uri
        }

        self.attribute_map = {
            'accepted_availability_zones': 'acceptedAvailabilityZones',
            'avail_zone_notif_link': 'availZoneNotifLink'
        }
        self._accepted_availability_zones = accepted_availability_zones
        self._avail_zone_notif_link = avail_zone_notif_link

    @classmethod
    def from_dict(cls, dikt) -> 'ZoneRegistrationRequestData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ZoneRegistrationRequestData of this ZoneRegistrationRequestData.  # noqa: E501
        :rtype: ZoneRegistrationRequestData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def accepted_availability_zones(self) -> List[ZoneIdentifier]:
        """Gets the accepted_availability_zones of this ZoneRegistrationRequestData.


        :return: The accepted_availability_zones of this ZoneRegistrationRequestData.
        :rtype: List[ZoneIdentifier]
        """
        return self._accepted_availability_zones

    @accepted_availability_zones.setter
    def accepted_availability_zones(self, accepted_availability_zones: List[ZoneIdentifier]):
        """Sets the accepted_availability_zones of this ZoneRegistrationRequestData.


        :param accepted_availability_zones: The accepted_availability_zones of this ZoneRegistrationRequestData.
        :type accepted_availability_zones: List[ZoneIdentifier]
        """
        if accepted_availability_zones is None:
            raise ValueError("Invalid value for `accepted_availability_zones`, must not be `None`")  # noqa: E501

        self._accepted_availability_zones = accepted_availability_zones

    @property
    def avail_zone_notif_link(self) -> Uri:
        """Gets the avail_zone_notif_link of this ZoneRegistrationRequestData.


        :return: The avail_zone_notif_link of this ZoneRegistrationRequestData.
        :rtype: Uri
        """
        return self._avail_zone_notif_link

    @avail_zone_notif_link.setter
    def avail_zone_notif_link(self, avail_zone_notif_link: Uri):
        """Sets the avail_zone_notif_link of this ZoneRegistrationRequestData.


        :param avail_zone_notif_link: The avail_zone_notif_link of this ZoneRegistrationRequestData.
        :type avail_zone_notif_link: Uri
        """
        if avail_zone_notif_link is None:
            raise ValueError("Invalid value for `avail_zone_notif_link`, must not be `None`")  # noqa: E501

        self._avail_zone_notif_link = avail_zone_notif_link
