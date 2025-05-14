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
import util


class TestArtefactManagementController(BaseTestCase):
    """ArtefactManagementController integration test stubs"""

    BaseTestCase.federation = ""
    BaseTestCase.federation2 = ""
    BaseTestCase.token = ""
    BaseTestCase.artefact_upload = ""
    BaseTestCase.artefact_public = "3fa85f64-5717-4562-b3fc-333333333333"
    BaseTestCase.artefact_private = "3fa85f64-5717-4562-b3fc-444444444444"
    BaseTestCase.artefact_name_upload = ""
    BaseTestCase.artefact_name_public = "hello-world"
    BaseTestCase.artefact_name_private = "orchestrator"
    BaseTestCase.artefact_file_encoded = ""
    BaseTestCase.artefact_version_info_upload = ""
    BaseTestCase.artefact_version_info_public = "0.8.0"
    BaseTestCase.artefact_version_info_private = "0.1.0"

    def run(self, result=None):
        """ Stop after first error """
        try:
            BaseTestCase.artefact_upload = self.artefact_id
            BaseTestCase.artefact_version_info_upload = self.artefact_version
            BaseTestCase.artefact_name_upload = self.artefact_name
            BaseTestCase.artefact_file_encoded = self.artefact_file

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

            super(TestArtefactManagementController, self).run(result)
        except Exception as error:
            raise Exception(f"Test failed. Reason: {error}")

    def test_00(self):

        try:
            # Check it the artefacts id of this test have been created previously at i2edge and remains there due
            # to a possible issue of the same test
            i2edge.delete_artefact(BaseTestCase.artefact_upload)
            i2edge.delete_artefact(BaseTestCase.artefact_public)
            i2edge.delete_artefact(BaseTestCase.artefact_private)

            # Create federation context
            BaseTestCase.federation = self.post_federation_context(BaseTestCase.token)

            # Get token from keycloak
            BaseTestCase.token = self.get_access_token()

            # Create federation context
            BaseTestCase.federation2 = self.post_federation_context(BaseTestCase.token)

        except Exception as error:
            raise Exception(f"Test failed. Reason: {error}")

    # Upload artefact. UPLOAD option to upload artefact file. Provider is mandatory
    def test_01(self):
        """Test case for upload_artefact

            Uploads application artefact on partner OP. Artefact is a zip file containing scripts and/or packaging files
            like Terraform or Helm which are required to create an instance of an application.
            """
        body = {
          "artefactId": BaseTestCase.artefact_upload,
          "appProviderId": "",
          "artefactName": BaseTestCase.artefact_name_upload,
          "artefactVersionInfo": BaseTestCase.artefact_version_info_upload,
          "artefactDescription": "string",
          "artefactVirtType": "VM_TYPE",
          "artefactFileName": "string",
          "artefactFileFormat": "WINZIP",
          "artefactDescriptorType": "HELM",
          "repoType": util.RepoType.UPLOAD.value,
          "artefactRepoLocation": {
            "repoURL": "",
            "userName": "",
            "password": "",
            "token": ""
          },
          "artefactFile": BaseTestCase.artefact_file_encoded,
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
        url = f"http://{self.base_url}/{BaseTestCase.federation}/artefact"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
          self.assertEqual(response.status_code, 400, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
          self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # Upload artefact. UPLOAD option to upload artefact file. Artefact name is mandatory
    def test_02(self):
        """Test case for upload_artefact

            Uploads application artefact on partner OP. Artefact is a zip file containing scripts and/or packaging files
            like Terraform or Helm which are required to create an instance of an application.
            """
        body = {
          "artefactId": BaseTestCase.artefact_upload,
          "appProviderId": self.app_provider,
          "artefactName": "",
          "artefactVersionInfo": BaseTestCase.artefact_version_info_upload,
          "artefactDescription": "string",
          "artefactVirtType": "VM_TYPE",
          "artefactFileName": "string",
          "artefactFileFormat": "WINZIP",
          "artefactDescriptorType": "HELM",
          "repoType": util.RepoType.UPLOAD.value,
          "artefactRepoLocation": {
            "repoURL": "",
            "userName": "",
            "password": "",
            "token": ""
          },
          "artefactFile": BaseTestCase.artefact_file_encoded,
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
        url = f"http://{self.base_url}/{BaseTestCase.federation}/artefact"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
          self.assertEqual(response.status_code, 400, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
          self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # Upload artefact. UPLOAD option to upload artefact file. Artefact file is mandatory
    def test_03(self):
        """Test case for upload_artefact

            Uploads application artefact on partner OP. Artefact is a zip file containing scripts and/or packaging files
            like Terraform or Helm which are required to create an instance of an application.
            """
        body = {
          "artefactId": BaseTestCase.artefact_upload,
          "appProviderId": self.app_provider,
          "artefactName": BaseTestCase.artefact_name_upload,
          "artefactVersionInfo": BaseTestCase.artefact_version_info_upload,
          "artefactDescription": "string",
          "artefactVirtType": "VM_TYPE",
          "artefactFileName": "string",
          "artefactFileFormat": "WINZIP",
          "artefactDescriptorType": "HELM",
          "repoType": util.RepoType.UPLOAD.value,
          "artefactRepoLocation": {
            "repoURL": "",
            "userName": "",
            "password": "",
            "token": ""
          },
          "artefactFile": "",
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
        url = f"http://{self.base_url}/{BaseTestCase.federation}/artefact"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
          self.assertEqual(response.status_code, 400, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
          self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # Upload artefact. PUBLICREPO option to indicate public repo info. Repo URL is mandatory
    def test_04(self):
        """Test case for upload_artefact

            Uploads application artefact on partner OP. Artefact is a zip file containing scripts and/or packaging files
            like Terraform or Helm which are required to create an instance of an application.
            """
        body = {
          "artefactId": BaseTestCase.artefact_public,
          "appProviderId": self.app_provider,
          "artefactName": BaseTestCase.artefact_name_public,
          "artefactVersionInfo": BaseTestCase.artefact_version_info_public,
          "artefactDescription": "string",
          "artefactVirtType": "VM_TYPE",
          "artefactFileName": "string",
          "artefactFileFormat": "WINZIP",
          "artefactDescriptorType": "HELM",
          "repoType": util.RepoType.PUBLIC.value,
          "artefactRepoLocation": {
            "repoURL": "",
            "userName": "",
            "password": "",
            "token": ""
          },
          "artefactFile": "",
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
        url = f"http://{self.base_url}/{BaseTestCase.federation}/artefact"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
          self.assertEqual(response.status_code, 400, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
          self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # Upload artefact. PRIVATEREPO option to indicate private repo info. Repo URL is mandatory
    def test_05(self):
        """Test case for upload_artefact

            Uploads application artefact on partner OP. Artefact is a zip file containing scripts and/or packaging files
            like Terraform or Helm which are required to create an instance of an application.
            """
        body = {
          "artefactId": BaseTestCase.artefact_private,
          "appProviderId": self.app_provider,
          "artefactName": BaseTestCase.artefact_name_private,
          "artefactVersionInfo": BaseTestCase.artefact_version_info_private,
          "artefactDescription": "string",
          "artefactVirtType": "VM_TYPE",
          "artefactFileName": "string",
          "artefactFileFormat": "WINZIP",
          "artefactDescriptorType": "HELM",
          "repoType": util.RepoType.PRIVATE.value,
          "artefactRepoLocation": {
            "repoURL": "",
            "userName": "i2edge",
            "password": "3wZztr7cLvypoCCCdwJt",
            "token": ""
          },
          "artefactFile": "",
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
        url = f"http://{self.base_url}/{BaseTestCase.federation}/artefact"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
          self.assertEqual(response.status_code, 400, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
          self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # Upload artefact. PRIVATEREPO option to indicate private repo info. Credentials or token are mandatory
    def test_06(self):
        """Test case for upload_artefact

            Uploads application artefact on partner OP. Artefact is a zip file containing scripts and/or packaging files
            like Terraform or Helm which are required to create an instance of an application.
            """
        body = {
          "artefactId": BaseTestCase.artefact_private,
          "appProviderId": self.app_provider,
          "artefactName": BaseTestCase.artefact_name_private,
          "artefactVersionInfo": BaseTestCase.artefact_version_info_private,
          "artefactDescription": "string",
          "artefactVirtType": "VM_TYPE",
          "artefactFileName": "string",
          "artefactFileFormat": "WINZIP",
          "artefactDescriptorType": "HELM",
          "repoType": util.RepoType.PRIVATE.value,
          "artefactRepoLocation": {
            "repoURL": "https://gitlab.i2cat.net/api/v4/projects/1458/packages/helm/stable",
            "userName": "",
            "password": "",
            "token": ""
          },
          "artefactFile": "",
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
        url = f"http://{self.base_url}/{BaseTestCase.federation}/artefact"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
          self.assertEqual(response.status_code, 400, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
          self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # Upload artefact. PRIVATEREPO option to indicate private repo info. User without password
    def test_07(self):
        """Test case for upload_artefact

            Uploads application artefact on partner OP. Artefact is a zip file containing scripts and/or packaging files
            like Terraform or Helm which are required to create an instance of an application.
            """
        body = {
          "artefactId": BaseTestCase.artefact_private,
          "appProviderId": self.app_provider,
          "artefactName": BaseTestCase.artefact_name_private,
          "artefactVersionInfo": BaseTestCase.artefact_version_info_private,
          "artefactDescription": "string",
          "artefactVirtType": "VM_TYPE",
          "artefactFileName": "string",
          "artefactFileFormat": "WINZIP",
          "artefactDescriptorType": "HELM",
          "repoType": util.RepoType.PRIVATE.value,
          "artefactRepoLocation": {
            "repoURL": "https://gitlab.i2cat.net/api/v4/projects/1458/packages/helm/stable",
            "userName": "i2edge",
            "password": "",
            "token": ""
          },
          "artefactFile": "",
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
        url = f"http://{self.base_url}/{BaseTestCase.federation}/artefact"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
          self.assertEqual(response.status_code, 400, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
          self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # Upload artefact. PRIVATEREPO option to indicate private repo info. Password without user
    def test_08(self):
        """Test case for upload_artefact

            Uploads application artefact on partner OP. Artefact is a zip file containing scripts and/or packaging files
            like Terraform or Helm which are required to create an instance of an application.
            """
        body = {
          "artefactId": BaseTestCase.artefact_private,
          "appProviderId": self.app_provider,
          "artefactName": BaseTestCase.artefact_name_private,
          "artefactVersionInfo": BaseTestCase.artefact_version_info_private,
          "artefactDescription": "string",
          "artefactVirtType": "VM_TYPE",
          "artefactFileName": "string",
          "artefactFileFormat": "WINZIP",
          "artefactDescriptorType": "HELM",
          "repoType": util.RepoType.PRIVATE.value,
          "artefactRepoLocation": {
            "repoURL": "https://gitlab.i2cat.net/api/v4/projects/1458/packages/helm/stable",
            "userName": "",
            "password": "3wZztr7cLvypoCCCdwJt",
            "token": ""
          },
          "artefactFile": "",
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
        url = f"http://{self.base_url}/{BaseTestCase.federation}/artefact"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
          self.assertEqual(response.status_code, 400, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
          self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # Upload artefact. UPLOAD option to upload artefact file
    def test_09(self):
        """Test case for upload_artefact

            Uploads application artefact on partner OP. Artefact is a zip file containing scripts and/or packaging files
            like Terraform or Helm which are required to create an instance of an application.
            """
        body = {
          "artefactId": BaseTestCase.artefact_upload,
          "appProviderId": self.app_provider,
          "artefactName": BaseTestCase.artefact_name_upload,
          "artefactVersionInfo": BaseTestCase.artefact_version_info_upload,
          "artefactDescription": "string",
          "artefactVirtType": "VM_TYPE",
          "artefactFileName": "string",
          "artefactFileFormat": "WINZIP",
          "artefactDescriptorType": "HELM",
          "repoType": util.RepoType.UPLOAD.value,
          "artefactRepoLocation": {
            "repoURL": "",
            "userName": "",
            "password": "",
            "token": ""
          },
          "artefactFile": BaseTestCase.artefact_file_encoded,
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
        url = f"http://{self.base_url}/{BaseTestCase.federation}/artefact"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        self.assertIn(response.status_code, [200, 409], f'Response body is : {content}')

    # Upload artefact. UPLOAD option to upload artefact file
    # Check if exist Federation Context Id and Artefact Id in Artefact Management
    def test_10(self):
        """Test case for upload_artefact

            Uploads application artefact on partner OP. Artefact is a zip file containing scripts and/or packaging files
            like Terraform or Helm which are required to create an instance of an application.
            """
        body = {
          "artefactId": BaseTestCase.artefact_upload,
          "appProviderId": self.app_provider,
          "artefactName": BaseTestCase.artefact_name_upload,
          "artefactVersionInfo": BaseTestCase.artefact_version_info_upload,
          "artefactDescription": "string",
          "artefactVirtType": "VM_TYPE",
          "artefactFileName": "string",
          "artefactFileFormat": "WINZIP",
          "artefactDescriptorType": "HELM",
          "repoType": util.RepoType.UPLOAD.value,
          "artefactRepoLocation": {
            "repoURL": "",
            "userName": "",
            "password": "",
            "token": ""
          },
          "artefactFile": BaseTestCase.artefact_file_encoded,
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
        url = f"http://{self.base_url}/{BaseTestCase.federation}/artefact"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
          self.assertEqual(response.status_code, 409, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
          self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # Upload artefact. UPLOAD option to upload artefact file
    # Check if exist artefact id in the database. If found artefact id belongs to another federation
    def test_11(self):
        """Test case for upload_artefact

            Uploads application artefact on partner OP. Artefact is a zip file containing scripts and/or packaging files
            like Terraform or Helm which are required to create an instance of an application.
            """
        body = {
          "artefactId": BaseTestCase.artefact_upload,
          "appProviderId": self.app_provider,
          "artefactName": BaseTestCase.artefact_name_upload,
          "artefactVersionInfo": BaseTestCase.artefact_version_info_upload,
          "artefactDescription": "string",
          "artefactVirtType": "VM_TYPE",
          "artefactFileName": "string",
          "artefactFileFormat": "WINZIP",
          "artefactDescriptorType": "HELM",
          "repoType": util.RepoType.UPLOAD.value,
          "artefactRepoLocation": {
            "repoURL": "",
            "userName": "",
            "password": "",
            "token": ""
          },
          "artefactFile": BaseTestCase.artefact_file_encoded,
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
        url = f"http://{self.base_url}/{BaseTestCase.federation2}/artefact"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
          self.assertEqual(response.status_code, 409, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
          self.assertEqual(response.status_code, 422, f'Response body is : {content}')


    # Upload artefact. PUBLICREPO option to indicate public repo info
    def test_12(self):
        """Test case for upload_artefact

            Uploads application artefact on partner OP. Artefact is a zip file containing scripts and/or packaging files
            like Terraform or Helm which are required to create an instance of an application.
            """
        body = {
          "artefactId": BaseTestCase.artefact_public,
          "appProviderId": self.app_provider,
          "artefactName": BaseTestCase.artefact_name_public,
          "artefactVersionInfo": BaseTestCase.artefact_version_info_public,
          "artefactDescription": "string",
          "artefactVirtType": "VM_TYPE",
          "artefactFileName": "string",
          "artefactFileFormat": "WINZIP",
          "artefactDescriptorType": "HELM",
          "repoType": util.RepoType.PUBLIC.value,
          "artefactRepoLocation": {
            "repoURL": "https://helm.github.io/examples",
            "userName": "",
            "password": "",
            "token": ""
          },
          "artefactFile": "",
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
        url = f"http://{self.base_url}/{BaseTestCase.federation}/artefact"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        self.assertIn(response.status_code, [200, 409], f'Response body is : {content}')

    # Upload artefact. PRIVATEREPO option to indicate private repo info
    def test_13(self):
        """Test case for upload_artefact

            Uploads application artefact on partner OP. Artefact is a zip file containing scripts and/or packaging files
            like Terraform or Helm which are required to create an instance of an application.
            """
        body = {
          "artefactId": BaseTestCase.artefact_private,
          "appProviderId": self.app_provider,
          "artefactName": BaseTestCase.artefact_name_private,
          "artefactVersionInfo": BaseTestCase.artefact_version_info_private,
          "artefactDescription": "string",
          "artefactVirtType": "VM_TYPE",
          "artefactFileName": "string",
          "artefactFileFormat": "WINZIP",
          "artefactDescriptorType": "HELM",
          "repoType": util.RepoType.PRIVATE.value,
          "artefactRepoLocation": {
            "repoURL": "https://gitlab.i2cat.net/api/v4/projects/1458/packages/helm/stable",
            "userName": "i2edge",
            "password": "3wZztr7cLvypoCCCdwJt",
            "token": ""
          },
          "artefactFile": "",
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
        url = f"http://{self.base_url}/{BaseTestCase.federation}/artefact"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.post(url, headers=headers, json=body)
        content = json.loads(response.content)
        self.assertIn(response.status_code, [200, 409], f'Response body is : {content}')

    def test_14(self):
        """Test case for get_artefact

        Retrieves details about an artefact.
        """
        url = f"http://{self.base_url}/{BaseTestCase.federation}/artefact/{BaseTestCase.artefact_upload}"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.get(url, headers=headers)
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200, f'Response body is : {content}')

    # Get artefact. Incorrect value for federation
    def test_15(self):
        """Test case for get_artefact

        Retrieves details about an artefact.
        """
        url = f"http://{self.base_url}/{3232222232323232}/artefact/{BaseTestCase.artefact_upload}"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.get(url, headers=headers)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
          self.assertEqual(response.status_code, 422, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
          self.assertEqual(response.status_code, 500, f'Response body is : {content}')

    # Get artefact. Federation not found
    def test_16(self):
        """Test case for get_artefact

        Retrieves details about an artefact.
        """
        url = f"http://{self.base_url}/{'65b799f576063bc1ac9e6999'}/artefact/{BaseTestCase.artefact_upload}"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.get(url, headers=headers)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
          self.assertEqual(response.status_code, 422, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
          self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    # Get artefact. Check if exist Federation and artefact
    def test_17(self):
        """Test case for get_artefact

        Retrieves details about an artefact.
        """
        url = f"http://{self.base_url}/{BaseTestCase.federation}/artefact/{'3fa85f64-5717-4562-b3fc-222222222233'}"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.get(url, headers=headers)
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    # Remove artefact. Incorrect value for federation
    def test_18(self):
        """Test case for remove_artefact

        Removes an artefact from partner OP.
        """
        url = f"http://{self.base_url}/{3232222232323232}/artefact/{BaseTestCase.artefact_upload}"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.delete(url, headers=headers)
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 422, f'Response body is : {content}')

    # Remove artefact. Federation not found
    def test_19(self):
        """Test case for remove_artefact

        Removes an artefact from partner OP.
        """
        url = f"http://{self.base_url}/{'65b799f576063bc1ac9e6999'}/artefact/{BaseTestCase.artefact_upload}"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.delete(url, headers=headers)
        content = json.loads(response.content)
        if self.roleOp == util._ROLE_PARTNER_OP:
          self.assertEqual(response.status_code, 422, f'Response body is : {content}')
        if self.roleOp == util._ROLE_ORIGINATING_OP:
          self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    # Remove artefact. Check if exist Federation and artefact
    def test_20(self):
        """Test case for remove_artefact

        Removes an artefact from partner OP.
        """
        url = f"http://{self.base_url}/{BaseTestCase.federation}/artefact/{'3fa85f64-5717-4562-b3fc-222222222233'}"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.delete(url, headers=headers)
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 404, f'Response body is : {content}')

    def test_21(self):
        """Test case for remove_artefact

        Removes an artefact from partner OP.
        """
        url = f"http://{self.base_url}/{BaseTestCase.federation}/artefact/{BaseTestCase.artefact_upload}"

        headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {BaseTestCase.token}"}

        response = requests.delete(url, headers=headers)
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200, f'Response body is : {content}')

    def test_22(self):

        # Delete artefacts created
        #self.delete_artefact(BaseTestCase.federation, BaseTestCase.artefact_upload, BaseTestCase.token)
        self.delete_artefact(BaseTestCase.federation, BaseTestCase.artefact_public, BaseTestCase.token)
        self.delete_artefact(BaseTestCase.federation, BaseTestCase.artefact_private, BaseTestCase.token)

        # Delete federations
        self.delete_federation(BaseTestCase.federation, BaseTestCase.token)
        self.delete_federation(BaseTestCase.federation2, BaseTestCase.token)


if __name__ == '__main__':
    import unittest
    unittest.main()
