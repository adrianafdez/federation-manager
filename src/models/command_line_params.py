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


class CommandLineParams(Model):
    def __init__(self, command: List[str]=None, command_args: List[str]=None):  # noqa: E501
        """CommandLineParams - a model defined in Swagger

        :param command: The command of this CommandLineParams.  # noqa: E501
        :type command: List[str]
        :param command_args: The command_args of this CommandLineParams.  # noqa: E501
        :type command_args: List[str]
        """
        self.swagger_types = {
            'command': List[str],
            'command_args': List[str]
        }

        self.attribute_map = {
            'command': 'command',
            'command_args': 'commandArgs'
        }
        self._command = command
        self._command_args = command_args

    @classmethod
    def from_dict(cls, dikt) -> 'CommandLineParams':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CommandLineParams of this CommandLineParams.  # noqa: E501
        :rtype: CommandLineParams
        """
        return util.deserialize_model(dikt, cls)

    @property
    def command(self) -> List[str]:
        """Gets the command of this CommandLineParams.

        List of commands that application should invoke when an instance is created.  # noqa: E501

        :return: The command of this CommandLineParams.
        :rtype: List[str]
        """
        return self._command

    @command.setter
    def command(self, command: List[str]):
        """Sets the command of this CommandLineParams.

        List of commands that application should invoke when an instance is created.  # noqa: E501

        :param command: The command of this CommandLineParams.
        :type command: List[str]
        """
        if command is None:
            raise ValueError("Invalid value for `command`, must not be `None`")  # noqa: E501

        self._command = command

    @property
    def command_args(self) -> List[str]:
        """Gets the command_args of this CommandLineParams.

        List of arguments required by the command.  # noqa: E501

        :return: The command_args of this CommandLineParams.
        :rtype: List[str]
        """
        return self._command_args

    @command_args.setter
    def command_args(self, command_args: List[str]):
        """Sets the command_args of this CommandLineParams.

        List of arguments required by the command.  # noqa: E501

        :param command_args: The command_args of this CommandLineParams.
        :type command_args: List[str]
        """

        self._command_args = command_args
