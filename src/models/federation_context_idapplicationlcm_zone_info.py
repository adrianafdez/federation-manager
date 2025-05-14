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
from models.flavour_id import FlavourId  # noqa: F401,E501
from models.zone_identifier import ZoneIdentifier  # noqa: F401,E501
import re  # noqa: F401,E501
import util


class FederationContextIdapplicationlcmZoneInfo(Model):
    def __init__(self, zone_id: ZoneIdentifier=None, flavour_id: FlavourId=None, resource_consumption: str='RESERVED_RES_AVOID', res_pool: str=None):  # noqa: E501
        """FederationContextIdapplicationlcmZoneInfo - a model defined in Swagger

        :param zone_id: The zone_id of this FederationContextIdapplicationlcmZoneInfo.  # noqa: E501
        :type zone_id: ZoneIdentifier
        :param flavour_id: The flavour_id of this FederationContextIdapplicationlcmZoneInfo.  # noqa: E501
        :type flavour_id: FlavourId
        :param resource_consumption: The resource_consumption of this FederationContextIdapplicationlcmZoneInfo.  # noqa: E501
        :type resource_consumption: str
        :param res_pool: The res_pool of this FederationContextIdapplicationlcmZoneInfo.  # noqa: E501
        :type res_pool: str
        """
        self.swagger_types = {
            'zone_id': ZoneIdentifier,
            'flavour_id': FlavourId,
            'resource_consumption': str,
            'res_pool': str
        }

        self.attribute_map = {
            'zone_id': 'zoneId',
            'flavour_id': 'flavourId',
            'resource_consumption': 'resourceConsumption',
            'res_pool': 'resPool'
        }
        self._zone_id = zone_id
        self._flavour_id = flavour_id
        self._resource_consumption = resource_consumption
        self._res_pool = res_pool

    @classmethod
    def from_dict(cls, dikt) -> 'FederationContextIdapplicationlcmZoneInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The federationContextIdapplicationlcm_zoneInfo of this FederationContextIdapplicationlcmZoneInfo.  # noqa: E501
        :rtype: FederationContextIdapplicationlcmZoneInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def zone_id(self) -> ZoneIdentifier:
        """Gets the zone_id of this FederationContextIdapplicationlcmZoneInfo.


        :return: The zone_id of this FederationContextIdapplicationlcmZoneInfo.
        :rtype: ZoneIdentifier
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id: ZoneIdentifier):
        """Sets the zone_id of this FederationContextIdapplicationlcmZoneInfo.


        :param zone_id: The zone_id of this FederationContextIdapplicationlcmZoneInfo.
        :type zone_id: ZoneIdentifier
        """
        if zone_id is None:
            raise ValueError("Invalid value for `zone_id`, must not be `None`")  # noqa: E501

        if zone_id != "":
            pattern = re.compile("^[A-Za-z0-9][A-Za-z0-9-]*$")
            if not re.fullmatch(pattern, zone_id):
                raise ValueError("'' does not match '^[A-Za-z0-9][A-Za-z0-9-]*$' - 'zoneInfo.zoneId'")

        self._zone_id = zone_id

    @property
    def flavour_id(self) -> FlavourId:
        """Gets the flavour_id of this FederationContextIdapplicationlcmZoneInfo.


        :return: The flavour_id of this FederationContextIdapplicationlcmZoneInfo.
        :rtype: FlavourId
        """
        return self._flavour_id

    @flavour_id.setter
    def flavour_id(self, flavour_id: FlavourId):
        """Sets the flavour_id of this FederationContextIdapplicationlcmZoneInfo.


        :param flavour_id: The flavour_id of this FederationContextIdapplicationlcmZoneInfo.
        :type flavour_id: FlavourId
        """
        if flavour_id is None:
            raise ValueError("Invalid value for `flavour_id`, must not be `None`")  # noqa: E501

        self._flavour_id = flavour_id

    @property
    def resource_consumption(self) -> str:
        """Gets the resource_consumption of this FederationContextIdapplicationlcmZoneInfo.

        Specifies if the application can be instantiated using pre-reserved resource or not.  App provider can pre-reserve a pool of compute resource on each zone.  'RESERVED_RES_SHALL' instruct OP to use only the pre-reserved resources. 'RESERVED_RES_PREFER' instruct to first try using pre-reserved resource, if none available go for non-reserved resources. 'RESERVED_RES_AVOID' instruct OP not to use pre-reserved resource if possible, it is a choice depending upon circumstances 'RESERVED_RES_FORBID' instruct OP not to use pre-reserved resources.  # noqa: E501

        :return: The resource_consumption of this FederationContextIdapplicationlcmZoneInfo.
        :rtype: str
        """
        return self._resource_consumption

    @resource_consumption.setter
    def resource_consumption(self, resource_consumption: str):
        """Sets the resource_consumption of this FederationContextIdapplicationlcmZoneInfo.

        Specifies if the application can be instantiated using pre-reserved resource or not.  App provider can pre-reserve a pool of compute resource on each zone.  'RESERVED_RES_SHALL' instruct OP to use only the pre-reserved resources. 'RESERVED_RES_PREFER' instruct to first try using pre-reserved resource, if none available go for non-reserved resources. 'RESERVED_RES_AVOID' instruct OP not to use pre-reserved resource if possible, it is a choice depending upon circumstances 'RESERVED_RES_FORBID' instruct OP not to use pre-reserved resources.  # noqa: E501

        :param resource_consumption: The resource_consumption of this FederationContextIdapplicationlcmZoneInfo.
        :type resource_consumption: str
        """
        allowed_values = ["RESERVED_RES_SHALL", "RESERVED_RES_PREFER", "RESERVED_RES_AVOID", "RESERVED_RES_FORBID"]  # noqa: E501
        if resource_consumption not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_consumption` ({0}), must be one of {1}"
                .format(resource_consumption, allowed_values)
            )

        self._resource_consumption = resource_consumption

    @property
    def res_pool(self) -> str:
        """Gets the res_pool of this FederationContextIdapplicationlcmZoneInfo.

        Resource pool to be used for application instantiation on this zone.  Valid only if IE 'resourceConsumption' is set to 'RESERVED_RES_SHALL' or 'RESERVED_RES_PREFER'  # noqa: E501

        :return: The res_pool of this FederationContextIdapplicationlcmZoneInfo.
        :rtype: str
        """
        return self._res_pool

    @res_pool.setter
    def res_pool(self, res_pool: str):
        """Sets the res_pool of this FederationContextIdapplicationlcmZoneInfo.

        Resource pool to be used for application instantiation on this zone.  Valid only if IE 'resourceConsumption' is set to 'RESERVED_RES_SHALL' or 'RESERVED_RES_PREFER'  # noqa: E501

        :param res_pool: The res_pool of this FederationContextIdapplicationlcmZoneInfo.
        :type res_pool: str
        """

        self._res_pool = res_pool
