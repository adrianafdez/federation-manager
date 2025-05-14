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
from models.artefact_id import ArtefactId  # noqa: F401,E501
import re  # noqa: F401,E501
import util


class FederationContextIdapplicationonboardingappappIdAppComponentSpecs(Model):
    def __init__(self, service_name_nb: str=None, service_name_ew: str=None, component_name: str=None, artefact_id: ArtefactId=None):  # noqa: E501
        """FederationContextIdapplicationonboardingappappIdAppComponentSpecs - a model defined in Swagger

        :param service_name_nb: The service_name_nb of this FederationContextIdapplicationonboardingappappIdAppComponentSpecs.  # noqa: E501
        :type service_name_nb: str
        :param service_name_ew: The service_name_ew of this FederationContextIdapplicationonboardingappappIdAppComponentSpecs.  # noqa: E501
        :type service_name_ew: str
        :param component_name: The component_name of this FederationContextIdapplicationonboardingappappIdAppComponentSpecs.  # noqa: E501
        :type component_name: str
        :param artefact_id: The artefact_id of this FederationContextIdapplicationonboardingappappIdAppComponentSpecs.  # noqa: E501
        :type artefact_id: ArtefactId
        """
        self.swagger_types = {
            'service_name_nb': str,
            'service_name_ew': str,
            'component_name': str,
            'artefact_id': ArtefactId
        }

        self.attribute_map = {
            'service_name_nb': 'serviceNameNB',
            'service_name_ew': 'serviceNameEW',
            'component_name': 'componentName',
            'artefact_id': 'artefactId'
        }
        self._service_name_nb = service_name_nb
        self._service_name_ew = service_name_ew
        self._component_name = component_name
        self._artefact_id = artefact_id

    @classmethod
    def from_dict(cls, dikt) -> 'FederationContextIdapplicationonboardingappappIdAppComponentSpecs':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The federationContextIdapplicationonboardingappappId_appComponentSpecs of this FederationContextIdapplicationonboardingappappIdAppComponentSpecs.  # noqa: E501
        :rtype: FederationContextIdapplicationonboardingappappIdAppComponentSpecs
        """
        return util.deserialize_model(dikt, cls)

    @property
    def service_name_nb(self) -> str:
        """Gets the service_name_nb of this FederationContextIdapplicationonboardingappappIdAppComponentSpecs.

        Must be a valid RFC 1035 label name.  This defines the DNS name via which the component can be accessed over NBI. Access via serviceNameNB is restricted on specific ports. Platform shall expose component access externally via this DNS name  # noqa: E501

        :return: The service_name_nb of this FederationContextIdapplicationonboardingappappIdAppComponentSpecs.
        :rtype: str
        """
        return self._service_name_nb

    @service_name_nb.setter
    def service_name_nb(self, service_name_nb: str):
        """Sets the service_name_nb of this FederationContextIdapplicationonboardingappappIdAppComponentSpecs.

        Must be a valid RFC 1035 label name.  This defines the DNS name via which the component can be accessed over NBI. Access via serviceNameNB is restricted on specific ports. Platform shall expose component access externally via this DNS name  # noqa: E501

        :param service_name_nb: The service_name_nb of this FederationContextIdapplicationonboardingappappIdAppComponentSpecs.
        :type service_name_nb: str
        """

        self._service_name_nb = service_name_nb

    @property
    def service_name_ew(self) -> str:
        """Gets the service_name_ew of this FederationContextIdapplicationonboardingappappIdAppComponentSpecs.

        Must be a valid RFC 1035 label name.  This defines the DNS name via which the component can be accessed via peer components. Access via serviceNameEW is open on all ports.   Platform shall not expose serviceNameEW externally outside edge.  # noqa: E501

        :return: The service_name_ew of this FederationContextIdapplicationonboardingappappIdAppComponentSpecs.
        :rtype: str
        """
        return self._service_name_ew

    @service_name_ew.setter
    def service_name_ew(self, service_name_ew: str):
        """Sets the service_name_ew of this FederationContextIdapplicationonboardingappappIdAppComponentSpecs.

        Must be a valid RFC 1035 label name.  This defines the DNS name via which the component can be accessed via peer components. Access via serviceNameEW is open on all ports.   Platform shall not expose serviceNameEW externally outside edge.  # noqa: E501

        :param service_name_ew: The service_name_ew of this FederationContextIdapplicationonboardingappappIdAppComponentSpecs.
        :type service_name_ew: str
        """

        self._service_name_ew = service_name_ew

    @property
    def component_name(self) -> str:
        """Gets the component_name of this FederationContextIdapplicationonboardingappappIdAppComponentSpecs.

        Must be a valid RFC 1035 label name.  Component name must be unique with an application  # noqa: E501

        :return: The component_name of this FederationContextIdapplicationonboardingappappIdAppComponentSpecs.
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name: str):
        """Sets the component_name of this FederationContextIdapplicationonboardingappappIdAppComponentSpecs.

        Must be a valid RFC 1035 label name.  Component name must be unique with an application  # noqa: E501

        :param component_name: The component_name of this FederationContextIdapplicationonboardingappappIdAppComponentSpecs.
        :type component_name: str
        """
        if component_name is None:
            raise ValueError("Invalid value for `component_name`, must not be `None`")  # noqa: E501

        self._component_name = component_name

    @property
    def artefact_id(self) -> ArtefactId:
        """Gets the artefact_id of this FederationContextIdapplicationonboardingappappIdAppComponentSpecs.


        :return: The artefact_id of this FederationContextIdapplicationonboardingappappIdAppComponentSpecs.
        :rtype: ArtefactId
        """
        return self._artefact_id

    @artefact_id.setter
    def artefact_id(self, artefact_id: ArtefactId):
        """Sets the artefact_id of this FederationContextIdapplicationonboardingappappIdAppComponentSpecs.


        :param artefact_id: The artefact_id of this FederationContextIdapplicationonboardingappappIdAppComponentSpecs.
        :type artefact_id: ArtefactId
        """

        self._artefact_id = artefact_id
