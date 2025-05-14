import logging

import connexion
import requests
import random
from flask_testing import TestCase

from encoder import JSONEncoder

from configparser import ConfigParser
from clients import i2edge
import util

CONFIG = ConfigParser()
CONFIG.read("conf/config.cfg")
HOST = CONFIG.get("server", "host")
PORT = int(CONFIG.get("server", "port"))
CLIENT_ID = CONFIG.get("keycloak", "client1_id")
CLIENT_SECRET = CONFIG.get("keycloak", "client1_secret")
SERVER = "/operatorplatform/federation/v1"
HOST_KEYCLOAK = CONFIG.get("keycloak", "host")
PORT_KEYCLOAK = int(CONFIG.get("keycloak", "port"))
ROLE_OP = CONFIG.get("partner_op", "role")
HOST_ORIGINATING_OP = CONFIG.get("partner_op", "partner_op_host")
SERVER_ORIGINATING_OP = CONFIG.get("partner_op", "partner_op_server")
PORT_ORIGINATING_OP = int(CONFIG.get("partner_op", "partner_op_port"))


class BaseTestCase(TestCase):

    def create_app(self):
        #logging.getLogger('connexion.operation').setLevel('ERROR')
        logging.basicConfig(level=logging.ERROR)
        app = connexion.App(__name__, specification_dir='../swagger/')
        app.app.json_encoder = JSONEncoder
        app.add_api('swagger.yaml')

        # keycloak
        self.client_id = CLIENT_ID
        self.client_secret = CLIENT_SECRET

        # Base url application server
        self.base_url = f"{HOST}:{PORT}{SERVER}"

        self.artefact_id = "3fa85f64-5717-4562-b3fc-222222222222"
        self.app_provider = "test_app_providerid"
        self.app_id = "test_app_id"
        self.artefact_name = "3fa85f64-5717-4562-b3fc-222222222222"
        self.artefact_version = "0.3.0"
        self.artefact_file = "H4sIAAAAAAAAA+1XUW/bNhDOs37FzXlZi0qWZEne/FYkAzag3YpmCDAMxUBLtMxGEjmScupl6W/fUYoc2bEXxxkSDOH3QInH492RxyPvRjPyXTxLIjceB2M3ipPQnY5mqRv2MDx6HHzEeBybbzCO/f63w1EQJYEfhUGSIF8QhXF4BPEj9e6FWmkiAY4+c5mxf+G7b/x/itE+/vfmtChZXnFJD9FhHJxE0U7/x6MY/Y+qkxGSQ/R/EgXof/+/Xuw2vHD/H8MHojWVlQLNofUxXM5pBdOaFRmrchAkvSA5VZ5zDL/OmQJVC8Glxh88FwXkBZ9CSXQ6R+43IGlBNFtQnKfnPTqpMhRQ0RxHeQXfCkln7AvN4JIh3zevPPilKpbAq2amMQkElVCwinqOd3r2x5lG21DECS9LFHB+cgYZk8rxcqaHTdua73jTv+SwaTvCPB+apuuqRTW8FTTF9dUCZqygynntqUuB7ZRcYKtL889RjvP6K844J5LxWsFPpz+gXiH5Z5pqx2MZJcOWHUmOt1Apz+jQeW7n7oG94n9Bihr9vyRlcYiO++I/SMZ34h/Zbfw/AY6h51xHUlGwlJzwutITCJwKj/EZLfCQczmBq2unIiVVeCHQiVPSksvlWyEmTirqj/RPlKI78qqLQ+9YyVYDN53nXrbFDfaK/5M5kfrg8G/jP9kd/2EwMvnfOI6DsKEHSejb9/9JQAQ7p1LhizyBRegQIVbdwAs838moSiUTuiG9hR8xE4TUnAeYcQlLXkv4wDN89RX+prS5ISawz7FyFp0m3/seNT33VrxI7BX/mpYCkzqqDqsE96z/kMcfjaJxE/9xYuu/p8AD/d8+4q5sn/c9n4R78r8wiKOm/g8jdL+PfGEYhIm9/58C/fsfL381XATOBauyCZxiLsiXJa00pm6aZESTiQOI9oa/ugLvI6aGRFHvZ6TA35DRGakLDQM8KXoA19cr9jZlbOact+nmiro5z9CCZrISNG013qSlyqSkpq+6lLTpGTRl5jsypYW6JRrgmvaz1b052hl+Ggndoe8pWduGDsUWrY/T3CxxtfgOG7l4byt7Ayhf898wKvGnQjei9yBIOld0SHmlCdbVcsNs9wG+3Wp1C1aSHKUIjrV7/WWoNCYHaoOnyxe2bJwZbK6XrWON/aKewKC3BbcFSN9U3wuNpYMdUtoFrAtaq176sgLff892SStMUfMga5syaN3W6DBb70gKd1ma8rIkJrJ/H7QuGXza4CAyV2bYdRfl4A0u2jSm406X6HfTu6MfC8C1fYr9943ybuacVHkr69Nz33UWFhYWFhYWFhYWFhYWFhYWLxH/AEh4YrAAKAAA"

        self.roleOp = ROLE_OP
        # Base url application server originating op
        self.base_url_originating_op = f"{HOST_ORIGINATING_OP}:{PORT_ORIGINATING_OP}{SERVER_ORIGINATING_OP}"

        return app.app

    def get_access_token(self):
        # URL to obtain access token from Keycloak
        token_url = f"http://{HOST_KEYCLOAK}:{PORT_KEYCLOAK}/auth/realms/mec-federation/protocol/openid-connect/token"

        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials"
        }

        # POST to  obtain access token
        response = requests.post(token_url, data=payload)

        # Returns access token
        return response.json()["access_token"]

    def post_federation_context(self, token):
        federation_context_id = ""

        url = f"http://{self.base_url}/partner"
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
        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {token}"}
        response = requests.post(url, headers=headers, json=body)
        assert response.status_code == 200
        data_response = response.json()
        federation_context_id = data_response.get("federationContextId")

        return federation_context_id

    def post_availability_zones(self, federation_context_id, zone_id, token):

        url = f"http://{self.base_url}/{federation_context_id}/zones"
        body = {
              "acceptedAvailabilityZones": [
                zone_id
              ],
              "availZoneNotifLink": "string"
        }
        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {token}"}
        response = requests.post(url, headers=headers, json=body)
        assert response.status_code == 200

        return

    def post_artefact(self, federation_context_id, artefact_id, app_provider, token):

        url = f"http://{self.base_url}/{federation_context_id}/artefact"
        body = {
          "artefactId": artefact_id,
          "appProviderId": app_provider,
          "artefactName": self.artefact_name,
          "artefactVersionInfo": self.artefact_version,
          "artefactDescription": "string",
          "artefactVirtType": "VM_TYPE",
          "artefactFileName": "string",
          "artefactFileFormat": "WINZIP",
          "artefactDescriptorType": "HELM",
          "repoType": util.RepoType.UPLOAD.value,
          "artefactRepoLocation": {
            "repoURL": "string",
            "userName": "string",
            "password": "string",
            "token": "string"
          },
          "artefactFile": self.artefact_file,
          "componentSpec": [
            {
              "componentName": "string",
              "images": [
                "3fa85f64-5717-4562-b3fc-2c963f66afa6"
              ],
              "numOfInstances": 0,
              "restartPolicy": "RESTART_POLICY_ALWAYS",
              "commandLineParams": {
                "command": [
                  "string"
                ],
                "commandArgs": [
                  "string"
                ]
              },
              "exposedInterfaces": [
                {
                  "interfaceId": "string",
                  "commProtocol": "TCP",
                  "commPort": 0,
                  "visibilityType": "VISIBILITY_EXTERNAL",
                  "network": "string",
                  "InterfaceName": "string"
                }
              ],
              "computeResourceProfile": {
                "cpuArchType": "ISA_X86_64",
                "numCPU": {
                  "whole": {
                    "value": 2
                  },
                  "decimal": {
                    "value": 0.5
                  },
                  "millivcpu": {
                    "value": "500m"
                  }
                },
                "memory": 0,
                "diskStorage": 0,
                "gpu": [
                  {
                    "gpuVendorType": "GPU_PROVIDER_NVIDIA",
                    "gpuModeName": "string",
                    "gpuMemory": 0,
                    "numGPU": 0
                  }
                ],
                "vpu": 0,
                "fpga": 0,
                "hugepages": [
                  {
                    "pageSize": "2MB",
                    "number": 0
                  }
                ],
                "cpuExclusivity": True
              },
              "compEnvParams": [
                {
                  "envVarName": "string",
                  "envValueType": "USER_DEFINED",
                  "envVarValue": "string",
                  "envVarSrc": "string"
                }
              ],
              "deploymentConfig": {
                "configType": "DOCKER_COMPOSE",
                "contents": "string"
              },
              "persistentVolumes": [
                {
                  "volumeSize": "10Gi",
                  "volumeMountPath": "string",
                  "volumeName": "string",
                  "ephemeralType": False,
                  "accessMode": "RW",
                  "sharingPolicy": "EXCLUSIVE"
                }
              ]
            }
          ]
        }
        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {token}"}
        response = requests.post(url, headers=headers, json=body)
        assert response.status_code == 200

        return

    def post_onboarding(self, federation_context_id, app_id, app_provider, zone_id, artefact_id, token):
        url = f"http://{self.base_url}/{federation_context_id}/application/onboarding"
        body = {
          "appId": app_id,
          "appProviderId": app_provider,
          "appDeploymentZones": [
            zone_id
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
              "artefactId": artefact_id
            }
          ],
          "appStatusCallbackLink": "string"
        }
        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {token}"}
        response = requests.post(url, headers=headers, json=body)
        assert response.status_code == 202

        return

    def delete_deployments(self, federation_id, app_id, instance_id, zone_id, token):

        url = f"http://{self.base_url}/{federation_id}/application/lcm/app/{app_id}/instance/{instance_id}/zone/{zone_id}"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {token}"}
        response = requests.delete(url, headers=headers)

        return

    def delete_onboarding(self, federation_id, app_id, token):

        url = f"http://{self.base_url}/{federation_id}/application/onboarding/app/{app_id}"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {token}"}
        response = requests.delete(url, headers=headers)

        return

    def delete_artefact(self, federation_id, artefact_id, token):

        url = f"http://{self.base_url}/{federation_id}/artefact/{artefact_id}"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {token}"}
        response = requests.delete(url, headers=headers)

        return

    def delete_zone(self, federation_id, zone_id, token):

        url = f"http://{self.base_url}/{federation_id}/zones/{zone_id}"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {token}"}
        response = requests.delete(url, headers=headers)

        return

    def delete_federation(self, federation_id, token):

        url = f"http://{self.base_url}/{federation_id}/partner"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {token}"}
        response = requests.delete(url, headers=headers)

        return

    def get_federation(self, federation_id, token):

        url = f"http://{self.base_url}/{federation_id}/partner"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {token}"}
        response = requests.get(url, headers=headers)

        return response.json()

    def get_first_zone_from_zone_list_i2edge(self):
        zone_selected = ""

        try:
            # Get zone list
            zones_list = i2edge.get_zones()

            for zone in zones_list:
                # If the zone value is a dict, is a correct zone, else there is an issue and returns a str
                if isinstance(zone, dict):
                    flavours = zone.get("flavoursSupported")
                    if len(flavours) > 0:
                        zone_selected = zone.get("zoneId")
                        break
        except:
            zone_selected = ""

        return zone_selected

    def get_flavour_from_zone(self, zone_id):
        flavour_selected = ""

        try:
            # Get zone from i2edge
            zone = i2edge.get_zone_by_zone_id(zone_id)

            flavours = zone.get("flavoursSupported")
            if len(flavours) > 0:
                for f in flavours:
                    flavour_selected = f.get("flavourId")
                    break
        except:
            flavour_selected = ""

        return flavour_selected

    def get_federation_resources(self, token):

        url = f"http://{self.base_url}/federation-resources"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {token}"}
        response = requests.get(url, headers=headers)

        return response.json()

    def get_federation_resources_originating_op(self, token):

        url = f"http://{self.base_url_originating_op}/federation-resources"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {token}"}
        response = requests.get(url, headers=headers)

        return response.json()
