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
import re  # noqa: F401,E501
import util


class InterfaceDetails(Model):
    def __init__(self, interface_id: str=None, comm_protocol: str=None, comm_port: int=None, visibility_type: str=None, network: str=None, interface_name: str=None):  # noqa: E501
        """InterfaceDetails - a model defined in Swagger

        :param interface_id: The interface_id of this InterfaceDetails.  # noqa: E501
        :type interface_id: str
        :param comm_protocol: The comm_protocol of this InterfaceDetails.  # noqa: E501
        :type comm_protocol: str
        :param comm_port: The comm_port of this InterfaceDetails.  # noqa: E501
        :type comm_port: int
        :param visibility_type: The visibility_type of this InterfaceDetails.  # noqa: E501
        :type visibility_type: str
        :param network: The network of this InterfaceDetails.  # noqa: E501
        :type network: str
        :param interface_name: The interface_name of this InterfaceDetails.  # noqa: E501
        :type interface_name: str
        """
        self.swagger_types = {
            'interface_id': str,
            'comm_protocol': str,
            'comm_port': int,
            'visibility_type': str,
            'network': str,
            'interface_name': str
        }

        self.attribute_map = {
            'interface_id': 'interfaceId',
            'comm_protocol': 'commProtocol',
            'comm_port': 'commPort',
            'visibility_type': 'visibilityType',
            'network': 'network',
            'interface_name': 'InterfaceName'
        }
        self._interface_id = interface_id
        self._comm_protocol = comm_protocol
        self._comm_port = comm_port
        self._visibility_type = visibility_type
        self._network = network
        self._interface_name = interface_name

    @classmethod
    def from_dict(cls, dikt) -> 'InterfaceDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InterfaceDetails of this InterfaceDetails.  # noqa: E501
        :rtype: InterfaceDetails
        """
        return util.deserialize_model(dikt, cls)

    @property
    def interface_id(self) -> str:
        """Gets the interface_id of this InterfaceDetails.

        Each Port and corresponding traffic protocol exposed by the component is identified by a name. Application client on user device requires this to uniquely identify the interface.  # noqa: E501

        :return: The interface_id of this InterfaceDetails.
        :rtype: str
        """
        return self._interface_id

    @interface_id.setter
    def interface_id(self, interface_id: str):
        """Sets the interface_id of this InterfaceDetails.

        Each Port and corresponding traffic protocol exposed by the component is identified by a name. Application client on user device requires this to uniquely identify the interface.  # noqa: E501

        :param interface_id: The interface_id of this InterfaceDetails.
        :type interface_id: str
        """
        if interface_id is None:
            raise ValueError("Invalid value for `interface_id`, must not be `None`")  # noqa: E501

        self._interface_id = interface_id

    @property
    def comm_protocol(self) -> str:
        """Gets the comm_protocol of this InterfaceDetails.

        Defines the IP transport communication protocol i.e., TCP, UDP or HTTP  # noqa: E501

        :return: The comm_protocol of this InterfaceDetails.
        :rtype: str
        """
        return self._comm_protocol

    @comm_protocol.setter
    def comm_protocol(self, comm_protocol: str):
        """Sets the comm_protocol of this InterfaceDetails.

        Defines the IP transport communication protocol i.e., TCP, UDP or HTTP  # noqa: E501

        :param comm_protocol: The comm_protocol of this InterfaceDetails.
        :type comm_protocol: str
        """
        allowed_values = ["TCP", "UDP", "HTTP_HTTPS"]  # noqa: E501
        if comm_protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `comm_protocol` ({0}), must be one of {1}"
                .format(comm_protocol, allowed_values)
            )

        self._comm_protocol = comm_protocol

    @property
    def comm_port(self) -> int:
        """Gets the comm_port of this InterfaceDetails.

        Port number exposed by the component. OP may generate a dynamic port towards the UCs corresponding to this internal port and forward the client traffic from dynamic port to container Port.  # noqa: E501

        :return: The comm_port of this InterfaceDetails.
        :rtype: int
        """
        return self._comm_port

    @comm_port.setter
    def comm_port(self, comm_port: int):
        """Sets the comm_port of this InterfaceDetails.

        Port number exposed by the component. OP may generate a dynamic port towards the UCs corresponding to this internal port and forward the client traffic from dynamic port to container Port.  # noqa: E501

        :param comm_port: The comm_port of this InterfaceDetails.
        :type comm_port: int
        """
        if comm_port is None:
            raise ValueError("Invalid value for `comm_port`, must not be `None`")  # noqa: E501

        self._comm_port = comm_port

    @property
    def visibility_type(self) -> str:
        """Gets the visibility_type of this InterfaceDetails.

        Defines whether the interface is exposed to outer world or not i.e., external, or internal. If this is set to \"external\", then it is exposed to external applications otherwise it is exposed internally to edge application components within edge cloud. When exposed to external world, an external dynamic port is assigned for UC traffic and mapped to the internal container Port  # noqa: E501

        :return: The visibility_type of this InterfaceDetails.
        :rtype: str
        """
        return self._visibility_type

    @visibility_type.setter
    def visibility_type(self, visibility_type: str):
        """Sets the visibility_type of this InterfaceDetails.

        Defines whether the interface is exposed to outer world or not i.e., external, or internal. If this is set to \"external\", then it is exposed to external applications otherwise it is exposed internally to edge application components within edge cloud. When exposed to external world, an external dynamic port is assigned for UC traffic and mapped to the internal container Port  # noqa: E501

        :param visibility_type: The visibility_type of this InterfaceDetails.
        :type visibility_type: str
        """
        allowed_values = ["VISIBILITY_EXTERNAL", "VISIBILITY_INTERNAL"]  # noqa: E501
        if visibility_type not in allowed_values:
            raise ValueError(
                "Invalid value for `visibility_type` ({0}), must be one of {1}"
                .format(visibility_type, allowed_values)
            )

        self._visibility_type = visibility_type

    @property
    def network(self) -> str:
        """Gets the network of this InterfaceDetails.

        Name of the network.  In case the application has to be associated with more than 1 network then app provider must define the name of the network on which this interface has to be exposed.  This parameter is required only if the port has to be exposed on a specific network other than default.  # noqa: E501

        :return: The network of this InterfaceDetails.
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network: str):
        """Sets the network of this InterfaceDetails.

        Name of the network.  In case the application has to be associated with more than 1 network then app provider must define the name of the network on which this interface has to be exposed.  This parameter is required only if the port has to be exposed on a specific network other than default.  # noqa: E501

        :param network: The network of this InterfaceDetails.
        :type network: str
        """

        self._network = network

    @property
    def interface_name(self) -> str:
        """Gets the interface_name of this InterfaceDetails.

        Interface Name. Required only if application has to be attached to a network other than default.  # noqa: E501

        :return: The interface_name of this InterfaceDetails.
        :rtype: str
        """
        return self._interface_name

    @interface_name.setter
    def interface_name(self, interface_name: str):
        """Sets the interface_name of this InterfaceDetails.

        Interface Name. Required only if application has to be attached to a network other than default.  # noqa: E501

        :param interface_name: The interface_name of this InterfaceDetails.
        :type interface_name: str
        """

        self._interface_name = interface_name
