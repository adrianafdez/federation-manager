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
from test import BaseTestCase
import requests
from clients import i2edge
import time
import util


class TestFederationManagementController(BaseTestCase):
    """FederationManagementController integration test stubs"""

    BaseTestCase.federation = ""
    BaseTestCase.token = ""

    def run(self, result=None):
        """ Stop after first error """
        try:
            time.sleep(5)

            # Check if there is connection with i2edge. Otherwise stop the test
            self.assertRaises(Exception, i2edge.get_zones())

            # Check if there is connection with keycloak. Otherwise stop the test
            self.assertRaises(Exception, self.get_access_token())

            super(TestFederationManagementController, self).run(result)
        except Exception as error:
            raise Exception(f"Test failed. Reason: {error}")

    def test_00(self):

        try:
            # Get token from keycloak
            BaseTestCase.token = self.get_access_token()

            # Check if there is connection with FM. Otherwise stop the test
            self.assertRaises(Exception, self.get_federation_resources(BaseTestCase.token))

            # Check if there is connection with FM ORIGINATING OP. Otherwise stop the test
            if self.roleOp == util._ROLE_ORIGINATING_OP:
                self.assertRaises(Exception, self.get_federation_resources_originating_op(BaseTestCase.token))

        except Exception as error:
            raise Exception(f"Test failed. Reason: {error}")

    # test create a federation
    def test_01(self):
        """Test case for create_federation

                Creates one direction federation with partner operator platform.
                """

        body = {
            "origOPFederationId": "string",
            "origOPCountryCode": "US",
            "origOPMobileNetworkCodes": {
                "mcc": "111",
                "mncs": [
                    "11"
                ]
            },
            "origOPFixedNetworkCodes": [
                "string"
            ],
            "initialDate": "2024-02-26T11:05:07.925Z",
            "partnerStatusLink": "string",
            "partnerCallbackCredentials": {
                "tokenUrl": "string",
                "clientId": "string",
                "clientSecret": "string"
            }
        }
        url = f"http://{self.base_url}/partner"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        BaseTestCase.federation = content.get("federationContextId")
        self.assertEqual(response.status_code, 200, f'Response body is : {content}')

    # test create a federation. Already Exists
    def test_02(self):
        """Test case for create_federation

                Creates one direction federation with partner operator platform.
                """

        body = {
            "origOPFederationId": "string",
            "origOPCountryCode": "US",
            "origOPMobileNetworkCodes": {
                "mcc": "111",
                "mncs": [
                    "11"
                ]
            },
            "origOPFixedNetworkCodes": [
                "string"
            ],
            "initialDate": "2024-02-26T11:05:07.925Z",
            "partnerStatusLink": "string",
            "partnerCallbackCredentials": {
                "tokenUrl": "string",
                "clientId": "string",
                "clientSecret": "string"
            }
        }
        url = f"http://{self.base_url}/partner"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 409, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')
    # Get federation
    def test_03(self):
        """Test case for get_federation_details
            Retrieves details about the federation context with the partner OP.
            The response shall provide info about the zones offered by the partner,
            partner OP network codes, information about edge discovery and LCM service etc.
        """
        url = f"http://{self.base_url}/{BaseTestCase.federation}/partner"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.get(url, headers=headers)

        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200, f'Response body is : {content}')

    # Get federation. Incorrect value for federation
    def test_04(self):
        """Test case for get_federation_details
            Retrieves details about the federation context with the partner OP.
            The response shall provide info about the zones offered by the partner,
            partner OP network codes, information about edge discovery and LCM service etc.
        """
        url = f"http://{self.base_url}/{3232222232323232}/partner"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.get(url, headers=headers)

        content = json.loads(response.content)
        self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # Get federation. Federation not Found
    def test_05(self):
        """Test case for get_federation_details
            Retrieves details about the federation context with the partner OP.
            The response shall provide info about the zones offered by the partner,
            partner OP network codes, information about edge discovery and LCM service etc.
        """
        url = f"http://{self.base_url}/{'65b799f576063bc1ac9e6999'}/partner"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.get(url, headers=headers)

        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    # test update a federation
    def test_06(self):
        """Test case for update_federation

         API used by the Originating OP towards the partner OP, to update the parameters associated to the existing federation
        """

        body = {
          "objectType": "MOBILE_NETWORK_CODES",
          "operationType": "ADD_CODES",
          "addMobileNetworkIds": {
            "mcc": "111",
            "mncs": [
              "22"
            ]
          },
          "removeMobileNetworkIds": {
            "mcc": "111",
            "mncs": [
              "11"
            ]
          },
          "addFixedNetworkIds": [
            "string"
          ],
          "removeFixedNetworkIds": [
            "string"
          ],
          "modificationDate": "2024-03-18T14:47:17.054Z"
        }
        url = f"http://{self.base_url}/{BaseTestCase.federation}/partner"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.patch(url, headers=headers, json=body)
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200, f'Response body is : {content}')

    # test update a federation. Bad request mcc value
    def test_07(self):
        """Test case for update_federation

         API used by the Originating OP towards the partner OP, to update the parameters associated to the existing federation
        """

        body = {
            "objectType": "MOBILE_NETWORK_CODES",
            "operationType": "ADD_CODES",
            "addMobileNetworkIds": {
                "mcc": "1111",
                "mncs": [
                    "22"
                ]
            },
            "removeMobileNetworkIds": {
                "111": "string",
                "mncs": [
                    "11"
                ]
            },
            "addFixedNetworkIds": [
                "string"
            ],
            "removeFixedNetworkIds": [
                "string"
            ],
            "modificationDate": "2024-03-18T14:47:17.054Z"
        }
        url = f"http://{self.base_url}/{BaseTestCase.federation}/partner"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.patch(url, headers=headers, json=body)
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 400, f'Response body is : {content}')

    # test update a federation. Federation not found
    def test_08(self):
        """Test case for update_federation

         API used by the Originating OP towards the partner OP, to update the parameters associated to the existing federation
        """

        body = {
            "objectType": "MOBILE_NETWORK_CODES",
            "operationType": "ADD_CODES",
            "addMobileNetworkIds": {
                "mcc": "111",
                "mncs": [
                    "22"
                ]
            },
            "removeMobileNetworkIds": {
                "mcc": "111",
                "mncs": [
                    "11"
                ]
            },
            "addFixedNetworkIds": [
                "string"
            ],
            "removeFixedNetworkIds": [
                "string"
            ],
            "modificationDate": "2024-03-18T14:47:17.054Z"
        }
        url = f"http://{self.base_url}/{'65b799f576063bc1ac9e6999'}/partner"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.patch(url, headers=headers, json=body)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    # test update a federation. Conflict with mcc
    def test_09(self):
        """Test case for update_federation

         API used by the Originating OP towards the partner OP, to update the parameters associated to the existing federation
        """

        body = {
            "objectType": "MOBILE_NETWORK_CODES",
            "operationType": "ADD_CODES",
            "addMobileNetworkIds": {
                "mcc": "222",
                "mncs": [
                    "22"
                ]
            },
            "removeMobileNetworkIds": {
                "mcc": "111",
                "mncs": [
                    "11"
                ]
            },
            "addFixedNetworkIds": [
                "string"
            ],
            "removeFixedNetworkIds": [
                "string"
            ],
            "modificationDate": "2024-03-18T14:47:17.054Z"
        }
        url = f"http://{self.base_url}/{BaseTestCase.federation}/partner"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.patch(url, headers=headers, json=body)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 409, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # Delete federation. Incorrect value for federation
    def test_10(self):
        """Test case for delete_federation_details

            Remove existing federation with the partner OP
        """
        url = f"http://{self.base_url}/{3232222232323232}/partner"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.delete(url, headers=headers)

        content = json.loads(response.content)
        self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # Delete federation. Federation not Found
    def test_11(self):
        """Test case for delete_federation_details

            Remove existing federation with the partner OP
        """
        url = f"http://{self.base_url}/{'65b799f576063bc1ac9e6999'}/partner"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.delete(url, headers=headers)

        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    # Delete federation
    def test_12(self):
        """Test case for delete_federation_details

            Remove existing federation with the partner OP
        """
        url = f"http://{self.base_url}/{BaseTestCase.federation}/partner"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.delete(url, headers=headers)

        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200, f'Response body is : {content}')


if __name__ == '__main__':
    import unittest
    unittest.main()
