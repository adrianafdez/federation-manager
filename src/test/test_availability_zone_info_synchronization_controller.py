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

from models.federation_context_id import FederationContextId  # noqa: E501
from models.problem_details import ProblemDetails  # noqa: E501
from models.zone_identifier import ZoneIdentifier  # noqa: E501
from models.zone_registered_data import ZoneRegisteredData  # noqa: E501
from models.zone_registration_request_data import ZoneRegistrationRequestData  # noqa: E501
from models.zone_registration_response_data import ZoneRegistrationResponseData  # noqa: E501
from test import BaseTestCase
import requests
from clients import i2edge
import util


class TestAvailabilityZoneInfoSynchronizationController(BaseTestCase):
    """AvailabilityZoneInfoSynchronizationController integration test stubs"""

    BaseTestCase.federation = ""
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

            # Check if there is connection with FM ORIGINATING OP. Otherwise stop the test
            if self.roleOp == util._ROLE_ORIGINATING_OP:
                self.assertRaises(Exception, self.get_federation_resources_originating_op(BaseTestCase.token))

            # Get zone id from i2edge
            BaseTestCase.zone = self.get_first_zone_from_zone_list_i2edge()
            if BaseTestCase.zone == "":
                raise Exception("Test Failed. Unable to retrieve zone from i2edge")

            super(TestAvailabilityZoneInfoSynchronizationController, self).run(result)
        except Exception as error:
            raise Exception(f"Test failed. Reason: {error}")

    def test_00(self):

        try:
            # Create federation context
            BaseTestCase.federation = self.post_federation_context(BaseTestCase.token)

        except Exception as error:
            raise Exception(f"Test failed. Reason: {error}")

    # Subscribe zone to federation
    def test_01(self):
        """Test case for zone_subscribe

             Originating OP informs partner OP that it is willing to access the specified zones and partner OP shall reserve compute and network resources for these zones.
        """

        body = {
          "acceptedAvailabilityZones": [
            BaseTestCase.zone
          ],
          "availZoneNotifLink": "string"
        }
        url = f"http://{self.base_url}/{BaseTestCase.federation}/zones"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200, f'Response body is : {content}')

    # Subscribe zone to federation. Federation not found
    def test_02(self):
        """Test case for zone_subscribe

             Originating OP informs partner OP that it is willing to access the specified zones and partner OP shall reserve compute and network resources for these zones.
        """

        body = {
          "acceptedAvailabilityZones": [
            BaseTestCase.zone
          ],
          "availZoneNotifLink": "string"
        }
        url = f"http://{self.base_url}/{'65b799f576063bc1ac9e6999'}/zones"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    # Subscribe zone to federation. Incorrect value for Federation
    def test_03(self):
        """Test case for zone_subscribe

             Originating OP informs partner OP that it is willing to access the specified zones and partner OP shall reserve compute and network resources for these zones.
        """

        body = {
          "acceptedAvailabilityZones": [
            BaseTestCase.zone
          ],
          "availZoneNotifLink": "string"
        }
        url = f"http://{self.base_url}/{3232222232323232}/zones"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # Subscribe zone to federation. Check if exist zone in i2edge
    def test_04(self):
        """Test case for zone_subscribe

             Originating OP informs partner OP that it is willing to access the specified zones and partner OP shall reserve compute and network resources for these zones.
        """

        body = {
          "acceptedAvailabilityZones": [
            "cdf91a6231714ab09d8ff3609cfd5fff"
          ],
          "availZoneNotifLink": "string"
        }
        url = f"http://{self.base_url}/{BaseTestCase.federation}/zones"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # Subscribe zone to federation. Check if zone already exist fir federation
    def test_05(self):
        """Test case for zone_subscribe

             Originating OP informs partner OP that it is willing to access the specified zones and partner OP shall reserve compute and network resources for these zones.
        """

        body = {
          "acceptedAvailabilityZones": [
            BaseTestCase.zone
          ],
          "availZoneNotifLink": "string"
        }
        url = f"http://{self.base_url}/{BaseTestCase.federation}/zones"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 409, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # Get zone by federation.
    def test_06(self):
        """Test case for get_zone_data

             Retrieves details about the computation and network resources that partner OP has reserved for this zone.
        """

        url = f"http://{self.base_url}/{BaseTestCase.federation}/zones/{BaseTestCase.zone}"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.get(url, headers=headers)
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200, f'Response body is : {content}')

    # Get zone by federation. Federation not found
    def test_07(self):
        """Test case for get_zone_data

             Retrieves details about the computation and network resources that partner OP has reserved for this zone.
        """

        url = f"http://{self.base_url}/{'65b799f576063bc1ac9e6999'}/zones/{BaseTestCase.zone}"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.get(url, headers=headers)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    # Get zone by federation. Incorrect value for Federation
    def test_08(self):
        """Test case for get_zone_data

             Retrieves details about the computation and network resources that partner OP has reserved for this zone.
        """

        url = f"http://{self.base_url}/{3232222232323232}/zones/{BaseTestCase.zone}"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.get(url, headers=headers)
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # Get zone by federation. Check if exist zone in i2edge
    def test_09(self):
        """Test case for get_zone_data

             Retrieves details about the computation and network resources that partner OP has reserved for this zone.
        """

        url = f"http://{self.base_url}/{BaseTestCase.federation}/zones/{'cdf91a6231714ab09d8ff3609cfd5fff'}"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.get(url, headers=headers)
        content = json.loads(response.content)
        self.assertIn(response.status_code, [404, 422], f'Response body is : {content}')

    # Get zone by federation. Check if Zone id is in the list of availability zones by federation
    def test_10(self):
        """Test case for get_zone_data

             Retrieves details about the computation and network resources that partner OP has reserved for this zone.
        """

        url = f"http://{self.base_url}/{BaseTestCase.federation}/zones/{'08aad7a205694979b5f62c53624b97c9'}"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.get(url, headers=headers)
        content = json.loads(response.content)
        self.assertIn(response.status_code, [404, 422], f'Response body is : {content}')

    # Delete zone by federation. Federation not found
    def test_11(self):
        """Test case for zone_unsubscribe

         Assert usage of a partner OP zone. Originating OP informs partner OP that it will no longer access the specified zone.
        """
        url = f"http://{self.base_url}/{'65b799f576063bc1ac9e6999'}/zones/{BaseTestCase.zone}"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.delete(url, headers=headers)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    # Delete zone by federation. Incorrect value for Federation
    def test_12(self):
        """Test case for zone_unsubscribe

         Assert usage of a partner OP zone. Originating OP informs partner OP that it will no longer access the specified zone.
        """

        url = f"http://{self.base_url}/{3232222232323232}/zones/{BaseTestCase.zone}"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.delete(url, headers=headers)
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # # Delete zone by federation. Check if exist zone in i2edge
    # def test_13(self):
    #     """Test case for zone_unsubscribe
    #
    #      Assert usage of a partner OP zone. Originating OP informs partner OP that it will no longer access the specified zone.
    #     """
    #
    #     url = f"http://{self.base_url}/{BaseTestCase.federation}/zones/{'cdf91a6231714ab09d8ff3609cfd5fff'}"
    #
    #     headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}
    #
    #     response = requests.delete(url, headers=headers)
    #     content = json.loads(response.content)
    #     self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    # Delete zone by federation. Check if Zone id is in the list of availability zones by federation
    def test_14(self):
        """Test case for zone_unsubscribe

         Assert usage of a partner OP zone. Originating OP informs partner OP that it will no longer access the specified zone.
        """

        url = f"http://{self.base_url}/{BaseTestCase.federation}/zones/{'08aad7a205694979b5f62c53624b97c9'}"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.delete(url, headers=headers)
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    # Delete zone by federation.
    def test_15(self):
        """Test case for zone_unsubscribe

         Assert usage of a partner OP zone. Originating OP informs partner OP that it will no longer access the specified zone.
        """

        url = f"http://{self.base_url}/{BaseTestCase.federation}/zones/{BaseTestCase.zone}"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.delete(url, headers=headers)
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200, f'Response body is : {content}')

    def test_16(self):

        # Delete federation
        self.delete_federation(BaseTestCase.federation, BaseTestCase.token)


if __name__ == '__main__':
    import unittest
    unittest.main()
