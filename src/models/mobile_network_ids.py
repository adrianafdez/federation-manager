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
from models.mcc import Mcc  # noqa: F401,E501
from models.mnc import Mnc  # noqa: F401,E501
import re  # noqa: F401,E501
import util


class MobileNetworkIds(Model):
    def __init__(self, mcc: Mcc=None, mncs: List[Mnc]=None):  # noqa: E501
        """MobileNetworkIds - a model defined in Swagger

        :param mcc: The mcc of this MobileNetworkIds.  # noqa: E501
        :type mcc: Mcc
        :param mncs: The mncs of this MobileNetworkIds.  # noqa: E501
        :type mncs: List[Mnc]
        """
        self.swagger_types = {
            'mcc': Mcc,
            'mncs': List[Mnc]
        }

        self.attribute_map = {
            'mcc': 'mcc',
            'mncs': 'mncs'
        }
        self._mcc = mcc
        self._mncs = mncs

    @classmethod
    def from_dict(cls, dikt) -> 'MobileNetworkIds':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MobileNetworkIds of this MobileNetworkIds.  # noqa: E501
        :rtype: MobileNetworkIds
        """
        return util.deserialize_model(dikt, cls)

    @property
    def mcc(self) -> Mcc:
        """Gets the mcc of this MobileNetworkIds.


        :return: The mcc of this MobileNetworkIds.
        :rtype: Mcc
        """
        return self._mcc

    @mcc.setter
    def mcc(self, mcc: Mcc):
        """Sets the mcc of this MobileNetworkIds.


        :param mcc: The mcc of this MobileNetworkIds.
        :type mcc: Mcc
        """

        self._mcc = mcc

    @property
    def mncs(self) -> List[Mnc]:
        """Gets the mncs of this MobileNetworkIds.


        :return: The mncs of this MobileNetworkIds.
        :rtype: List[Mnc]
        """
        return self._mncs

    @mncs.setter
    def mncs(self, mncs: List[Mnc]):
        """Sets the mncs of this MobileNetworkIds.


        :param mncs: The mncs of this MobileNetworkIds.
        :type mncs: List[Mnc]
        """

        self._mncs = mncs
