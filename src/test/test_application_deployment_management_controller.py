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

from models.app_identifier import AppIdentifier  # noqa: E501
from models.app_provider_id import AppProviderId  # noqa: E501
from models.application_lcm_body import ApplicationLcmBody  # noqa: E501
from models.federation_context_id import FederationContextId  # noqa: E501
from models.inline_response2008 import InlineResponse2008  # noqa: E501
from models.inline_response2009 import InlineResponse2009  # noqa: E501
from models.inline_response202 import InlineResponse202  # noqa: E501
from models.instance_identifier import InstanceIdentifier  # noqa: E501
from models.problem_details import ProblemDetails  # noqa: E501
from models.zone_identifier import ZoneIdentifier  # noqa: E501
from test import BaseTestCase
import requests
from clients import i2edge
import util


class TestApplicationDeploymentManagementController(BaseTestCase):
    """ApplicationDeploymentManagementController integration test stubs"""

    BaseTestCase.federation = ""
    BaseTestCase.token = ""
    BaseTestCase.instances = []
    BaseTestCase.zone = ""
    BaseTestCase.flavour = ""

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

            # Get zone id from i2edge with flavour
            BaseTestCase.zone = self.get_first_zone_from_zone_list_i2edge()
            if BaseTestCase.zone == "":
                raise Exception("Test Failed. Unable to retrieve zone from i2edge")

            # Get flavour from zone
            BaseTestCase.flavour = self.get_flavour_from_zone(BaseTestCase.zone)
            if BaseTestCase.flavour == "":
                raise Exception("Test Failed. Unable to retrieve flavour from i2edge")

            super(TestApplicationDeploymentManagementController, self).run(result)
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

            # Create application onboarding for this federation context
            self.post_onboarding(BaseTestCase.federation, self.app_id, self.app_provider, BaseTestCase.zone, self.artefact_id,
                                 BaseTestCase.token)
        except Exception as error:
            raise Exception(f"Test failed. Reason: {error}")

    # test_install_app with zone id
    def test_01(self):
        """Test case for install_app

        Instantiates an application on a partner OP zone.
        """
        body = {
            "appId": self.app_id,
            "appVersion": "0.1.0",
            "appProviderId": self.app_provider,
            "zoneInfo": {
                "zoneId": BaseTestCase.zone,
                "flavourId": BaseTestCase.flavour,
                "resourceConsumption": "RESERVED_RES_AVOID",
                "resPool": "fdfddfdfdffdfdfd"
            },
            "appInstCallbackLink": "string"
        }
        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/lcm"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        BaseTestCase.instances.append(content)
        self.assertIn(response.status_code, [202, 422], f'Response body is : {content}')

    # test_install_app with zone id. Version already exist
    def test_02(self):
        """Test case for install_app

        Instantiates an application on a partner OP zone.
        """
        body = {
            "appId": self.app_id,
            "appVersion": "0.1.0",
            "appProviderId": self.app_provider,
            "zoneInfo": {
                "zoneId": BaseTestCase.zone,
                "flavourId": BaseTestCase.flavour,
                "resourceConsumption": "RESERVED_RES_AVOID",
                "resPool": "fdfddfdfdffdfdfd"
            },
            "appInstCallbackLink": "string"
        }
        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/lcm"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 409, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # Test case for install_app. Incorrect value for Federation
    def test_03(self):
        """Test case for install_app

        Instantiates an application on a partner OP zone.
        """
        body = {
            "appId": self.app_id,
            "appVersion": "0.1.1",
            "appProviderId": self.app_provider,
            "zoneInfo": {
                "zoneId": BaseTestCase.zone,
                "flavourId": BaseTestCase.flavour,
                "resourceConsumption": "RESERVED_RES_AVOID",
                "resPool": "fdfddfdfdffdfdfd"
            },
            "appInstCallbackLink": "string"
        }
        url = f"http://{self.base_url}/{3232222232323232}/application/lcm"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # Test case for install_app. Federation not found
    def test_04(self):
        """Test case for install_app

        Instantiates an application on a partner OP zone.
        """
        body = {
            "appId": self.app_id,
            "appVersion": "0.1.1",
            "appProviderId": self.app_provider,
            "zoneInfo": {
                "zoneId": BaseTestCase.zone,
                "flavourId": BaseTestCase.flavour,
                "resourceConsumption": "RESERVED_RES_AVOID",
                "resPool": "fdfddfdfdffdfdfd"
            },
            "appInstCallbackLink": "string"
        }
        url = f"http://{self.base_url}/{'65b799f576063bc1ac9e6999'}/application/lcm"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    # Test case for install_app. Check profile with fake app_id
    def test_05(self):
        """Test case for install_app

        Instantiates an application on a partner OP zone.
        """
        body = {
            "appId": "app_fake_id",
            "appVersion": "0.1.1",
            "appProviderId": self.app_provider,
            "zoneInfo": {
                "zoneId": BaseTestCase.zone,
                "flavourId": BaseTestCase.flavour,
                "resourceConsumption": "RESERVED_RES_AVOID",
                "resPool": "fdfddfdfdffdfdfd"
            },
            "appInstCallbackLink": "string"
        }
        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/lcm"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 404, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # Test case for install_app. Check fake zone at i2edge
    def test_06(self):
        """Test case for install_app

        Instantiates an application on a partner OP zone.
        """
        body = {
            "appId": self.app_id,
            "appVersion": "0.1.1",
            "appProviderId": self.app_provider,
            "zoneInfo": {
                "zoneId": "cdf91a6231714ab09d8ff3609cfd5uff",
                "flavourId": BaseTestCase.flavour,
                "resourceConsumption": "RESERVED_RES_AVOID",
                "resPool": "fdfddfdfdffdfdfd"
            },
            "appInstCallbackLink": "string"
        }
        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/lcm"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # Test case for install_app. Check zone and flavour. Incorrect flavour for zone
    def test_07(self):
        """Test case for install_app

        Instantiates an application on a partner OP zone.
        """
        body = {
            "appId": self.app_id,
            "appVersion": "0.1.1",
            "appProviderId": self.app_provider,
            "zoneInfo": {
                "zoneId": "08aad7a205694979b5f62c53624b97c9",
                "flavourId": BaseTestCase.flavour,
                "resourceConsumption": "RESERVED_RES_AVOID",
                "resPool": "fdfddfdfdffdfdfd"
            },
            "appInstCallbackLink": "string"
        }
        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/lcm"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # Test case for install_app. Check fake flavour if zone is blanks
    def test_08(self):
        """Test case for install_app

        Instantiates an application on a partner OP zone.
        """
        body = {
            "appId": self.app_id,
            "appVersion": "0.1.1",
            "appProviderId": self.app_provider,
            "zoneInfo": {
                "zoneId": "",
                "flavourId": "65d7a6f1b1e8031b9f3035ff",
                "resourceConsumption": "RESERVED_RES_AVOID",
                "resPool": "fdfddfdfdffdfdfd"
            },
            "appInstCallbackLink": "string"
        }
        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/lcm"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 404, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # Test case for install_app. check if exist zone for this federation at Availability Zones of the onboarding
    def test_09(self):
        """Test case for install_app

        Instantiates an application on a partner OP zone.
        """
        body = {
            "appId": self.app_id,
            "appVersion": "0.1.1",
            "appProviderId": self.app_provider,
            "zoneInfo": {
                "zoneId": "bf4090613ee1450298c5b4460154543d",
                "flavourId": BaseTestCase.flavour,
                "resourceConsumption": "RESERVED_RES_AVOID",
                "resPool": "fdfddfdfdffdfdfd"
            },
            "appInstCallbackLink": "string"
        }
        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/lcm"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # Test case for install_app. Check if the provider is the same that the provider of the app id
    def test_10(self):
        """Test case for install_app

        Instantiates an application on a partner OP zone.
        """
        body = {
            "appId": self.app_id,
            "appVersion": "0.1.1",
            "appProviderId": "fake_provider_id",
            "zoneInfo": {
                "zoneId": BaseTestCase.zone,
                "flavourId": BaseTestCase.flavour,
                "resourceConsumption": "RESERVED_RES_AVOID",
                "resPool": "fdfddfdfdffdfdfd"
            },
            "appInstCallbackLink": "string"
        }
        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/lcm"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 404, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # test_install_app without zone id
    def test_11(self):
        """Test case for install_app

        Instantiates an application on a partner OP zone.
        """
        body = {
            "appId": self.app_id,
            "appVersion": "0.1.1",
            "appProviderId": self.app_provider,
            "zoneInfo": {
                "zoneId": "",
                "flavourId": BaseTestCase.flavour,
                "resourceConsumption": "RESERVED_RES_AVOID",
                "resPool": "fdfddfdfdffdfdfd"
            },
            "appInstCallbackLink": "string"
        }
        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/lcm"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        BaseTestCase.instances.append(content)
        self.assertIn(response.status_code, [202, 422], f'Response body is : {content}')

    # Test case for get_all_app_instances.
    def test_12(self):
        """Test case for get_all_app_instances

        Retrieves all application instance of partner OP
        """
        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/lcm/app/{self.app_id}/appProvider/{self.app_provider}"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.get(url, headers=headers)

        content = json.loads(response.content)
        self.assertIn(response.status_code, [200, 422], f'Response body is: {content}')

    # Test case for get_all_app_instances. Federation Context Not Found
    def test_13(self):
        """Test case for get_all_app_instances

        Retrieves all application instance of partner OP
        """
        url = f"http://{self.base_url}/{'65b799f576063bc1ac9e6999'}/application/lcm/app/{self.app_id}/appProvider/{self.app_provider}"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.get(url, headers=headers)

        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    # Test case for get_all_app_instances. Incorrect value for Federation Context
    def test_14(self):
        """Test case for get_all_app_instances

        Retrieves all application instance of partner OP
        """
        url = f"http://{self.base_url}/{3232222232323232}/application/lcm/app/{self.app_id}/appProvider/{self.app_provider}"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.get(url, headers=headers)

        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 500, f'Response body is : {content}')

    # Test case for get_all_app_instances. Check if exist Federation Context Id and App Id in Application Onboarding
    def test_15(self):
        """Test case for get_all_app_instances

        Retrieves all application instance of partner OP
        """
        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/lcm/app/{'app_app_app'}/appProvider/{self.app_provider}"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.get(url, headers=headers)

        content = json.loads(response.content)
        self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    # Test case for get_all_app_instances. Check if exist application deployment by federation id, app Id, and app provider id
    def test_16(self):
        """Test case for get_all_app_instances

        Retrieves all application instance of partner OP
        """
        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/lcm/app/{self.app_id}/appProvider/{'provider_provider'}"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.get(url, headers=headers)

        content = json.loads(response.content)
        self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    # Test case for get_app_instance_details.
    def test_17(self):
        """Test case for get_app_instance_details

        Retrieves an application instance details from partner OP.
        """
        instance= ""
        zone_id=""
        for elem in BaseTestCase.instances:
            instance = elem.get("appInstIdentifier")
            zone_id = elem.get("zoneId")
            break

        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/lcm/app/{self.app_id}/instance/{instance}/zone/{zone_id}"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.get(url, headers=headers)

        content = json.loads(response.content)
        self.assertIn(response.status_code, [200, 422], f'Response body is: {content}')

    # Test case for get_app_instance_details. Federation Context Not Found
    def test_18(self):
        """Test case for get_app_instance_details

        Retrieves an application instance details from partner OP.
        """
        instance= ""
        zone_id=""
        for elem in BaseTestCase.instances:
            instance = elem.get("appInstIdentifier")
            zone_id = elem.get("zoneId")
            break

        url = f"http://{self.base_url}/{'65b799f576063bc1ac9e6999'}/application/lcm/app/{self.app_id}/instance/{instance}/zone/{zone_id}"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.get(url, headers=headers)

        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    # Test case for get_app_instance_details. Incorrect value for Federation Context
    def test_19(self):
        """Test case for get_app_instance_details

        Retrieves an application instance details from partner OP.
        """
        instance= ""
        zone_id=""
        for elem in BaseTestCase.instances:
            instance = elem.get("appInstIdentifier")
            zone_id = elem.get("zoneId")
            break

        url = f"http://{self.base_url}/{3232222232323232}/application/lcm/app/{self.app_id}/instance/{instance}/zone/{zone_id}"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.get(url, headers=headers)

        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 500, f'Response body is : {content}')

    # Test case for get_app_instance_details. Check if exist Federation Context Id and App Id in Application Onboarding
    def test_20(self):
        """Test case for get_app_instance_details

        Retrieves an application instance details from partner OP.
        """
        instance = ""
        zone_id = ""
        for elem in BaseTestCase.instances:
            instance = elem.get("appInstIdentifier")
            zone_id = elem.get("zoneId")
            break

        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/lcm/app/{'app_app_app'}/instance/{instance}/zone/{zone_id}"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.get(url, headers=headers)

        content = json.loads(response.content)
        self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    # Test case for get_app_instance_details. Check if exist instance id at i2edge
    def test_21(self):
        """Test case for get_app_instance_details

        Retrieves an application instance details from partner OP.
        """
        instance = ""
        zone_id = ""
        for elem in BaseTestCase.instances:
            instance = elem.get("appInstIdentifier")
            zone_id = elem.get("zoneId")
            break

        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/lcm/app/{'app_app_app'}/instance/{'instance_id'}/zone/{zone_id}"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.get(url, headers=headers)

        content = json.loads(response.content)
        self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    # Test case for get_app_instance_details. Check if exist zone id at i2edge
    def test_22(self):
        """Test case for get_app_instance_details

        Retrieves an application instance details from partner OP.
        """
        instance = ""
        zone_id = ""
        for elem in BaseTestCase.instances:
            instance = elem.get("appInstIdentifier")
            zone_id = elem.get("zoneId")
            break

        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/lcm/app/{self.app_id}/instance/{instance}/zone/{'cdf91a6231714ab09d8ff3609cfd5fff'}"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.get(url, headers=headers)

        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    # Test case for get_app_instance_details. Check if exist application deployment by federation id, app Id, instance Id and zone Id
    def test_23(self):
        """Test case for get_app_instance_details

        Retrieves an application instance details from partner OP.
        """
        instance = ""
        zone_id = ""
        for elem in BaseTestCase.instances:
            instance = elem.get("appInstIdentifier")
            zone_id = elem.get("zoneId")
            break

        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/lcm/app/{self.app_id}/instance/{instance}/zone/{'08aad7a205694979b5f62c53624b97c9'}"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.get(url, headers=headers)

        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    # Test case for remove_app.
    def test_24(self):
        """Test case for remove_app

           Terminate an application instance on a partner OP zone.
        """
        instance= ""
        zone_id=""
        for elem in BaseTestCase.instances:
            instance = elem.get("appInstIdentifier")
            zone_id = elem.get("zoneId")
            break

        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/lcm/app/{self.app_id}/instance/{instance}/zone/{zone_id}"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.delete(url, headers=headers)

        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200, f'Response body is : {content}')

    # Test case for remove_app. Federation Context Not Found
    def test_25(self):
        """Test case for remove_app

           Terminate an application instance on a partner OP zone.
        """
        instance= ""
        zone_id=""
        for elem in BaseTestCase.instances:
            instance = elem.get("appInstIdentifier")
            zone_id = elem.get("zoneId")
            break

        url = f"http://{self.base_url}/{'65b799f576063bc1ac9e6999'}/application/lcm/app/{self.app_id}/instance/{instance}/zone/{zone_id}"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.delete(url, headers=headers)

        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    # Test case for remove_app. Incorrect value for Federation Context
    def test_26(self):
        """Test case for remove_app

           Terminate an application instance on a partner OP zone.
        """
        instance= ""
        zone_id=""
        for elem in BaseTestCase.instances:
            instance = elem.get("appInstIdentifier")
            zone_id = elem.get("zoneId")
            break

        url = f"http://{self.base_url}/{3232222232323232}/application/lcm/app/{self.app_id}/instance/{instance}/zone/{zone_id}"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.delete(url, headers=headers)

        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
            self.assertEqual(response.status_code, 422, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
            self.assertEqual(response.status_code, 500, f'Response body is : {content}')

    # Test case for remove_app. Check if exist Federation Context Id and App Id in Application Onboarding
    def test_27(self):
        """Test case for remove_app

           Terminate an application instance on a partner OP zone.
        """
        instance = ""
        zone_id = ""
        for elem in BaseTestCase.instances:
            instance = elem.get("appInstIdentifier")
            zone_id = elem.get("zoneId")
            break

        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/lcm/app/{'app_app_app'}/instance/{instance}/zone/{zone_id}"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.delete(url, headers=headers)

        content = json.loads(response.content)
        self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    # Test case for remove_app. Check if exist instance id at i2edge
    def test_28(self):
        """Test case for remove_app

           Terminate an application instance on a partner OP zone.
        """
        instance = ""
        zone_id = ""
        for elem in BaseTestCase.instances:
            instance = elem.get("appInstIdentifier")
            zone_id = elem.get("zoneId")
            break

        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/lcm/app/{'app_app_app'}/instance/{'instance_id'}/zone/{zone_id}"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.delete(url, headers=headers)

        content = json.loads(response.content)
        self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    # Test case for remove_app. Check if exist zone id at i2edge
    def test_29(self):
        """Test case for remove_app

           Terminate an application instance on a partner OP zone.
        """
        instance = ""
        zone_id = ""
        for elem in BaseTestCase.instances:
            instance = elem.get("appInstIdentifier")
            zone_id = elem.get("zoneId")
            break

        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/lcm/app/{self.app_id}/instance/{instance}/zone/{'cdf91a6231714ab09d8ff3609cfd5fff'}"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.delete(url, headers=headers)

        content = json.loads(response.content)
        self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    # Test case for remove_app. Check if exist application deployment by federation id, app Id, instance Id and zone Id
    def test_30(self):
        """Test case for remove_app

           Terminate an application instance on a partner OP zone.
        """
        instance = ""
        zone_id = ""
        for elem in BaseTestCase.instances:
            instance = elem.get("appInstIdentifier")
            zone_id = elem.get("zoneId")
            break

        url = f"http://{self.base_url}/{BaseTestCase.federation}/application/lcm/app/{self.app_id}/instance/{instance}/zone/{'08aad7a205694979b5f62c53624b97c9'}"

        headers = {"Content-Type": "application/json; accept=application/json",
                   "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.delete(url, headers=headers)

        content = json.loads(response.content)
        self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    def test_31(self):

        # Delete instances
        for elem in BaseTestCase.instances:
            self.delete_deployments(BaseTestCase.federation, self.app_id, elem.get("appInstIdentifier"),
                                    elem.get("zoneId"), BaseTestCase.token)

        # Delete onboarding
        self.delete_onboarding(BaseTestCase.federation, self.app_id, BaseTestCase.token)

        # Delete artefact
        self.delete_artefact(BaseTestCase.federation, self.artefact_id, BaseTestCase.token)

        # Delete zone
        self.delete_zone(BaseTestCase.federation, BaseTestCase.zone, BaseTestCase.token)

        # Delete federation
        self.delete_federation(BaseTestCase.federation, BaseTestCase.token)

if __name__ == '__main__':
    import unittest
    unittest.main()
