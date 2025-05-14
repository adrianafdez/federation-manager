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
from models.callback_credentials import CallbackCredentials  # noqa: F401,E501
from models.country_code import CountryCode  # noqa: F401,E501
from models.federation_identifier import FederationIdentifier  # noqa: F401,E501
from models.fixed_network_ids import FixedNetworkIds  # noqa: F401,E501
from models.mobile_network_ids import MobileNetworkIds  # noqa: F401,E501
from models.uri import Uri  # noqa: F401,E501
import re  # noqa: F401,E501
import util


class FederationRequestData(Model):
    def __init__(self, orig_op_federation_id: FederationIdentifier=None, orig_op_country_code: CountryCode=None, orig_op_mobile_network_codes: MobileNetworkIds=None, orig_op_fixed_network_codes: FixedNetworkIds=None, initial_date: datetime=None, partner_status_link: Uri=None, partner_callback_credentials: CallbackCredentials=None):  # noqa: E501
        """FederationRequestData - a model defined in Swagger

        :param orig_op_federation_id: The orig_op_federation_id of this FederationRequestData.  # noqa: E501
        :type orig_op_federation_id: FederationIdentifier
        :param orig_op_country_code: The orig_op_country_code of this FederationRequestData.  # noqa: E501
        :type orig_op_country_code: CountryCode
        :param orig_op_mobile_network_codes: The orig_op_mobile_network_codes of this FederationRequestData.  # noqa: E501
        :type orig_op_mobile_network_codes: MobileNetworkIds
        :param orig_op_fixed_network_codes: The orig_op_fixed_network_codes of this FederationRequestData.  # noqa: E501
        :type orig_op_fixed_network_codes: FixedNetworkIds
        :param initial_date: The initial_date of this FederationRequestData.  # noqa: E501
        :type initial_date: datetime
        :param partner_status_link: The partner_status_link of this FederationRequestData.  # noqa: E501
        :type partner_status_link: Uri
        :param partner_callback_credentials: The partner_callback_credentials of this FederationRequestData.  # noqa: E501
        :type partner_callback_credentials: CallbackCredentials
        """
        self.swagger_types = {
            'orig_op_federation_id': FederationIdentifier,
            'orig_op_country_code': CountryCode,
            'orig_op_mobile_network_codes': MobileNetworkIds,
            'orig_op_fixed_network_codes': FixedNetworkIds,
            'initial_date': datetime,
            'partner_status_link': Uri,
            'partner_callback_credentials': CallbackCredentials
        }

        self.attribute_map = {
            'orig_op_federation_id': 'origOPFederationId',
            'orig_op_country_code': 'origOPCountryCode',
            'orig_op_mobile_network_codes': 'origOPMobileNetworkCodes',
            'orig_op_fixed_network_codes': 'origOPFixedNetworkCodes',
            'initial_date': 'initialDate',
            'partner_status_link': 'partnerStatusLink',
            'partner_callback_credentials': 'partnerCallbackCredentials'
        }
        self._orig_op_federation_id = orig_op_federation_id
        self._orig_op_country_code = orig_op_country_code
        self._orig_op_mobile_network_codes = orig_op_mobile_network_codes
        self._orig_op_fixed_network_codes = orig_op_fixed_network_codes
        self._initial_date = initial_date
        self._partner_status_link = partner_status_link
        self._partner_callback_credentials = partner_callback_credentials

    @classmethod
    def from_dict(cls, dikt) -> 'FederationRequestData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FederationRequestData of this FederationRequestData.  # noqa: E501
        :rtype: FederationRequestData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def orig_op_federation_id(self) -> FederationIdentifier:
        """Gets the orig_op_federation_id of this FederationRequestData.


        :return: The orig_op_federation_id of this FederationRequestData.
        :rtype: FederationIdentifier
        """
        return self._orig_op_federation_id

    @orig_op_federation_id.setter
    def orig_op_federation_id(self, orig_op_federation_id: FederationIdentifier):
        """Sets the orig_op_federation_id of this FederationRequestData.


        :param orig_op_federation_id: The orig_op_federation_id of this FederationRequestData.
        :type orig_op_federation_id: FederationIdentifier
        """
        if orig_op_federation_id is None:
            raise ValueError("Invalid value for `orig_op_federation_id`, must not be `None`")  # noqa: E501

        self._orig_op_federation_id = orig_op_federation_id

    @property
    def orig_op_country_code(self) -> CountryCode:
        """Gets the orig_op_country_code of this FederationRequestData.


        :return: The orig_op_country_code of this FederationRequestData.
        :rtype: CountryCode
        """
        return self._orig_op_country_code

    @orig_op_country_code.setter
    def orig_op_country_code(self, orig_op_country_code: CountryCode):
        """Sets the orig_op_country_code of this FederationRequestData.


        :param orig_op_country_code: The orig_op_country_code of this FederationRequestData.
        :type orig_op_country_code: CountryCode
        """

        self._orig_op_country_code = orig_op_country_code

    @property
    def orig_op_mobile_network_codes(self) -> MobileNetworkIds:
        """Gets the orig_op_mobile_network_codes of this FederationRequestData.


        :return: The orig_op_mobile_network_codes of this FederationRequestData.
        :rtype: MobileNetworkIds
        """
        return self._orig_op_mobile_network_codes

    @orig_op_mobile_network_codes.setter
    def orig_op_mobile_network_codes(self, orig_op_mobile_network_codes: MobileNetworkIds):
        """Sets the orig_op_mobile_network_codes of this FederationRequestData.


        :param orig_op_mobile_network_codes: The orig_op_mobile_network_codes of this FederationRequestData.
        :type orig_op_mobile_network_codes: MobileNetworkIds
        """

        self._orig_op_mobile_network_codes = orig_op_mobile_network_codes

    @property
    def orig_op_fixed_network_codes(self) -> FixedNetworkIds:
        """Gets the orig_op_fixed_network_codes of this FederationRequestData.


        :return: The orig_op_fixed_network_codes of this FederationRequestData.
        :rtype: FixedNetworkIds
        """
        return self._orig_op_fixed_network_codes

    @orig_op_fixed_network_codes.setter
    def orig_op_fixed_network_codes(self, orig_op_fixed_network_codes: FixedNetworkIds):
        """Sets the orig_op_fixed_network_codes of this FederationRequestData.


        :param orig_op_fixed_network_codes: The orig_op_fixed_network_codes of this FederationRequestData.
        :type orig_op_fixed_network_codes: FixedNetworkIds
        """

        self._orig_op_fixed_network_codes = orig_op_fixed_network_codes

    @property
    def initial_date(self) -> datetime:
        """Gets the initial_date of this FederationRequestData.

        Time zone info of the federation initiated by the originating OP  # noqa: E501

        :return: The initial_date of this FederationRequestData.
        :rtype: datetime
        """
        return self._initial_date

    @initial_date.setter
    def initial_date(self, initial_date: datetime):
        """Sets the initial_date of this FederationRequestData.

        Time zone info of the federation initiated by the originating OP  # noqa: E501

        :param initial_date: The initial_date of this FederationRequestData.
        :type initial_date: datetime
        """
        if initial_date is None:
            raise ValueError("Invalid value for `initial_date`, must not be `None`")  # noqa: E501

        self._initial_date = initial_date

    @property
    def partner_status_link(self) -> Uri:
        """Gets the partner_status_link of this FederationRequestData.


        :return: The partner_status_link of this FederationRequestData.
        :rtype: Uri
        """
        return self._partner_status_link

    @partner_status_link.setter
    def partner_status_link(self, partner_status_link: Uri):
        """Sets the partner_status_link of this FederationRequestData.


        :param partner_status_link: The partner_status_link of this FederationRequestData.
        :type partner_status_link: Uri
        """
        if partner_status_link is None:
            raise ValueError("Invalid value for `partner_status_link`, must not be `None`")  # noqa: E501

        self._partner_status_link = partner_status_link

    @property
    def partner_callback_credentials(self) -> CallbackCredentials:
        """Gets the partner_callback_credentials of this FederationRequestData.


        :return: The partner_callback_credentials of this FederationRequestData.
        :rtype: CallbackCredentials
        """
        return self._partner_callback_credentials

    @partner_callback_credentials.setter
    def partner_callback_credentials(self, partner_callback_credentials: CallbackCredentials):
        """Sets the partner_callback_credentials of this FederationRequestData.


        :param partner_callback_credentials: The partner_callback_credentials of this FederationRequestData.
        :type partner_callback_credentials: CallbackCredentials
        """

        self._partner_callback_credentials = partner_callback_credentials
