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
from models.compute_resource_info import ComputeResourceInfo  # noqa: F401,E501
from models.flavour import Flavour  # noqa: F401,E501
from models.zone_identifier import ZoneIdentifier  # noqa: F401,E501
from models.zone_registered_data_network_resources import ZoneRegisteredDataNetworkResources  # noqa: F401,E501
from models.zone_registered_data_zone_service_level_objs_info import ZoneRegisteredDataZoneServiceLevelObjsInfo  # noqa: F401,E501
import re  # noqa: F401,E501
import util


class ZoneRegisteredData(Model):
    def __init__(self, zone_id: ZoneIdentifier=None, reserved_compute_resources: List[ComputeResourceInfo]=None, compute_resource_quota_limits: List[ComputeResourceInfo]=None, flavours_supported: List[Flavour]=None, network_resources: ZoneRegisteredDataNetworkResources=None, zone_service_level_objs_info: ZoneRegisteredDataZoneServiceLevelObjsInfo=None):  # noqa: E501
        """ZoneRegisteredData - a model defined in Swagger

        :param zone_id: The zone_id of this ZoneRegisteredData.  # noqa: E501
        :type zone_id: ZoneIdentifier
        :param reserved_compute_resources: The reserved_compute_resources of this ZoneRegisteredData.  # noqa: E501
        :type reserved_compute_resources: List[ComputeResourceInfo]
        :param compute_resource_quota_limits: The compute_resource_quota_limits of this ZoneRegisteredData.  # noqa: E501
        :type compute_resource_quota_limits: List[ComputeResourceInfo]
        :param flavours_supported: The flavours_supported of this ZoneRegisteredData.  # noqa: E501
        :type flavours_supported: List[Flavour]
        :param network_resources: The network_resources of this ZoneRegisteredData.  # noqa: E501
        :type network_resources: ZoneRegisteredDataNetworkResources
        :param zone_service_level_objs_info: The zone_service_level_objs_info of this ZoneRegisteredData.  # noqa: E501
        :type zone_service_level_objs_info: ZoneRegisteredDataZoneServiceLevelObjsInfo
        """
        self.swagger_types = {
            'zone_id': ZoneIdentifier,
            'reserved_compute_resources': List[ComputeResourceInfo],
            'compute_resource_quota_limits': List[ComputeResourceInfo],
            'flavours_supported': List[Flavour],
            'network_resources': ZoneRegisteredDataNetworkResources,
            'zone_service_level_objs_info': ZoneRegisteredDataZoneServiceLevelObjsInfo
        }

        self.attribute_map = {
            'zone_id': 'zoneId',
            'reserved_compute_resources': 'reservedComputeResources',
            'compute_resource_quota_limits': 'computeResourceQuotaLimits',
            'flavours_supported': 'flavoursSupported',
            'network_resources': 'networkResources',
            'zone_service_level_objs_info': 'zoneServiceLevelObjsInfo'
        }
        self._zone_id = zone_id
        self._reserved_compute_resources = reserved_compute_resources
        self._compute_resource_quota_limits = compute_resource_quota_limits
        self._flavours_supported = flavours_supported
        self._network_resources = network_resources
        self._zone_service_level_objs_info = zone_service_level_objs_info

    @classmethod
    def from_dict(cls, dikt) -> 'ZoneRegisteredData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ZoneRegisteredData of this ZoneRegisteredData.  # noqa: E501
        :rtype: ZoneRegisteredData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def zone_id(self) -> ZoneIdentifier:
        """Gets the zone_id of this ZoneRegisteredData.


        :return: The zone_id of this ZoneRegisteredData.
        :rtype: ZoneIdentifier
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id: ZoneIdentifier):
        """Sets the zone_id of this ZoneRegisteredData.


        :param zone_id: The zone_id of this ZoneRegisteredData.
        :type zone_id: ZoneIdentifier
        """
        if zone_id is None:
            raise ValueError("Invalid value for `zone_id`, must not be `None`")  # noqa: E501

        self._zone_id = zone_id

    @property
    def reserved_compute_resources(self) -> List[ComputeResourceInfo]:
        """Gets the reserved_compute_resources of this ZoneRegisteredData.

        Resources exclusively reserved for the originator OP.  # noqa: E501

        :return: The reserved_compute_resources of this ZoneRegisteredData.
        :rtype: List[ComputeResourceInfo]
        """
        return self._reserved_compute_resources

    @reserved_compute_resources.setter
    def reserved_compute_resources(self, reserved_compute_resources: List[ComputeResourceInfo]):
        """Sets the reserved_compute_resources of this ZoneRegisteredData.

        Resources exclusively reserved for the originator OP.  # noqa: E501

        :param reserved_compute_resources: The reserved_compute_resources of this ZoneRegisteredData.
        :type reserved_compute_resources: List[ComputeResourceInfo]
        """
        if reserved_compute_resources is None:
            raise ValueError("Invalid value for `reserved_compute_resources`, must not be `None`")  # noqa: E501

        self._reserved_compute_resources = reserved_compute_resources

    @property
    def compute_resource_quota_limits(self) -> List[ComputeResourceInfo]:
        """Gets the compute_resource_quota_limits of this ZoneRegisteredData.

        Max quota on resources partner OP allows over reserved resources.  # noqa: E501

        :return: The compute_resource_quota_limits of this ZoneRegisteredData.
        :rtype: List[ComputeResourceInfo]
        """
        return self._compute_resource_quota_limits

    @compute_resource_quota_limits.setter
    def compute_resource_quota_limits(self, compute_resource_quota_limits: List[ComputeResourceInfo]):
        """Sets the compute_resource_quota_limits of this ZoneRegisteredData.

        Max quota on resources partner OP allows over reserved resources.  # noqa: E501

        :param compute_resource_quota_limits: The compute_resource_quota_limits of this ZoneRegisteredData.
        :type compute_resource_quota_limits: List[ComputeResourceInfo]
        """
        if compute_resource_quota_limits is None:
            raise ValueError("Invalid value for `compute_resource_quota_limits`, must not be `None`")  # noqa: E501

        self._compute_resource_quota_limits = compute_resource_quota_limits

    @property
    def flavours_supported(self) -> List[Flavour]:
        """Gets the flavours_supported of this ZoneRegisteredData.


        :return: The flavours_supported of this ZoneRegisteredData.
        :rtype: List[Flavour]
        """
        return self._flavours_supported

    @flavours_supported.setter
    def flavours_supported(self, flavours_supported: List[Flavour]):
        """Sets the flavours_supported of this ZoneRegisteredData.


        :param flavours_supported: The flavours_supported of this ZoneRegisteredData.
        :type flavours_supported: List[Flavour]
        """
        if flavours_supported is None:
            raise ValueError("Invalid value for `flavours_supported`, must not be `None`")  # noqa: E501

        self._flavours_supported = flavours_supported

    @property
    def network_resources(self) -> ZoneRegisteredDataNetworkResources:
        """Gets the network_resources of this ZoneRegisteredData.


        :return: The network_resources of this ZoneRegisteredData.
        :rtype: ZoneRegisteredDataNetworkResources
        """
        return self._network_resources

    @network_resources.setter
    def network_resources(self, network_resources: ZoneRegisteredDataNetworkResources):
        """Sets the network_resources of this ZoneRegisteredData.


        :param network_resources: The network_resources of this ZoneRegisteredData.
        :type network_resources: ZoneRegisteredDataNetworkResources
        """

        self._network_resources = network_resources

    @property
    def zone_service_level_objs_info(self) -> ZoneRegisteredDataZoneServiceLevelObjsInfo:
        """Gets the zone_service_level_objs_info of this ZoneRegisteredData.


        :return: The zone_service_level_objs_info of this ZoneRegisteredData.
        :rtype: ZoneRegisteredDataZoneServiceLevelObjsInfo
        """
        return self._zone_service_level_objs_info

    @zone_service_level_objs_info.setter
    def zone_service_level_objs_info(self, zone_service_level_objs_info: ZoneRegisteredDataZoneServiceLevelObjsInfo):
        """Sets the zone_service_level_objs_info of this ZoneRegisteredData.


        :param zone_service_level_objs_info: The zone_service_level_objs_info of this ZoneRegisteredData.
        :type zone_service_level_objs_info: ZoneRegisteredDataZoneServiceLevelObjsInfo
        """

        self._zone_service_level_objs_info = zone_service_level_objs_info
