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


class ZoneRegisteredDataNetworkResources(Model):
    def __init__(self, egress_band_width: int=None, dedicated_nic: int=None, support_sriov: bool=None, support_dpdk: bool=None):  # noqa: E501
        """ZoneRegisteredDataNetworkResources - a model defined in Swagger

        :param egress_band_width: The egress_band_width of this ZoneRegisteredDataNetworkResources.  # noqa: E501
        :type egress_band_width: int
        :param dedicated_nic: The dedicated_nic of this ZoneRegisteredDataNetworkResources.  # noqa: E501
        :type dedicated_nic: int
        :param support_sriov: The support_sriov of this ZoneRegisteredDataNetworkResources.  # noqa: E501
        :type support_sriov: bool
        :param support_dpdk: The support_dpdk of this ZoneRegisteredDataNetworkResources.  # noqa: E501
        :type support_dpdk: bool
        """
        self.swagger_types = {
            'egress_band_width': int,
            'dedicated_nic': int,
            'support_sriov': bool,
            'support_dpdk': bool
        }

        self.attribute_map = {
            'egress_band_width': 'egressBandWidth',
            'dedicated_nic': 'dedicatedNIC',
            'support_sriov': 'supportSriov',
            'support_dpdk': 'supportDPDK'
        }
        self._egress_band_width = egress_band_width
        self._dedicated_nic = dedicated_nic
        self._support_sriov = support_sriov
        self._support_dpdk = support_dpdk

    @classmethod
    def from_dict(cls, dikt) -> 'ZoneRegisteredDataNetworkResources':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ZoneRegisteredData_networkResources of this ZoneRegisteredDataNetworkResources.  # noqa: E501
        :rtype: ZoneRegisteredDataNetworkResources
        """
        return util.deserialize_model(dikt, cls)

    @property
    def egress_band_width(self) -> int:
        """Gets the egress_band_width of this ZoneRegisteredDataNetworkResources.

        Max dl throughput that this edge can offer. It is defined in Mbps.  # noqa: E501

        :return: The egress_band_width of this ZoneRegisteredDataNetworkResources.
        :rtype: int
        """
        return self._egress_band_width

    @egress_band_width.setter
    def egress_band_width(self, egress_band_width: int):
        """Sets the egress_band_width of this ZoneRegisteredDataNetworkResources.

        Max dl throughput that this edge can offer. It is defined in Mbps.  # noqa: E501

        :param egress_band_width: The egress_band_width of this ZoneRegisteredDataNetworkResources.
        :type egress_band_width: int
        """
        if egress_band_width is None:
            raise ValueError("Invalid value for `egress_band_width`, must not be `None`")  # noqa: E501

        self._egress_band_width = egress_band_width

    @property
    def dedicated_nic(self) -> int:
        """Gets the dedicated_nic of this ZoneRegisteredDataNetworkResources.

        Number of network interface cards which can be dedicatedly assigned to application pods on isolated networks. This includes virtual as well physical NICs  # noqa: E501

        :return: The dedicated_nic of this ZoneRegisteredDataNetworkResources.
        :rtype: int
        """
        return self._dedicated_nic

    @dedicated_nic.setter
    def dedicated_nic(self, dedicated_nic: int):
        """Sets the dedicated_nic of this ZoneRegisteredDataNetworkResources.

        Number of network interface cards which can be dedicatedly assigned to application pods on isolated networks. This includes virtual as well physical NICs  # noqa: E501

        :param dedicated_nic: The dedicated_nic of this ZoneRegisteredDataNetworkResources.
        :type dedicated_nic: int
        """
        if dedicated_nic is None:
            raise ValueError("Invalid value for `dedicated_nic`, must not be `None`")  # noqa: E501

        self._dedicated_nic = dedicated_nic

    @property
    def support_sriov(self) -> bool:
        """Gets the support_sriov of this ZoneRegisteredDataNetworkResources.

        If this zone support SRIOV networks or not  # noqa: E501

        :return: The support_sriov of this ZoneRegisteredDataNetworkResources.
        :rtype: bool
        """
        return self._support_sriov

    @support_sriov.setter
    def support_sriov(self, support_sriov: bool):
        """Sets the support_sriov of this ZoneRegisteredDataNetworkResources.

        If this zone support SRIOV networks or not  # noqa: E501

        :param support_sriov: The support_sriov of this ZoneRegisteredDataNetworkResources.
        :type support_sriov: bool
        """
        if support_sriov is None:
            raise ValueError("Invalid value for `support_sriov`, must not be `None`")  # noqa: E501

        self._support_sriov = support_sriov

    @property
    def support_dpdk(self) -> bool:
        """Gets the support_dpdk of this ZoneRegisteredDataNetworkResources.

        If this zone supports DPDK based networking.  # noqa: E501

        :return: The support_dpdk of this ZoneRegisteredDataNetworkResources.
        :rtype: bool
        """
        return self._support_dpdk

    @support_dpdk.setter
    def support_dpdk(self, support_dpdk: bool):
        """Sets the support_dpdk of this ZoneRegisteredDataNetworkResources.

        If this zone supports DPDK based networking.  # noqa: E501

        :param support_dpdk: The support_dpdk of this ZoneRegisteredDataNetworkResources.
        :type support_dpdk: bool
        """
        if support_dpdk is None:
            raise ValueError("Invalid value for `support_dpdk`, must not be `None`")  # noqa: E501

        self._support_dpdk = support_dpdk
