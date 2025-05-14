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
from models.fixed_network_ids import FixedNetworkIds  # noqa: F401,E501
from models.mobile_network_ids import MobileNetworkIds  # noqa: F401,E501
from models.service_endpoint import ServiceEndpoint  # noqa: F401,E501
from models.zone_details import ZoneDetails  # noqa: F401,E501
import util


class InlineResponse2001(Model):
    def __init__(self, edge_discovery_service_end_point: ServiceEndpoint=None, lcm_service_end_point: ServiceEndpoint=None, allowed_mobile_network_ids: MobileNetworkIds=None, allowed_fixed_network_ids: FixedNetworkIds=None, offered_availability_zones: List[ZoneDetails]=None):  # noqa: E501
        """InlineResponse2001 - a model defined in Swagger

        :param edge_discovery_service_end_point: The edge_discovery_service_end_point of this InlineResponse2001.  # noqa: E501
        :type edge_discovery_service_end_point: ServiceEndpoint
        :param lcm_service_end_point: The lcm_service_end_point of this InlineResponse2001.  # noqa: E501
        :type lcm_service_end_point: ServiceEndpoint
        :param allowed_mobile_network_ids: The allowed_mobile_network_ids of this InlineResponse2001.  # noqa: E501
        :type allowed_mobile_network_ids: MobileNetworkIds
        :param allowed_fixed_network_ids: The allowed_fixed_network_ids of this InlineResponse2001.  # noqa: E501
        :type allowed_fixed_network_ids: FixedNetworkIds
        :param offered_availability_zones: The offered_availability_zones of this InlineResponse2001.  # noqa: E501
        :type offered_availability_zones: List[ZoneDetails]
        """
        self.swagger_types = {
            'edge_discovery_service_end_point': ServiceEndpoint,
            'lcm_service_end_point': ServiceEndpoint,
            'allowed_mobile_network_ids': MobileNetworkIds,
            'allowed_fixed_network_ids': FixedNetworkIds,
            'offered_availability_zones': List[ZoneDetails]
        }

        self.attribute_map = {
            'edge_discovery_service_end_point': 'edgeDiscoveryServiceEndPoint',
            'lcm_service_end_point': 'lcmServiceEndPoint',
            'allowed_mobile_network_ids': 'allowedMobileNetworkIds',
            'allowed_fixed_network_ids': 'allowedFixedNetworkIds',
            'offered_availability_zones': 'offeredAvailabilityZones'
        }
        self._edge_discovery_service_end_point = edge_discovery_service_end_point
        self._lcm_service_end_point = lcm_service_end_point
        self._allowed_mobile_network_ids = allowed_mobile_network_ids
        self._allowed_fixed_network_ids = allowed_fixed_network_ids
        self._offered_availability_zones = offered_availability_zones

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2001':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_1 of this InlineResponse2001.  # noqa: E501
        :rtype: InlineResponse2001
        """
        return util.deserialize_model(dikt, cls)

    @property
    def edge_discovery_service_end_point(self) -> ServiceEndpoint:
        """Gets the edge_discovery_service_end_point of this InlineResponse2001.


        :return: The edge_discovery_service_end_point of this InlineResponse2001.
        :rtype: ServiceEndpoint
        """
        return self._edge_discovery_service_end_point

    @edge_discovery_service_end_point.setter
    def edge_discovery_service_end_point(self, edge_discovery_service_end_point: ServiceEndpoint):
        """Sets the edge_discovery_service_end_point of this InlineResponse2001.


        :param edge_discovery_service_end_point: The edge_discovery_service_end_point of this InlineResponse2001.
        :type edge_discovery_service_end_point: ServiceEndpoint
        """
        if edge_discovery_service_end_point is None:
            raise ValueError("Invalid value for `edge_discovery_service_end_point`, must not be `None`")  # noqa: E501

        self._edge_discovery_service_end_point = edge_discovery_service_end_point

    @property
    def lcm_service_end_point(self) -> ServiceEndpoint:
        """Gets the lcm_service_end_point of this InlineResponse2001.


        :return: The lcm_service_end_point of this InlineResponse2001.
        :rtype: ServiceEndpoint
        """
        return self._lcm_service_end_point

    @lcm_service_end_point.setter
    def lcm_service_end_point(self, lcm_service_end_point: ServiceEndpoint):
        """Sets the lcm_service_end_point of this InlineResponse2001.


        :param lcm_service_end_point: The lcm_service_end_point of this InlineResponse2001.
        :type lcm_service_end_point: ServiceEndpoint
        """
        if lcm_service_end_point is None:
            raise ValueError("Invalid value for `lcm_service_end_point`, must not be `None`")  # noqa: E501

        self._lcm_service_end_point = lcm_service_end_point

    @property
    def allowed_mobile_network_ids(self) -> MobileNetworkIds:
        """Gets the allowed_mobile_network_ids of this InlineResponse2001.


        :return: The allowed_mobile_network_ids of this InlineResponse2001.
        :rtype: MobileNetworkIds
        """
        return self._allowed_mobile_network_ids

    @allowed_mobile_network_ids.setter
    def allowed_mobile_network_ids(self, allowed_mobile_network_ids: MobileNetworkIds):
        """Sets the allowed_mobile_network_ids of this InlineResponse2001.


        :param allowed_mobile_network_ids: The allowed_mobile_network_ids of this InlineResponse2001.
        :type allowed_mobile_network_ids: MobileNetworkIds
        """

        self._allowed_mobile_network_ids = allowed_mobile_network_ids

    @property
    def allowed_fixed_network_ids(self) -> FixedNetworkIds:
        """Gets the allowed_fixed_network_ids of this InlineResponse2001.


        :return: The allowed_fixed_network_ids of this InlineResponse2001.
        :rtype: FixedNetworkIds
        """
        return self._allowed_fixed_network_ids

    @allowed_fixed_network_ids.setter
    def allowed_fixed_network_ids(self, allowed_fixed_network_ids: FixedNetworkIds):
        """Sets the allowed_fixed_network_ids of this InlineResponse2001.


        :param allowed_fixed_network_ids: The allowed_fixed_network_ids of this InlineResponse2001.
        :type allowed_fixed_network_ids: FixedNetworkIds
        """

        self._allowed_fixed_network_ids = allowed_fixed_network_ids

    @property
    def offered_availability_zones(self) -> List[ZoneDetails]:
        """Gets the offered_availability_zones of this InlineResponse2001.


        :return: The offered_availability_zones of this InlineResponse2001.
        :rtype: List[ZoneDetails]
        """
        return self._offered_availability_zones

    @offered_availability_zones.setter
    def offered_availability_zones(self, offered_availability_zones: List[ZoneDetails]):
        """Sets the offered_availability_zones of this InlineResponse2001.


        :param offered_availability_zones: The offered_availability_zones of this InlineResponse2001.
        :type offered_availability_zones: List[ZoneDetails]
        """

        self._offered_availability_zones = offered_availability_zones
