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
from models.country_code import CountryCode  # noqa: F401,E501
from models.federation_context_id import FederationContextId  # noqa: F401,E501
from models.federation_identifier import FederationIdentifier  # noqa: F401,E501
from models.fixed_network_ids import FixedNetworkIds  # noqa: F401,E501
from models.mobile_network_ids import MobileNetworkIds  # noqa: F401,E501
from models.service_endpoint import ServiceEndpoint  # noqa: F401,E501
from models.zone_details import ZoneDetails  # noqa: F401,E501
import re  # noqa: F401,E501
import util


class FederationResponseData(Model):
    def __init__(self, partner_op_federation_id: FederationIdentifier=None, partner_op_country_code: CountryCode=None, federation_context_id: FederationContextId=None, edge_discovery_service_end_point: ServiceEndpoint=None, lcm_service_end_point: ServiceEndpoint=None, partner_op_mobile_network_codes: MobileNetworkIds=None, partner_op_fixed_network_codes: FixedNetworkIds=None, offered_availability_zones: List[ZoneDetails]=None, platform_caps: List[str]=None):  # noqa: E501
        """FederationResponseData - a model defined in Swagger

        :param partner_op_federation_id: The partner_op_federation_id of this FederationResponseData.  # noqa: E501
        :type partner_op_federation_id: FederationIdentifier
        :param partner_op_country_code: The partner_op_country_code of this FederationResponseData.  # noqa: E501
        :type partner_op_country_code: CountryCode
        :param federation_context_id: The federation_context_id of this FederationResponseData.  # noqa: E501
        :type federation_context_id: FederationContextId
        :param edge_discovery_service_end_point: The edge_discovery_service_end_point of this FederationResponseData.  # noqa: E501
        :type edge_discovery_service_end_point: ServiceEndpoint
        :param lcm_service_end_point: The lcm_service_end_point of this FederationResponseData.  # noqa: E501
        :type lcm_service_end_point: ServiceEndpoint
        :param partner_op_mobile_network_codes: The partner_op_mobile_network_codes of this FederationResponseData.  # noqa: E501
        :type partner_op_mobile_network_codes: MobileNetworkIds
        :param partner_op_fixed_network_codes: The partner_op_fixed_network_codes of this FederationResponseData.  # noqa: E501
        :type partner_op_fixed_network_codes: FixedNetworkIds
        :param offered_availability_zones: The offered_availability_zones of this FederationResponseData.  # noqa: E501
        :type offered_availability_zones: List[ZoneDetails]
        :param platform_caps: The platform_caps of this FederationResponseData.  # noqa: E501
        :type platform_caps: List[str]
        """
        self.swagger_types = {
            'partner_op_federation_id': FederationIdentifier,
            'partner_op_country_code': CountryCode,
            'federation_context_id': FederationContextId,
            'edge_discovery_service_end_point': ServiceEndpoint,
            'lcm_service_end_point': ServiceEndpoint,
            'partner_op_mobile_network_codes': MobileNetworkIds,
            'partner_op_fixed_network_codes': FixedNetworkIds,
            'offered_availability_zones': List[ZoneDetails],
            'platform_caps': List[str]
        }

        self.attribute_map = {
            'partner_op_federation_id': 'partnerOPFederationId',
            'partner_op_country_code': 'partnerOPCountryCode',
            'federation_context_id': 'federationContextId',
            'edge_discovery_service_end_point': 'edgeDiscoveryServiceEndPoint',
            'lcm_service_end_point': 'lcmServiceEndPoint',
            'partner_op_mobile_network_codes': 'partnerOPMobileNetworkCodes',
            'partner_op_fixed_network_codes': 'partnerOPFixedNetworkCodes',
            'offered_availability_zones': 'offeredAvailabilityZones',
            'platform_caps': 'platformCaps'
        }
        self._partner_op_federation_id = partner_op_federation_id
        self._partner_op_country_code = partner_op_country_code
        self._federation_context_id = federation_context_id
        self._edge_discovery_service_end_point = edge_discovery_service_end_point
        self._lcm_service_end_point = lcm_service_end_point
        self._partner_op_mobile_network_codes = partner_op_mobile_network_codes
        self._partner_op_fixed_network_codes = partner_op_fixed_network_codes
        self._offered_availability_zones = offered_availability_zones
        self._platform_caps = platform_caps

    @classmethod
    def from_dict(cls, dikt) -> 'FederationResponseData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FederationResponseData of this FederationResponseData.  # noqa: E501
        :rtype: FederationResponseData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def partner_op_federation_id(self) -> FederationIdentifier:
        """Gets the partner_op_federation_id of this FederationResponseData.


        :return: The partner_op_federation_id of this FederationResponseData.
        :rtype: FederationIdentifier
        """
        return self._partner_op_federation_id

    @partner_op_federation_id.setter
    def partner_op_federation_id(self, partner_op_federation_id: FederationIdentifier):
        """Sets the partner_op_federation_id of this FederationResponseData.


        :param partner_op_federation_id: The partner_op_federation_id of this FederationResponseData.
        :type partner_op_federation_id: FederationIdentifier
        """
        if partner_op_federation_id is None:
            raise ValueError("Invalid value for `partner_op_federation_id`, must not be `None`")  # noqa: E501

        self._partner_op_federation_id = partner_op_federation_id

    @property
    def partner_op_country_code(self) -> CountryCode:
        """Gets the partner_op_country_code of this FederationResponseData.


        :return: The partner_op_country_code of this FederationResponseData.
        :rtype: CountryCode
        """
        return self._partner_op_country_code

    @partner_op_country_code.setter
    def partner_op_country_code(self, partner_op_country_code: CountryCode):
        """Sets the partner_op_country_code of this FederationResponseData.


        :param partner_op_country_code: The partner_op_country_code of this FederationResponseData.
        :type partner_op_country_code: CountryCode
        """

        self._partner_op_country_code = partner_op_country_code

    @property
    def federation_context_id(self) -> FederationContextId:
        """Gets the federation_context_id of this FederationResponseData.


        :return: The federation_context_id of this FederationResponseData.
        :rtype: FederationContextId
        """
        return self._federation_context_id

    @federation_context_id.setter
    def federation_context_id(self, federation_context_id: FederationContextId):
        """Sets the federation_context_id of this FederationResponseData.


        :param federation_context_id: The federation_context_id of this FederationResponseData.
        :type federation_context_id: FederationContextId
        """
        if federation_context_id is None:
            raise ValueError("Invalid value for `federation_context_id`, must not be `None`")  # noqa: E501

        self._federation_context_id = federation_context_id

    @property
    def edge_discovery_service_end_point(self) -> ServiceEndpoint:
        """Gets the edge_discovery_service_end_point of this FederationResponseData.


        :return: The edge_discovery_service_end_point of this FederationResponseData.
        :rtype: ServiceEndpoint
        """
        return self._edge_discovery_service_end_point

    @edge_discovery_service_end_point.setter
    def edge_discovery_service_end_point(self, edge_discovery_service_end_point: ServiceEndpoint):
        """Sets the edge_discovery_service_end_point of this FederationResponseData.


        :param edge_discovery_service_end_point: The edge_discovery_service_end_point of this FederationResponseData.
        :type edge_discovery_service_end_point: ServiceEndpoint
        """

        self._edge_discovery_service_end_point = edge_discovery_service_end_point

    @property
    def lcm_service_end_point(self) -> ServiceEndpoint:
        """Gets the lcm_service_end_point of this FederationResponseData.


        :return: The lcm_service_end_point of this FederationResponseData.
        :rtype: ServiceEndpoint
        """
        return self._lcm_service_end_point

    @lcm_service_end_point.setter
    def lcm_service_end_point(self, lcm_service_end_point: ServiceEndpoint):
        """Sets the lcm_service_end_point of this FederationResponseData.


        :param lcm_service_end_point: The lcm_service_end_point of this FederationResponseData.
        :type lcm_service_end_point: ServiceEndpoint
        """

        self._lcm_service_end_point = lcm_service_end_point

    @property
    def partner_op_mobile_network_codes(self) -> MobileNetworkIds:
        """Gets the partner_op_mobile_network_codes of this FederationResponseData.


        :return: The partner_op_mobile_network_codes of this FederationResponseData.
        :rtype: MobileNetworkIds
        """
        return self._partner_op_mobile_network_codes

    @partner_op_mobile_network_codes.setter
    def partner_op_mobile_network_codes(self, partner_op_mobile_network_codes: MobileNetworkIds):
        """Sets the partner_op_mobile_network_codes of this FederationResponseData.


        :param partner_op_mobile_network_codes: The partner_op_mobile_network_codes of this FederationResponseData.
        :type partner_op_mobile_network_codes: MobileNetworkIds
        """

        self._partner_op_mobile_network_codes = partner_op_mobile_network_codes

    @property
    def partner_op_fixed_network_codes(self) -> FixedNetworkIds:
        """Gets the partner_op_fixed_network_codes of this FederationResponseData.


        :return: The partner_op_fixed_network_codes of this FederationResponseData.
        :rtype: FixedNetworkIds
        """
        return self._partner_op_fixed_network_codes

    @partner_op_fixed_network_codes.setter
    def partner_op_fixed_network_codes(self, partner_op_fixed_network_codes: FixedNetworkIds):
        """Sets the partner_op_fixed_network_codes of this FederationResponseData.


        :param partner_op_fixed_network_codes: The partner_op_fixed_network_codes of this FederationResponseData.
        :type partner_op_fixed_network_codes: FixedNetworkIds
        """

        self._partner_op_fixed_network_codes = partner_op_fixed_network_codes

    @property
    def offered_availability_zones(self) -> List[ZoneDetails]:
        """Gets the offered_availability_zones of this FederationResponseData.

        List of zones, which the operator platform wishes to make available to developers/ISVs of requesting operator platform.  # noqa: E501

        :return: The offered_availability_zones of this FederationResponseData.
        :rtype: List[ZoneDetails]
        """
        return self._offered_availability_zones

    @offered_availability_zones.setter
    def offered_availability_zones(self, offered_availability_zones: List[ZoneDetails]):
        """Sets the offered_availability_zones of this FederationResponseData.

        List of zones, which the operator platform wishes to make available to developers/ISVs of requesting operator platform.  # noqa: E501

        :param offered_availability_zones: The offered_availability_zones of this FederationResponseData.
        :type offered_availability_zones: List[ZoneDetails]
        """

        self._offered_availability_zones = offered_availability_zones

    @property
    def platform_caps(self) -> List[str]:
        """Gets the platform_caps of this FederationResponseData.


        :return: The platform_caps of this FederationResponseData.
        :rtype: List[str]
        """
        return self._platform_caps

    @platform_caps.setter
    def platform_caps(self, platform_caps: List[str]):
        """Sets the platform_caps of this FederationResponseData.


        :param platform_caps: The platform_caps of this FederationResponseData.
        :type platform_caps: List[str]
        """
        allowed_values = ["homeRouting", "Anchoring", "serviceAPIs", "faultMgmt", "eventMgmt", "resourceMonitor"]  # noqa: E501
        if not set(platform_caps).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `platform_caps` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(platform_caps) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._platform_caps = platform_caps
