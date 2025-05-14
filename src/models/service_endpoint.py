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
from models.fqdn import Fqdn  # noqa: F401,E501
from models.ipv4_addr import Ipv4Addr  # noqa: F401,E501
from models.ipv6_addr import Ipv6Addr  # noqa: F401,E501
from models.port import Port  # noqa: F401,E501
import util


class ServiceEndpoint(Model):
    def __init__(self, port: Port=None, fqdn: Fqdn=None, ipv4_addresses: List[Ipv4Addr]=None, ipv6_addresses: List[Ipv6Addr]=None):  # noqa: E501
        """ServiceEndpoint - a model defined in Swagger

        :param port: The port of this ServiceEndpoint.  # noqa: E501
        :type port: Port
        :param fqdn: The fqdn of this ServiceEndpoint.  # noqa: E501
        :type fqdn: Fqdn
        :param ipv4_addresses: The ipv4_addresses of this ServiceEndpoint.  # noqa: E501
        :type ipv4_addresses: List[Ipv4Addr]
        :param ipv6_addresses: The ipv6_addresses of this ServiceEndpoint.  # noqa: E501
        :type ipv6_addresses: List[Ipv6Addr]
        """
        self.swagger_types = {
            'port': Port,
            'fqdn': Fqdn,
            'ipv4_addresses': List[Ipv4Addr],
            'ipv6_addresses': List[Ipv6Addr]
        }

        self.attribute_map = {
            'port': 'port',
            'fqdn': 'fqdn',
            'ipv4_addresses': 'ipv4Addresses',
            'ipv6_addresses': 'ipv6Addresses'
        }
        self._port = port
        self._fqdn = fqdn
        self._ipv4_addresses = ipv4_addresses
        self._ipv6_addresses = ipv6_addresses

    @classmethod
    def from_dict(cls, dikt) -> 'ServiceEndpoint':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ServiceEndpoint of this ServiceEndpoint.  # noqa: E501
        :rtype: ServiceEndpoint
        """
        return util.deserialize_model(dikt, cls)

    @property
    def port(self) -> Port:
        """Gets the port of this ServiceEndpoint.


        :return: The port of this ServiceEndpoint.
        :rtype: Port
        """
        return self._port

    @port.setter
    def port(self, port: Port):
        """Sets the port of this ServiceEndpoint.


        :param port: The port of this ServiceEndpoint.
        :type port: Port
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def fqdn(self) -> Fqdn:
        """Gets the fqdn of this ServiceEndpoint.


        :return: The fqdn of this ServiceEndpoint.
        :rtype: Fqdn
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn: Fqdn):
        """Sets the fqdn of this ServiceEndpoint.


        :param fqdn: The fqdn of this ServiceEndpoint.
        :type fqdn: Fqdn
        """

        self._fqdn = fqdn

    @property
    def ipv4_addresses(self) -> List[Ipv4Addr]:
        """Gets the ipv4_addresses of this ServiceEndpoint.


        :return: The ipv4_addresses of this ServiceEndpoint.
        :rtype: List[Ipv4Addr]
        """
        return self._ipv4_addresses

    @ipv4_addresses.setter
    def ipv4_addresses(self, ipv4_addresses: List[Ipv4Addr]):
        """Sets the ipv4_addresses of this ServiceEndpoint.


        :param ipv4_addresses: The ipv4_addresses of this ServiceEndpoint.
        :type ipv4_addresses: List[Ipv4Addr]
        """

        self._ipv4_addresses = ipv4_addresses

    @property
    def ipv6_addresses(self) -> List[Ipv6Addr]:
        """Gets the ipv6_addresses of this ServiceEndpoint.


        :return: The ipv6_addresses of this ServiceEndpoint.
        :rtype: List[Ipv6Addr]
        """
        return self._ipv6_addresses

    @ipv6_addresses.setter
    def ipv6_addresses(self, ipv6_addresses: List[Ipv6Addr]):
        """Sets the ipv6_addresses of this ServiceEndpoint.


        :param ipv6_addresses: The ipv6_addresses of this ServiceEndpoint.
        :type ipv6_addresses: List[Ipv6Addr]
        """

        self._ipv6_addresses = ipv6_addresses
