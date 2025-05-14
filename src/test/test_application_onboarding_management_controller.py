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

from flask import json
from six import BytesIO

from models.app_app_id_body import AppAppIdBody  # noqa: E501
from models.app_identifier import AppIdentifier  # noqa: E501
from models.application_onboarding_body import ApplicationOnboardingBody  # noqa: E501
from models.federation_context_id import FederationContextId  # noqa: E501
from models.inline_response2007 import InlineResponse2007  # noqa: E501
from models.problem_details import ProblemDetails  # noqa: E501
from models.zone_identifier import ZoneIdentifier  # noqa: E501
from test import BaseTestCase
import requests
from clients import i2edge
import util


class TestApplicationOnboardingManagementController(BaseTestCase):
    """ApplicationOnboardingManagementController integration test stubs"""

    BaseTestCase.federation = ""
    BaseTestCase.federation2 = ""
    BaseTestCase.token = ""
    BaseTestCase.zone = ""

    def run(self, result=None):
        """ Stop after first error """
        try:
            # Check if there is connection with i2edge. Otherwise stop the test
            self.assertRaises(Exception, i2edge.get_zones())

            # Check if there is connection with keycloak. Otherwise stop the test
            self.assertRaises(Exception, self.get_access_token())

            # Get token from keycloak
            BaseTestCase.token = self.get_access_token()

            # Check if there is connection with FM. Otherwise stop the test
            self.assertRaises(Exception, self.get_federation_resources(BaseTestCase.token))

            # Check if there is connection with FM Originating OP. Otherwise stop the test
            if self.roleOp == util._ROLE_ORIGINATING_OP:
                self.assertRaises(Exception, self.get_federation_resources_originating_op(BaseTestCase.token))

            # Get zone id from i2edge
            BaseTestCase.zone = self.get_first_zone_from_zone_list_i2edge()
            if BaseTestCase.zone == "":
                raise Exception("Test Failed. Unable to retrieve zone from i2edge")

            super(TestApplicationOnboardingManagementController, self).run(result)
        except Exception as error:
            raise Exception(f"Test failed. Reason: {error}")

    def test_00(self):

        try:
            # Check it there are artefact and profile created at i2edge and must be deleted because remains there due
            # to a possible issue during the test
            i2edge.delete_onboarding(self.app_id)
            i2edge.delete_artefact(self.artefact_id)

            # Create federation context
            BaseTestCase.federation = self.post_federation_context(BaseTestCase.token)

            # Assign Zones to this federation context
            self.post_availability_zones(BaseTestCase.federation, BaseTestCase.zone, BaseTestCase.token)

            # Create artefact for this federation context
            self.post_artefact(BaseTestCase.federation, self.artefact_id, self.app_provider, BaseTestCase.token)

            # Get token from keycloak
            BaseTestCase.token = self.get_access_token()

            # Create alternative federation context
            BaseTestCase.federation2 = self.post_federation_context(BaseTestCase.token)

        except Exception as error:
            raise Exception(f"Test failed. Reason: {error}")

    # Create onboarding
    def test_01(self):
        """Test case for onboard_application

             Submits an application details to a partner OP. Based on the details provided,  partner OP shall do bookkeeping, resource validation and other pre-deployment operations.
        """

        body = {
            "appId": self.app_id,
            "appProviderId": self.app_provider,
            "appDeploymentZones": [
                BaseTestCase.zone
            ],
            "appMetaData": {
                "appName": "dsdsdsdssdssdsdssd",
                "version": "string",
                "appDescription": "sdssdssdsdssdsdsdss",
                "mobilitySupport": False,
                "accessToken": "sdsddssddssdsssdsdsdsdsdsdsdsddsddsdsdsdsdsd",
                "category": "IOT"
            },
            "appQoSProfile": {
                "latencyConstraints": "NONE",
                "bandwidthRequired": 1,
                "multiUserClients": "APP_TYPE_SINGLE_USER",
                "noOfUsersPerAppInst": 1,
                "appProvisioning": True
            },
            "appComponentSpecs": [
                {
                    "serviceNameNB": "dsdsdsdsdsdsdsdsdsdds",
                    "serviceNameEW": "sdsdsdsdddsssdsdssdsd",
                    "componentName": "sdssssssssdsdsdsdsdss",
                    "artefactId": self.artefact_id
                }
            ],
            "appStatusCallbackLink": "string"
        }

        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/onboarding"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}
        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)

        self.assertEqual(response.status_code, 202, f'Response body is : {content}')

    # Create onboarding. Incorrect value for federation
    def test_02(self):
        """Test case for onboard_application

             Submits an application details to a partner OP. Based on the details provided,  partner OP shall do bookkeeping, resource validation and other pre-deployment operations.
        """

        body = {
            "appId": self.app_id,
            "appProviderId": self.app_provider,
            "appDeploymentZones": [
                BaseTestCase.zone
            ],
            "appMetaData": {
                "appName": "dsdsdsdssdssdsdssd",
                "version": "string",
                "appDescription": "sdssdssdsdssdsdsdss",
                "mobilitySupport": False,
                "accessToken": "sdsddssddssdsssdsdsdsdsdsdsdsddsddsdsdsdsdsd",
                "category": "IOT"
            },
            "appQoSProfile": {
                "latencyConstraints": "NONE",
                "bandwidthRequired": 1,
                "multiUserClients": "APP_TYPE_SINGLE_USER",
                "noOfUsersPerAppInst": 1,
                "appProvisioning": True
            },
            "appComponentSpecs": [
                {
                    "serviceNameNB": "dsdsdsdsdsdsdsdsdsdds",
                    "serviceNameEW": "sdsdsdsdddsssdsdssdsd",
                    "componentName": "sdssssssssdsdsdsdsdss",
                    "artefactId": self.artefact_id
                }
            ],
            "appStatusCallbackLink": "string"
        }

        url = f"http://{self.base_url}/{3232222232323232}/application/onboarding"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}
        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)

        self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # Create onboarding. Federation not found
    def test_03(self):
        """Test case for onboard_application

             Submits an application details to a partner OP. Based on the details provided,  partner OP shall do bookkeeping, resource validation and other pre-deployment operations.
        """

        body = {
            "appId": self.app_id,
            "appProviderId": self.app_provider,
            "appDeploymentZones": [
                BaseTestCase.zone
            ],
            "appMetaData": {
                "appName": "dsdsdsdssdssdsdssd",
                "version": "string",
                "appDescription": "sdssdssdsdssdsdsdss",
                "mobilitySupport": False,
                "accessToken": "sdsddssddssdsssdsdsdsdsdsdsdsddsddsdsdsdsdsd",
                "category": "IOT"
            },
            "appQoSProfile": {
                "latencyConstraints": "NONE",
                "bandwidthRequired": 1,
                "multiUserClients": "APP_TYPE_SINGLE_USER",
                "noOfUsersPerAppInst": 1,
                "appProvisioning": True
            },
            "appComponentSpecs": [
                {
                    "serviceNameNB": "dsdsdsdsdsdsdsdsdsdds",
                    "serviceNameEW": "sdsdsdsdddsssdsdssdsd",
                    "componentName": "sdssssssssdsdsdsdsdss",
                    "artefactId": self.artefact_id
                }
            ],
            "appStatusCallbackLink": "string"
        }

        url = f"http://{self.base_url}/{'65b799f576063bc1ac9e6999'}/application/onboarding"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}
        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    # Create onboarding. Federation and app id already exist
    def test_04(self):
        """Test case for onboard_application

             Submits an application details to a partner OP. Based on the details provided,  partner OP shall do bookkeeping, resource validation and other pre-deployment operations.
        """

        body = {
            "appId": self.app_id,
            "appProviderId": self.app_provider,
            "appDeploymentZones": [
                BaseTestCase.zone
            ],
            "appMetaData": {
                "appName": "dsdsdsdssdssdsdssd",
                "version": "string",
                "appDescription": "sdssdssdsdssdsdsdss",
                "mobilitySupport": False,
                "accessToken": "sdsddssddssdsssdsdsdsdsdsdsdsddsddsdsdsdsdsd",
                "category": "IOT"
            },
            "appQoSProfile": {
                "latencyConstraints": "NONE",
                "bandwidthRequired": 1,
                "multiUserClients": "APP_TYPE_SINGLE_USER",
                "noOfUsersPerAppInst": 1,
                "appProvisioning": True
            },
            "appComponentSpecs": [
                {
                    "serviceNameNB": "dsdsdsdsdsdsdsdsdsdds",
                    "serviceNameEW": "sdsdsdsdddsssdsdssdsd",
                    "componentName": "sdssssssssdsdsdsdsdss",
                    "artefactId": self.artefact_id
                }
            ],
            "appStatusCallbackLink": "string"
        }

        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/onboarding"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}
        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 409, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # Create onboarding. Check if exist app id in the database. If found app id belongs to another federation,
    def test_05(self):
        """Test case for onboard_application

             Submits an application details to a partner OP. Based on the details provided,  partner OP shall do bookkeeping, resource validation and other pre-deployment operations.
        """

        body = {
            "appId": self.app_id,
            "appProviderId": self.app_provider,
            "appDeploymentZones": [
                BaseTestCase.zone
            ],
            "appMetaData": {
                "appName": "dsdsdsdssdssdsdssd",
                "version": "string",
                "appDescription": "sdssdssdsdssdsdsdss",
                "mobilitySupport": False,
                "accessToken": "sdsddssddssdsssdsdsdsdsdsdsdsddsddsdsdsdsdsd",
                "category": "IOT"
            },
            "appQoSProfile": {
                "latencyConstraints": "NONE",
                "bandwidthRequired": 1,
                "multiUserClients": "APP_TYPE_SINGLE_USER",
                "noOfUsersPerAppInst": 1,
                "appProvisioning": True
            },
            "appComponentSpecs": [
                {
                    "serviceNameNB": "dsdsdsdsdsdsdsdsdsdds",
                    "serviceNameEW": "sdsdsdsdddsssdsdssdsd",
                    "componentName": "sdssssssssdsdsdsdsdss",
                    "artefactId": self.artefact_id
                }
            ],
            "appStatusCallbackLink": "string"
        }

        url = f"http://{self.base_url}/{BaseTestCase.federation2}/application/onboarding"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}
        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 409, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # Create onboarding. Check if exist artefact id for this federation context
    def test_06(self):
        """Test case for onboard_application

             Submits an application details to a partner OP. Based on the details provided,  partner OP shall do bookkeeping, resource validation and other pre-deployment operations.
        """

        body = {
            "appId": "test_app_id_id",
            "appProviderId": self.app_provider,
            "appDeploymentZones": [
                BaseTestCase.zone
            ],
            "appMetaData": {
                "appName": "dsdsdsdssdssdsdssd",
                "version": "string",
                "appDescription": "sdssdssdsdssdsdsdss",
                "mobilitySupport": False,
                "accessToken": "sdsddssddssdsssdsdsdsdsdsdsdsddsddsdsdsdsdsd",
                "category": "IOT"
            },
            "appQoSProfile": {
                "latencyConstraints": "NONE",
                "bandwidthRequired": 1,
                "multiUserClients": "APP_TYPE_SINGLE_USER",
                "noOfUsersPerAppInst": 1,
                "appProvisioning": True
            },
            "appComponentSpecs": [
                {
                    "serviceNameNB": "dsdsdsdsdsdsdsdsdsdds",
                    "serviceNameEW": "sdsdsdsdddsssdsdssdsd",
                    "componentName": "sdssssssssdsdsdsdsdss",
                    "artefactId": "3fa85f64-5717-4562-b3fc-888888888888"
                }
            ],
            "appStatusCallbackLink": "string"
        }

        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/onboarding"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}
        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 404, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # Create onboarding. Check if exist the provider of the body natches with the providers of the artefact in component specs
    def test_07(self):
        """Test case for onboard_application

             Submits an application details to a partner OP. Based on the details provided,  partner OP shall do bookkeeping, resource validation and other pre-deployment operations.
        """

        body = {
            "appId": "test_app_id_id",
            "appProviderId": "provider_provider",
            "appDeploymentZones": [
                BaseTestCase.zone
            ],
            "appMetaData": {
                "appName": "dsdsdsdssdssdsdssd",
                "version": "string",
                "appDescription": "sdssdssdsdssdsdsdss",
                "mobilitySupport": False,
                "accessToken": "sdsddssddssdsssdsdsdsdsdsdsdsddsddsdsdsdsdsd",
                "category": "IOT"
            },
            "appQoSProfile": {
                "latencyConstraints": "NONE",
                "bandwidthRequired": 1,
                "multiUserClients": "APP_TYPE_SINGLE_USER",
                "noOfUsersPerAppInst": 1,
                "appProvisioning": True
            },
            "appComponentSpecs": [
                {
                    "serviceNameNB": "dsdsdsdsdsdsdsdsdsdds",
                    "serviceNameEW": "sdsdsdsdddsssdsdssdsd",
                    "componentName": "sdssssssssdsdsdsdsdss",
                    "artefactId": self.artefact_id
                }
            ],
            "appStatusCallbackLink": "string"
        }

        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/onboarding"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}
        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 404, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # Create onboarding. Check if exist zones for this federation context
    def test_08(self):
        """Test case for onboard_application

             Submits an application details to a partner OP. Based on the details provided,  partner OP shall do bookkeeping, resource validation and other pre-deployment operations.
        """

        body = {
            "appId": "test_app_id_id",
            "appProviderId": self.app_provider,
            "appDeploymentZones": [
                "ba5da2ead2c8461cb9e33a0ea47db555"
            ],
            "appMetaData": {
                "appName": "dsdsdsdssdssdsdssd",
                "version": "string",
                "appDescription": "sdssdssdsdssdsdsdss",
                "mobilitySupport": False,
                "accessToken": "sdsddssddssdsssdsdsdsdsdsdsdsddsddsdsdsdsdsd",
                "category": "IOT"
            },
            "appQoSProfile": {
                "latencyConstraints": "NONE",
                "bandwidthRequired": 1,
                "multiUserClients": "APP_TYPE_SINGLE_USER",
                "noOfUsersPerAppInst": 1,
                "appProvisioning": True
            },
            "appComponentSpecs": [
                {
                    "serviceNameNB": "dsdsdsdsdsdsdsdsdsdds",
                    "serviceNameEW": "sdsdsdsdddsssdsdssdsd",
                    "componentName": "sdssssssssdsdsdsdsdss",
                    "artefactId": self.artefact_id
                }
            ],
            "appStatusCallbackLink": "string"
        }

        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/onboarding"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}
        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 404, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # View onboarding
    def test_09(self):
        """Test case for view_application

           Retrieves application details from partner OP
        """
        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/onboarding/app/{self.app_id}"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}
        response = requests.get(url, headers=headers)
        content = json.loads(response.content)

        self.assertEqual(response.status_code, 200, f'Response body is : {content}')

    # View onboarding. Incorrect value for Federation
    def test_10(self):
        """Test case for view_application

           Retrieves application details from partner OP
        """
        url = f"http://{self.base_url}/{3232222232323232}/application/onboarding/app/{self.app_id}"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}
        response = requests.get(url, headers=headers)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 500, f'Response body is : {content}')

    # View onboarding. Federation not found
    def test_11(self):
        """Test case for view_application

           Retrieves application details from partner OP
        """
        url = f"http://{self.base_url}/{'65b799f576063bc1ac9e6999'}/application/onboarding/app/{self.app_id}"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}
        response = requests.get(url, headers=headers)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    # View onboarding. Check if exist Federation Context Id and App Id in Application Onboarding Management
    def test_12(self):
        """Test case for view_application

           Retrieves application details from partner OP
        """
        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/onboarding/app/{'test_test'}"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}
        response = requests.get(url, headers=headers)
        content = json.loads(response.content)

        self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    # Update onboarding
    def test_13(self):
        """Test case for update_application

            Updates partner OP about changes in application compute resource requirements, QOS Profile, associated descriptor or change in associated components
        """
        body = {
          "appUpdQoSProfile": {
            "latencyConstraints": "NONE",
            "bandwidthRequired": 2,
            "mobilitySupport": True,
            "multiUserClients": "APP_TYPE_SINGLE_USER",
            "noOfUsersPerAppInst": 1,
            "appProvisioning": True
          },
          "appComponentSpecs": [
              {
                  "serviceNameNB": "nameNBUpdated",
                  "serviceNameEW": "nameEWUpdated",
                  "componentName": "componentNameUpdated",
                  "artefactId": self.artefact_id
              }
          ]
        }
        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/onboarding/app/{self.app_id}"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.patch(url, headers=headers, json=body)
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 202, f'Response body is : {content}')

    # Update onboarding. Federation not found
    def test_14(self):
        """Test case for update_application

            Updates partner OP about changes in application compute resource requirements, QOS Profile, associated descriptor or change in associated components
        """
        body = {
            "appUpdQoSProfile": {
                "latencyConstraints": "NONE",
                "bandwidthRequired": 2,
                "mobilitySupport": True,
                "multiUserClients": "APP_TYPE_SINGLE_USER",
                "noOfUsersPerAppInst": 1,
                "appProvisioning": True
            },
            "appComponentSpecs": [
                {
                    "serviceNameNB": "nameNBUpdated",
                    "serviceNameEW": "nameEWUpdated",
                    "componentName": "componentNameUpdated",
                    "artefactId": self.artefact_id
                }
            ]
        }
        url = f"http://{self.base_url}/{'65b799f576063bc1ac9e6999'}/application/onboarding/app/{self.app_id}"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.patch(url, headers=headers, json=body)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    # Update onboarding. Incorrect value for Federation
    def test_15(self):
        """Test case for update_application

            Updates partner OP about changes in application compute resource requirements, QOS Profile, associated descriptor or change in associated components
        """
        body = {
            "appUpdQoSProfile": {
                "latencyConstraints": "NONE",
                "bandwidthRequired": 2,
                "mobilitySupport": True,
                "multiUserClients": "APP_TYPE_SINGLE_USER",
                "noOfUsersPerAppInst": 1,
                "appProvisioning": True
            },
            "appComponentSpecs": [
                {
                    "serviceNameNB": "nameNBUpdated",
                    "serviceNameEW": "nameEWUpdated",
                    "componentName": "componentNameUpdated",
                    "artefactId": self.artefact_id
                }
            ]
        }
        url = f"http://{self.base_url}/{3232222232323232}/application/onboarding/app/{self.app_id}"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.patch(url, headers=headers, json=body)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 500, f'Response body is : {content}')

    # Update onboarding. Check if exist Federation Context Id and App Id in Application Onboarding Management
    def test_16(self):
        """Test case for update_application

            Updates partner OP about changes in application compute resource requirements, QOS Profile, associated descriptor or change in associated components
        """
        body = {
            "appUpdQoSProfile": {
                "latencyConstraints": "NONE",
                "bandwidthRequired": 2,
                "mobilitySupport": True,
                "multiUserClients": "APP_TYPE_SINGLE_USER",
                "noOfUsersPerAppInst": 1,
                "appProvisioning": True
            },
            "appComponentSpecs": [
                {
                    "serviceNameNB": "nameNBUpdated",
                    "serviceNameEW": "nameEWUpdated",
                    "componentName": "componentNameUpdated",
                    "artefactId": self.artefact_id
                }
            ]
        }
        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/onboarding/app/{'test_test_test'}"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.patch(url, headers=headers, json=body)
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    # Update onboarding. Check if exist artefact id for this federation context
    def test_17(self):
        """Test case for update_application

            Updates partner OP about changes in application compute resource requirements, QOS Profile, associated descriptor or change in associated components
        """
        body = {
            "appUpdQoSProfile": {
                "latencyConstraints": "NONE",
                "bandwidthRequired": 2,
                "mobilitySupport": True,
                "multiUserClients": "APP_TYPE_SINGLE_USER",
                "noOfUsersPerAppInst": 1,
                "appProvisioning": True
            },
            "appComponentSpecs": [
                {
                    "serviceNameNB": "nameNBUpdated",
                    "serviceNameEW": "nameEWUpdated",
                    "componentName": "componentNameUpdated",
                    "artefactId": "3fa85f64-5717-4562-b3fc-888888888888"
                }
            ]
        }
        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/onboarding/app/{self.app_id}"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.patch(url, headers=headers, json=body)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 404, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # Remove onboarding. Incorrect value for federation
    def test_18(self):
        """Test case for delete_app

           Deboards the application from any zones, if any, and deletes the App.
        """

        url = f"http://{self.base_url}/{3232222232323232}/application/onboarding/app/{self.app_id}"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}
        response = requests.delete(url, headers=headers)
        content = json.loads(response.content)

        self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # Remove onboarding. Federation not found
    def test_19(self):
        """Test case for delete_app

           Deboards the application from any zones, if any, and deletes the App.
        """

        url = f"http://{self.base_url}/{'65b799f576063bc1ac9e6999'}/application/onboarding/app/{self.app_id}"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}
        response = requests.delete(url, headers=headers)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    # Remove onboarding. Check if exist Federation Context Id and App Id in Application Onboarding Management
    def test_20(self):
        """Test case for delete_app

           Deboards the application from any zones, if any, and deletes the App.
        """

        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/onboarding/app/{'test_test'}"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}
        response = requests.delete(url, headers=headers)
        content = json.loads(response.content)

        self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    # Remove onboarding
    def test_21(self):
        """Test case for delete_app

           Deboards the application from any zones, if any, and deletes the App.
        """

        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/onboarding/app/{self.app_id}"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}
        response = requests.delete(url, headers=headers)
        content = json.loads(response.content)

        self.assertEqual(response.status_code, 200, f'Response body is : {content}')

    def test_22(self):

        # Delete artefact
        self.delete_artefact(BaseTestCase.federation, self.artefact_id, BaseTestCase.token)

        # Delete zone
        self.delete_zone(BaseTestCase.federation, BaseTestCase.zone, BaseTestCase.token)

        # Delete federation
        self.delete_federation(BaseTestCase.federation, BaseTestCase.token)

        # Delete alternative federation
        self.delete_federation(BaseTestCase.federation2, BaseTestCase.token)


if __name__ == '__main__':
    import unittest
    unittest.main()
