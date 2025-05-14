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
import util


class FederationContextIdPartnerBody(Model):
    def __init__(self, object_type: str=None, operation_type: str=None, add_mobile_network_ids: MobileNetworkIds=None, remove_mobile_network_ids: MobileNetworkIds=None, add_fixed_network_ids: FixedNetworkIds=None, remove_fixed_network_ids: FixedNetworkIds=None, modification_date: datetime=None):  # noqa: E501
        """FederationContextIdPartnerBody - a model defined in Swagger

        :param object_type: The object_type of this FederationContextIdPartnerBody.  # noqa: E501
        :type object_type: str
        :param operation_type: The operation_type of this FederationContextIdPartnerBody.  # noqa: E501
        :type operation_type: str
        :param add_mobile_network_ids: The add_mobile_network_ids of this FederationContextIdPartnerBody.  # noqa: E501
        :type add_mobile_network_ids: MobileNetworkIds
        :param remove_mobile_network_ids: The remove_mobile_network_ids of this FederationContextIdPartnerBody.  # noqa: E501
        :type remove_mobile_network_ids: MobileNetworkIds
        :param add_fixed_network_ids: The add_fixed_network_ids of this FederationContextIdPartnerBody.  # noqa: E501
        :type add_fixed_network_ids: FixedNetworkIds
        :param remove_fixed_network_ids: The remove_fixed_network_ids of this FederationContextIdPartnerBody.  # noqa: E501
        :type remove_fixed_network_ids: FixedNetworkIds
        :param modification_date: The modification_date of this FederationContextIdPartnerBody.  # noqa: E501
        :type modification_date: datetime
        """
        self.swagger_types = {
            'object_type': str,
            'operation_type': str,
            'add_mobile_network_ids': MobileNetworkIds,
            'remove_mobile_network_ids': MobileNetworkIds,
            'add_fixed_network_ids': FixedNetworkIds,
            'remove_fixed_network_ids': FixedNetworkIds,
            'modification_date': datetime
        }

        self.attribute_map = {
            'object_type': 'objectType',
            'operation_type': 'operationType',
            'add_mobile_network_ids': 'addMobileNetworkIds',
            'remove_mobile_network_ids': 'removeMobileNetworkIds',
            'add_fixed_network_ids': 'addFixedNetworkIds',
            'remove_fixed_network_ids': 'removeFixedNetworkIds',
            'modification_date': 'modificationDate'
        }
        self._object_type = object_type
        self._operation_type = operation_type
        self._add_mobile_network_ids = add_mobile_network_ids
        self._remove_mobile_network_ids = remove_mobile_network_ids
        self._add_fixed_network_ids = add_fixed_network_ids
        self._remove_fixed_network_ids = remove_fixed_network_ids
        self._modification_date = modification_date

    @classmethod
    def from_dict(cls, dikt) -> 'FederationContextIdPartnerBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The federationContextId_partner_body of this FederationContextIdPartnerBody.  # noqa: E501
        :rtype: FederationContextIdPartnerBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def object_type(self) -> str:
        """Gets the object_type of this FederationContextIdPartnerBody.


        :return: The object_type of this FederationContextIdPartnerBody.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type: str):
        """Sets the object_type of this FederationContextIdPartnerBody.


        :param object_type: The object_type of this FederationContextIdPartnerBody.
        :type object_type: str
        """
        allowed_values = ["MOBILE_NETWORK_CODES", "FIXED_NETWORK_CODES"]  # noqa: E501
        if object_type not in allowed_values:
            raise ValueError(
                "Invalid value for `object_type` ({0}), must be one of {1}"
                .format(object_type, allowed_values)
            )

        self._object_type = object_type

    @property
    def operation_type(self) -> str:
        """Gets the operation_type of this FederationContextIdPartnerBody.


        :return: The operation_type of this FederationContextIdPartnerBody.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type: str):
        """Sets the operation_type of this FederationContextIdPartnerBody.


        :param operation_type: The operation_type of this FederationContextIdPartnerBody.
        :type operation_type: str
        """
        allowed_values = ["ADD_CODES", "REMOVE_CODES", "UPDATE_CODES"]  # noqa: E501
        if operation_type not in allowed_values:
            raise ValueError(
                "Invalid value for `operation_type` ({0}), must be one of {1}"
                .format(operation_type, allowed_values)
            )

        self._operation_type = operation_type

    @property
    def add_mobile_network_ids(self) -> MobileNetworkIds:
        """Gets the add_mobile_network_ids of this FederationContextIdPartnerBody.


        :return: The add_mobile_network_ids of this FederationContextIdPartnerBody.
        :rtype: MobileNetworkIds
        """
        return self._add_mobile_network_ids

    @add_mobile_network_ids.setter
    def add_mobile_network_ids(self, add_mobile_network_ids: MobileNetworkIds):
        """Sets the add_mobile_network_ids of this FederationContextIdPartnerBody.


        :param add_mobile_network_ids: The add_mobile_network_ids of this FederationContextIdPartnerBody.
        :type add_mobile_network_ids: MobileNetworkIds
        """

        self._add_mobile_network_ids = add_mobile_network_ids

    @property
    def remove_mobile_network_ids(self) -> MobileNetworkIds:
        """Gets the remove_mobile_network_ids of this FederationContextIdPartnerBody.


        :return: The remove_mobile_network_ids of this FederationContextIdPartnerBody.
        :rtype: MobileNetworkIds
        """
        return self._remove_mobile_network_ids

    @remove_mobile_network_ids.setter
    def remove_mobile_network_ids(self, remove_mobile_network_ids: MobileNetworkIds):
        """Sets the remove_mobile_network_ids of this FederationContextIdPartnerBody.


        :param remove_mobile_network_ids: The remove_mobile_network_ids of this FederationContextIdPartnerBody.
        :type remove_mobile_network_ids: MobileNetworkIds
        """

        self._remove_mobile_network_ids = remove_mobile_network_ids

    @property
    def add_fixed_network_ids(self) -> FixedNetworkIds:
        """Gets the add_fixed_network_ids of this FederationContextIdPartnerBody.


        :return: The add_fixed_network_ids of this FederationContextIdPartnerBody.
        :rtype: FixedNetworkIds
        """
        return self._add_fixed_network_ids

    @add_fixed_network_ids.setter
    def add_fixed_network_ids(self, add_fixed_network_ids: FixedNetworkIds):
        """Sets the add_fixed_network_ids of this FederationContextIdPartnerBody.


        :param add_fixed_network_ids: The add_fixed_network_ids of this FederationContextIdPartnerBody.
        :type add_fixed_network_ids: FixedNetworkIds
        """

        self._add_fixed_network_ids = add_fixed_network_ids

    @property
    def remove_fixed_network_ids(self) -> FixedNetworkIds:
        """Gets the remove_fixed_network_ids of this FederationContextIdPartnerBody.


        :return: The remove_fixed_network_ids of this FederationContextIdPartnerBody.
        :rtype: FixedNetworkIds
        """
        return self._remove_fixed_network_ids

    @remove_fixed_network_ids.setter
    def remove_fixed_network_ids(self, remove_fixed_network_ids: FixedNetworkIds):
        """Sets the remove_fixed_network_ids of this FederationContextIdPartnerBody.


        :param remove_fixed_network_ids: The remove_fixed_network_ids of this FederationContextIdPartnerBody.
        :type remove_fixed_network_ids: FixedNetworkIds
        """

        self._remove_fixed_network_ids = remove_fixed_network_ids

    @property
    def modification_date(self) -> datetime:
        """Gets the modification_date of this FederationContextIdPartnerBody.

        Date and time of the federation modification by the originating partner OP  # noqa: E501

        :return: The modification_date of this FederationContextIdPartnerBody.
        :rtype: datetime
        """
        return self._modification_date

    @modification_date.setter
    def modification_date(self, modification_date: datetime):
        """Sets the modification_date of this FederationContextIdPartnerBody.

        Date and time of the federation modification by the originating partner OP  # noqa: E501

        :param modification_date: The modification_date of this FederationContextIdPartnerBody.
        :type modification_date: datetime
        """
        if modification_date is None:
            raise ValueError("Invalid value for `modification_date`, must not be `None`")  # noqa: E501

        self._modification_date = modification_date
