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


class HugePage(Model):
    def __init__(self, page_size: str=None, number: int=None):  # noqa: E501
        """HugePage - a model defined in Swagger

        :param page_size: The page_size of this HugePage.  # noqa: E501
        :type page_size: str
        :param number: The number of this HugePage.  # noqa: E501
        :type number: int
        """
        self.swagger_types = {
            'page_size': str,
            'number': int
        }

        self.attribute_map = {
            'page_size': 'pageSize',
            'number': 'number'
        }
        self._page_size = page_size
        self._number = number

    @classmethod
    def from_dict(cls, dikt) -> 'HugePage':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The HugePage of this HugePage.  # noqa: E501
        :rtype: HugePage
        """
        return util.deserialize_model(dikt, cls)

    @property
    def page_size(self) -> str:
        """Gets the page_size of this HugePage.

        Size of hugepage  # noqa: E501

        :return: The page_size of this HugePage.
        :rtype: str
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size: str):
        """Sets the page_size of this HugePage.

        Size of hugepage  # noqa: E501

        :param page_size: The page_size of this HugePage.
        :type page_size: str
        """
        """
        allowed_values = ["2MB", "4MB", "1GB"]  # noqa: E501
        if page_size not in allowed_values:
            raise ValueError(
                "Invalid value for `page_size` ({0}), must be one of {1}"
                .format(page_size, allowed_values)
            )
        """
        self._page_size = page_size

    @property
    def number(self) -> int:
        """Gets the number of this HugePage.

        Total number of huge pages  # noqa: E501

        :return: The number of this HugePage.
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number: int):
        """Sets the number of this HugePage.

        Total number of huge pages  # noqa: E501

        :param number: The number of this HugePage.
        :type number: int
        """
        if number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501

        self._number = number
