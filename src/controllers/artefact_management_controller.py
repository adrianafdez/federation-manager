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

import connexion
from models.inline_response2005 import InlineResponse2005  # noqa: E501
from models.inline_response2006 import InlineResponse2006  # noqa: E501
import util
from models.federation_context_id_artefact_body import FederationContextIdArtefactBody
from models.mongo_document import OriginatingOperatorPlatform
from models.mongo_document import OriginatingOperatorPlatformOriginatingOP
from models.mongo_document import OriginatingArtefactManagement
from models.mongo_document import OriginatingArtefactManagementOriginatingOP
from models.federation_context_id_files_body import FederationContextIdFilesBody
from models.mongo_document import OriginatingArtefactFileManagement
from models.mongo_document import OriginatingApplicationOnboardingManagement
from models.mongo_document import ComponentSpec, ExposedInterfaces, Gpu, HugePages, CompEnvParams, PersistentVolumes
from clients import i2edge

from flask import abort
import base64
import json
from enum import Enum

from configparser import ConfigParser
from clients import fed_manager as fm_client

CONFIG = ConfigParser()
CONFIG.read("conf/config.cfg")
roleOp = CONFIG.get("partner_op", "role")

def get_artefact(federation_context_id, artefact_id):  # noqa: E501
    """Retrieves details about an artefact.

     # noqa: E501

    :param federation_context_id:
    :type federation_context_id: dict | bytes
    :param artefact_id:
    :type artefact_id: dict | bytes

    :rtype: InlineResponse2005
    """
    """
    if connexion.request.is_json:
        federation_context_id = FederationContextId.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        artefact_id = ArtefactId.from_dict(connexion.request.get_json())  # noqa: E501
    """
    if roleOp == util._ROLE_PARTNER_OP:
        # Check if exist Federation Context Id in Operator Platform
        try:
            originating_op_objects = OriginatingOperatorPlatform.objects(id=federation_context_id)
            if not originating_op_objects:
                abort(404, "Federation not found at Operator Platform")
        except Exception as error:
            abort(422, f"Incorrect value for Federation. Error: {error}")

        # Check if exist Federation Context Id and Artefact Id in Artefact Management
        originating_am_objects = OriginatingArtefactManagement.objects(
            orig_am_federation_context_id=federation_context_id,
            orig_am_artefact_id=artefact_id)
        if not originating_am_objects:
            abort(404, "Federation Context and Artefact Id Not Found at Artefact Management")

        artefact = originating_am_objects.get()

        artefactRepoLocation = {'repoURL':artefact.orig_am_artefact_repo_location_repo_url,
                                'userName':artefact.orig_am_artefact_repo_location_user_name,
                                'password':artefact.orig_am_artefact_repo_location_password,
                                'token':artefact.orig_am_artefact_repo_location_token}

        response_data = {
             "artefactId": artefact.orig_am_artefact_id,
             "appProviderId": artefact.orig_am_app_provider_id,
             "artefactName": artefact.orig_am_artefact_name,
             "artefactDescription": artefact.orig_am_artefact_description,
             "artefactVersionInfo": artefact.orig_am_artefact_version_info,
             "artefactVirtType": artefact.orig_am_artefact_virt_type,
             "artefactFileName": artefact.orig_am_artefact_filename,
             "artefactFileFormat": artefact.orig_am_artefact_file_format,
             "artefactDescriptorType": artefact.orig_am_artefact_descriptor_type,
             "repoType": artefact.orig_am_repo_type,
             "artefactRepoLocation": artefactRepoLocation
        }
        artefact_response_data = InlineResponse2005.from_dict(response_data)
    elif roleOp == util._ROLE_ORIGINATING_OP:
        try:
            # Extract the token from the header
            bearer_token = util.get_token_from_request(connexion)

            # Find federation at originating OP
            originating_op_objects = OriginatingOperatorPlatformOriginatingOP.objects(id=federation_context_id)
            if not originating_op_objects:
                return "Federation not found", 404
            originating_op_instance = originating_op_objects[0]

            # Find artefact at partner
            response_get = fm_client.get_artefact(originating_op_instance.partner_federation_id, artefact_id,
                                                  bearer_token)
            if "artefactId" in response_get:
                if find_artefact_at_orig_op(federation_context_id, artefact_id):
                    return response_get
                else:
                    return "Artefact exist at partner operator but not in originating operator", 409
            else:
                if find_artefact_at_orig_op(federation_context_id, artefact_id):
                    return "Artefact exist in originating operator but not in partner operator", 409
                else:
                    return "Artefact not Found", 404
        except Exception as error:
            artefact_response_data = {f"Error while getting Artefact. Reason: {error}"}
    else:
        artefact_response_data = {"Error": "Not assigned role to the operator (originating_op|partner_op)"}

    return artefact_response_data


def remove_artefact(federation_context_id, artefact_id):  # noqa: E501
    """Removes an artefact from partner OP.

     # noqa: E501

    :param federation_context_id:
    :type federation_context_id: dict | bytes
    :param artefact_id:
    :type artefact_id: dict | bytes

    :rtype: None
    """
    if roleOp == util._ROLE_PARTNER_OP:
        # Check if exist Federation Context Id in Operator Platform
        try:
            originating_op_objects = OriginatingOperatorPlatform.objects(id=federation_context_id)
            if not originating_op_objects:
                abort(404, "Federation not found at Operator Platform")
        except Exception as error:
            abort(422, f"Incorrect value for Federation. Error: {error}")

        # Check if exist Federation Context Id and Artefact Id in Artefact Management
        originating_am_objects = OriginatingArtefactManagement.objects(
            orig_am_federation_context_id=federation_context_id,
            orig_am_artefact_id=artefact_id)
        if not originating_am_objects:
            abort(404, "Federation Context and Artefact Id Not Found at Artefact Management")
        artefact_instance = originating_am_objects.get()

        # Check if there are onboardings dependents of the artefact by provider
        if check_childs_artefact(federation_context_id, artefact_id, artefact_instance):
            abort(409, "Unable to remove Artefact. There are application onboardings dependent. Remove it and try again ")

        try:
            response = i2edge.delete_artefact(artefact_id)
            if response.status_code != 200:
                abort(422, f"Unable to delete artefact from i2edge. Response: {response.content}")
        except Exception as error:
            abort(422, f"Unable to delete artefact from i2edge. Error: {error}")

        # Delete artefact from FM
        originating_am_objects.delete()
    elif roleOp == util._ROLE_ORIGINATING_OP:
        try:
            # Extract the token from the header
            bearer_token = util.get_token_from_request(connexion)

            # Find federation at originating OP
            originating_op_objects = OriginatingOperatorPlatformOriginatingOP.objects(id=federation_context_id)
            if not originating_op_objects:
                return "Federation not found", 404
            originating_op_instance = originating_op_objects[0]

            # Find artefact at partner
            response_get = fm_client.get_artefact(originating_op_instance.partner_federation_id, artefact_id,
                                                  bearer_token)
            if "artefactId" in response_get:
                originating_am_objects = find_artefact_at_orig_op(federation_context_id, artefact_id)
                if originating_am_objects:
                    # Delete artefact from partner
                    response_data = fm_client.delete_artefact(originating_op_instance.partner_federation_id,
                                                              artefact_id, bearer_token)
                    if "deletion" in response_data:
                        # If artefact has been removed well, remove artefact from originating
                        originating_am_objects.delete()
                        return response_data, 200
                    else:
                        return response_data, 422
                else:
                    return "Artefact exist at partner operator but not in originating operator", 409
            else:
                if find_artefact_at_orig_op(federation_context_id, artefact_id):
                    return "Artefact exist in originating operator but not in partner operator", 409
                else:
                    return "Artefact not Found", 404
        except Exception as error:
            return f"Error while deleting Artefact. Reason: {error}", 422
    else:
        return "Error: Not assigned role to the operator (originating_op|partner_op)", 422

    return 'Artefact deletion successful', 200


def remove_file(federation_context_id, file_id):  # noqa: E501
    """Removes an image file from partner OP.

     # noqa: E501

    :param federation_context_id:
    :type federation_context_id: dict | bytes
    :param file_id:
    :type file_id: dict | bytes

    :rtype: None
    """
    # Check if exist Federation Context Id in Operator Platform
    try:
        originating_op_objects = OriginatingOperatorPlatform.objects(id=federation_context_id)
        if not originating_op_objects:
            abort(404, "Federation not found at Operator Platform")
    except Exception as error:
        abort(422, f"Incorrect value for Federation. Error {error}")

    # Check if exist Federation Context Id and File Id in Artefact File Management
    originating_af_objects = OriginatingArtefactFileManagement.objects(
        orig_af_federation_context_id=federation_context_id,
        orig_af_file_id=file_id)
    if not originating_af_objects:
        abort(404, "Federation Context and File Id Not Found at Artefact File Management")

    originating_af_objects.delete()

    return 'Image deletion successful', 200

#def upload_artefact(artefact_id, app_provider_id, artefact_name, artefact_version_info, artefact_description, artefact_virt_type, artefact_file_name, artefact_file_format, artefact_descriptor_type, repo_type, artefact_repo_location, artefact_file, component_spec, federation_context_id):  # noqa: E501
def upload_artefact(body, federation_context_id):  # noqa: E501
    """Uploads application artefact on partner OP. Artefact is a zip file containing scripts and/or packaging files like Terraform or Helm which are required to create an instance of an application.

     # noqa: E501

    :param artefact_id:
    :type artefact_id: dict | bytes
    :param app_provider_id:
    :type app_provider_id: dict | bytes
    :param artefact_name:
    :type artefact_name: str
    :param artefact_version_info:
    :type artefact_version_info: str
    :param artefact_description:
    :type artefact_description: str
    :param artefact_virt_type:
    :type artefact_virt_type: str
    :param artefact_file_name:
    :type artefact_file_name: str
    :param artefact_file_format:
    :type artefact_file_format: str
    :param artefact_descriptor_type:
    :type artefact_descriptor_type: str
    :param repo_type:
    :type repo_type: str
    :param artefact_repo_location:
    :type artefact_repo_location: dict | bytes
    :param artefact_file:
    :type artefact_file: strstr
    :param component_spec:
    :type component_spec: list | bytes
    :param federation_context_id:
    :type federation_context_id: dict | bytes

    :rtype: None
    """
    if roleOp == util._ROLE_PARTNER_OP:
        # Check if exist Federation Context Id in Operator Platform
        try:
            originating_op_objects = OriginatingOperatorPlatform.objects(id=federation_context_id)
            if not originating_op_objects:
                abort(404, "Federation not found at Operator Platform")
        except Exception as error:
            abort(422, f"Incorrect value for Federation. Error: {error}")

        try:
            if connexion.request.is_json:
                body = FederationContextIdArtefactBody.from_dict(connexion.request.get_json())
        except Exception as error:
            abort(422, f"Artefact Validation Error. Message: {error}")

        # Check if exist Federation Context Id and Artefact Id in Artefact Management
        originating_am_objects = OriginatingArtefactManagement.objects(
            orig_am_federation_context_id=federation_context_id,
            orig_am_artefact_id=body.artefact_id)
        if originating_am_objects:
            abort(409, "Federation Context and Artefact Id already exists at Artefact Management")

        # Check if exist artefact id in the database. If found artefact id belongs to another federation
        originating_am_objects = OriginatingArtefactManagement.objects(
            orig_am_artefact_id=body.artefact_id)
        if originating_am_objects:
            abort(409, "Artefact Id already exists for another Federation at Artefact Management")

        # Provider is mandatory
        if body.app_provider_id == "":
            abort(400, f"appProviderId is empty")

        # Artefact name is mandatory
        if body.artefact_name == "":
            abort(400, f"artefactName is empty")

        # Artefact version info is mandatory
        if body.artefact_version_info == "":
            abort(400, f"artefactVersionInfo is empty")

        if body.repo_type == util.RepoType.UPLOAD.value:

            # Check artefact file
            if body.artefact_file == "":
                abort(400, f"artefactFile is empty")

            try:
                decoded_data = base64.b64decode(body.artefact_file)
            except Exception as error:
                abort(422, f"Incorrect Artefact File. Error: {error}")

        if body.repo_type == util.RepoType.PUBLIC.value:
            if body.artefact_repo_location.repo_url == "":
                abort(400, f"You have chosen PUBLICREPO but the repoUrl is empty")
            body.artefact_file = ""

        if body.repo_type == util.RepoType.PRIVATE.value:
            if body.artefact_repo_location.repo_url == "":
                abort(400, f"You have chosen PRIVATEREPO but the repoUrl is empty")
            if (body.artefact_repo_location.user_name == "" and body.artefact_repo_location.password == "" and
                    body.artefact_repo_location.token == ""):
                abort(400, f"You have chosen PRIVATEREPO but credentials or token are empty")
            if body.artefact_repo_location.user_name != "" and body.artefact_repo_location.password == "":
                abort(400, f"You have chosen PRIVATEREPO with userName but Password is empty")
            if body.artefact_repo_location.user_name == "" and body.artefact_repo_location.password != "":
                abort(400, f"You have chosen PRIVATEREPO with Password but userName is empty")
            body.artefact_file = ""

        # Onboarding helm to i2edge
        try:
            response_data = i2edge.onboarding_artefact(body)
            if response_data.status_code != 201:
                data = response_data.json()
                return data, 409
        except Exception as error:
            abort(422, f"Unable to upload artefact to i2edge. Error: {error}")

        # Convert the original model instance to the MongoEngine document
        artefact_data = fill_artefact_mongo_document(federation_context_id, body)

        # Create a new MongoEngine document and save it to MongoDB
        new_artefact = OriginatingArtefactManagement(**artefact_data)
        new_artefact.save()

        """
        if connexion.request.is_json:
            artefact_id = ArtefactId.from_dict(connexion.request.get_json())  # noqa: E501
        if connexion.request.is_json:
            app_provider_id = AppProviderId.from_dict(connexion.request.get_json())  # noqa: E501
        if connexion.request.is_json:
            artefact_repo_location = ObjectRepoLocation.from_dict(connexion.request.get_json())  # noqa: E501
        if connexion.request.is_json:
            component_spec = [ComponentSpec.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
        if connexion.request.is_json:
            federation_context_id = FederationContextId.from_dict(connexion.request.get_json())  # noqa: E501
        """
    elif roleOp == util._ROLE_ORIGINATING_OP:
        try:
            # Extract the token from the header
            bearer_token = util.get_token_from_request(connexion)

            body = FederationContextIdArtefactBody.from_dict(connexion.request.get_json())

            # Find federation at originating OP
            originating_op_objects = OriginatingOperatorPlatformOriginatingOP.objects(id=federation_context_id)
            if not originating_op_objects:
                return "Federation not found", 404
            originating_op_instance = originating_op_objects[0]
            # Find artefact at partner
            response_get = fm_client.get_artefact(originating_op_instance.partner_federation_id, body.artefact_id, bearer_token)
            if "artefactId" in response_get:
                if find_artefact_at_orig_op(federation_context_id, body.artefact_id):
                    return "Artefact already exist", 422
                else:
                    return "Artefact exist in Partner Operator but not in Originating Operator", 409
            else:
                if find_artefact_at_orig_op(federation_context_id, body.artefact_id):
                    return "Artefact exist in Originating Operator but not in Partner Operator", 409
                else:
                    # Create artefact in partner
                    response_data = fm_client.create_artefact(originating_op_instance.partner_federation_id,
                                                              connexion.request.get_json(), bearer_token)
                    if "uploaded" in response_data:
                        # Create artefact in originating
                        create_artefact_originatingOP(federation_context_id, originating_op_instance.partner_federation_id, body)
                        return response_data, 200
                    else:
                        return response_data, 422

            return response_data, 200
        except Exception as error:
            return f"Error while creating Artefact. Reason: {error}", 422
    else:
        return "Error: Not assigned role to the operator (originating_op|partner_op)", 422

    return 'Artefact uploaded successfully', 200


#def upload_file(file_id, app_provider_id, file_name, file_description, file_version_info, file_type, checksum, img_os_type, img_ins_set_arch, repo_type, file_repo_location, file, federation_context_id):  # noqa: E501
def upload_file(body, federation_context_id):  # noqa: E501
    """Uploads an image file. Originating OP uses this api to onboard an application image to partner OP.

     # noqa: E501

    :param file_id:
    :type file_id: dict | bytes
    :param app_provider_id:
    :type app_provider_id: dict | bytes
    :param file_name:
    :type file_name: str
    :param file_description:
    :type file_description: str
    :param file_version_info:
    :type file_version_info: str
    :param file_type:
    :type file_type: dict | bytes
    :param checksum:
    :type checksum: str
    :param img_os_type:
    :type img_os_type: dict | bytes
    :param img_ins_set_arch:
    :type img_ins_set_arch: dict | bytes
    :param repo_type:
    :type repo_type: str
    :param file_repo_location:
    :type file_repo_location: dict | bytes
    :param file:
    :type file: strstr
    :param federation_context_id:
    :type federation_context_id: dict | bytes

    :rtype: None
    """
    # Check if exist Federation Context Id in Operator Platform
    try:
        originating_op_objects = OriginatingOperatorPlatform.objects(id=federation_context_id)
        if not originating_op_objects:
            abort(404, "Federation not found at Operator Platform")
    except Exception as error:
        abort(422, f"Incorrect value for Federation. Error: {error}")

    try:
        if connexion.request.is_json:
            body = FederationContextIdFilesBody.from_dict(connexion.request.get_json())
    except Exception as error:
        abort(422, f"File Validation Error. Message: {error}")

    # Check if exist Federation Context Id and File Id in Artefact File Management
    originating_af_objects = OriginatingArtefactFileManagement.objects(
        orig_af_federation_context_id=federation_context_id,
        orig_af_file_id=body.file_id)
    if originating_af_objects:
        abort(404, "Federation Context and File Id already exists at Artefact File Management")

    # Check if exist File Id for another Federation in Artefact File Management
    originating_af_objects = OriginatingArtefactFileManagement.objects(
        orig_af_file_id=body.file_id)
    if originating_af_objects:
        abort(404, "File Id already exists for another Federation at Artefact File Management")

    # Check if is provided a correct file when repoType is UPLOAD
    if body.repo_type == util.RepoType.UPLOAD.value:
        body.file_repo_location.repo_url = ""
        body.file_repo_location.user_name = ""
        body.file_repo_location.password = ""
        body.file_repo_location.token = ""
        try:
            decoded_data = base64.b64decode(body.file)
        except Exception as error:
            abort(422,
                  f"You have chosen UPLOAD Repo Type option but the File is incorrect. Error: {error}")
    else:
        body.file = ""

    file_data = {
        "orig_af_federation_context_id": federation_context_id,
        "orig_af_file_id": body.file_id,
        "orig_af_app_provider_id": body.app_provider_id,
        "orig_af_file_name": body.file_name,
        "orig_af_file_description": body.file_description,
        "orig_af_file_version_info": body.file_version_info,
        "orig_af_file_type": body.file_type,
        "orig_af_checksum": body.checksum,
        "orig_af_img_os_type_architecture": body.img_os_type.architecture,
        "orig_af_img_os_type_distribution": body.img_os_type.distribution,
        "orig_af_img_os_type_version": body.img_os_type.version,
        "orig_af_img_os_type_license": body.img_os_type.license,
        "orig_af_img_ins_set_arch": body.img_ins_set_arch,
        "orig_af_repo_type": body.repo_type,
        "orig_af_file_repo_location_repo_url": body.file_repo_location.repo_url,
        "orig_af_file_repo_location_user_name": body.file_repo_location.user_name,
        "orig_af_file_repo_location_password": body.file_repo_location.password,
        "orig_af_file_repo_location_token": body.file_repo_location.token,
        "orig_af_file": body.file
    }

    # Create a new MongoEngine document and save it to MongoDB
    new_file = OriginatingArtefactFileManagement(**file_data)
    new_file.save()

    return 'File uploaded successfully', 200


def view_file(federation_context_id, file_id):  # noqa: E501
    """View an image file from partner OP.

     # noqa: E501

    :param federation_context_id:
    :type federation_context_id: dict | bytes
    :param file_id:
    :type file_id: dict | bytes

    :rtype: InlineResponse2006
    """
    # Check if exist Federation Context Id in Operator Platform
    try:
        originating_op_objects = OriginatingOperatorPlatform.objects(id=federation_context_id)
        if not originating_op_objects:
            abort(404, "Federation not found at Operator Platform")
    except Exception as error:
        abort(422, f"Incorrect value for Federation. Error: {error}")

    # Check if exist Federation Context Id and File Id in Artefact File Management
    originating_af_objects = OriginatingArtefactFileManagement.objects(
        orig_af_federation_context_id=federation_context_id,
        orig_af_file_id=file_id)
    if not originating_af_objects:
        abort(404, "Federation Context and File Id Not Found at Artefact File Management")

    files = originating_af_objects.get()

    img_os_type = {'architecture': files.orig_af_img_os_type_architecture,
                   'distribution': files.orig_af_img_os_type_distribution,
                   'version': files.orig_af_img_os_type_version,
                   'license': files.orig_af_img_os_type_license}

    file_repo_location = {'repoUrl': files.orig_af_file_repo_location_repo_url,
                          'userName': files.orig_af_file_repo_location_user_name,
                          'password': files.orig_af_file_repo_location_password,
                          'token': files.orig_af_file_repo_location_token}

    response_data = {
        "fileId": files.orig_af_file_id,
        "appProviderId": files.orig_af_app_provider_id,
        "fileName": files.orig_af_file_name,
        "fileDescription": files.orig_af_file_description,
        "fileVersionInfo": files.orig_af_file_version_info,
        "fileType": files.orig_af_file_type,
        "imgOSType": img_os_type,
        "imgInsSetArch": files.orig_af_img_ins_set_arch,
        "repoType": files.orig_af_repo_type,
        "fileRepoLocation": file_repo_location
    }
    file_response_data = InlineResponse2006.from_dict(response_data)

    return file_response_data

def  fill_artefact_mongo_document(federation_context_id, body):

    component_spec_list = []
    for c in body.component_spec:

        exposed_interfaces_list = []
        for e in c.exposed_interfaces:
            data_ei = {
                "orig_ei_interface_id" : e.interface_id,
                "orig_ei_comm_protocol" : e.comm_protocol,
                "orig_ei_comm_port" : e.comm_port,
                "orig_ei_visibility_type" : e.visibility_type,
                "orig_ei_network" : e.network,
                "orig_ei_interface_name" : e.interface_name
            }
            exposed_interfaces_list.append(data_ei)

        gpu_list = []
        for g in c.compute_resource_profile.gpu:
            data_gpu = {
                "orig_g_gpu_vendor_type": g.gpu_vendor_type,
                "orig_g_gpu_mode_name": g.gpu_mode_name,
                "orig_g_gpu_memory": g.gpu_memory,
                "orig_g_num_gpu": g.num_gpu,
            }
            gpu_list.append(data_gpu)

        huge_pages_list = []
        for h in c.compute_resource_profile.hugepages:
            data_hp = {
                "orig_h_page_size": h.page_size,
                "orig_h_number": h.number
            }
            huge_pages_list.append(data_hp)

        comp_env_params_list = []
        for cep in c.comp_env_params:
            data_comp = {
                "orig_cep_env_var_name": cep.env_var_name,
                "orig_cep_env_value_type": cep.env_value_type,
                "orig_cep_env_var_value": cep.env_var_value,
                "orig_cep_env_var_src": cep.env_var_src
            }
            comp_env_params_list.append(data_comp)

        pv_list = []
        for v in c.persistent_volumes:
            data_pv = {
                "orig_pv_volume_size": v.volume_size,
                "orig_pv_volume_mounth_path": v.volume_mount_path,
                "orig_pv_volume_name": v.volume_name,
                "orig_pv_ephemeral_type": v.ephemeral_type,
                "orig_pv_access_mode": v.access_mode,
                "orig_pv_sharing_policy": v.sharing_policy
            }
            pv_list.append(data_pv)

        data_ce = {
            "orig_ce_component_name": c.component_name,
            "orig_ce_component_spec_images": c.images,
            "orig_ce_component_spec_num_of_instances": c.num_of_instances,
            "orig_ce_component_spec_restart_policy": c.restart_policy,
            "orig_ce_component_spec_command_line_params_command": c.command_line_params.command,
            "orig_ce_component_spec_command_line_params_command_args": c.command_line_params.command_args,
            "orig_ce_component_spec_exposed_interfaces": exposed_interfaces_list,
            "orig_ce_component_spec_compute_resource_profile_cpuarchtype": c.compute_resource_profile.cpu_arch_type,
            "orig_ce_component_spec_compute_resource_profile_numcpu_whole": c.compute_resource_profile.num_cpu.get('whole').get('value'),
            "orig_ce_component_spec_compute_resource_profile_numcpu_decimal": c.compute_resource_profile.num_cpu.get('decimal').get('value'),
            "orig_ce_component_spec_compute_resource_profile_numcpu_millivcpu": c.compute_resource_profile.num_cpu.get('millivcpu').get('value'),
            "orig_ce_component_spec_compute_resource_profile_memory": c.compute_resource_profile.memory,
            "orig_ce_component_spec_compute_resource_profile_diskstorage": c.compute_resource_profile.disk_storage,
            "orig_ce_component_spec_compute_resource_profile_gpu": gpu_list,
            "orig_ce_component_spec_compute_resource_profile_vpu": c.compute_resource_profile.vpu,
            "orig_ce_component_spec_compute_resource_profile_fpga": c.compute_resource_profile.fpga,
            "orig_ce_component_spec_compute_resource_profile_hugepages": huge_pages_list,
            "orig_ce_component_spec_compute_resource_profile_cpuexclusivity": c.compute_resource_profile.cpu_exclusivity,
            "orig_ce_component_spec_comp_env_params": comp_env_params_list,
            "orig_ce_component_spec_deployment_config_config_type": c.deployment_config.config_type,
            "orig_ce_component_spec_deployment_config_contents": c.deployment_config.contents,
            "orig_ce_component_spec_persistent_volumes": pv_list
        }
        component_spec_list.append(data_ce)

    artefact_data = {
        "orig_am_federation_context_id": federation_context_id,
        "orig_am_artefact_id": body.artefact_id,
        "orig_am_app_provider_id": body.app_provider_id,
        "orig_am_artefact_name": body.artefact_name,
        "orig_am_artefact_version_info": body.artefact_version_info,
        "orig_am_artefact_description": body.artefact_description,
        "orig_am_artefact_virt_type": body.artefact_virt_type,
        "orig_am_artefact_filename": body.artefact_file_name,
        "orig_am_artefact_file_format": body.artefact_file_format,
        "orig_am_artefact_descriptor_type": body.artefact_descriptor_type,
        "orig_am_repo_type": body.repo_type,
        "orig_am_artefact_repo_location_repo_url": body.artefact_repo_location.repo_url,
        "orig_am_artefact_repo_location_user_name": body.artefact_repo_location.user_name,
        "orig_am_artefact_repo_location_password": body.artefact_repo_location.password,
        "orig_am_artefact_repo_location_token": body.artefact_repo_location.token,
        "orig_am_artefact_file": "",
        #"orig_am_artefact_file": body.artefact_file,
        "orig_am_component_spec": json.dumps(component_spec_list)
    }

    return artefact_data

def check_childs_artefact(federation_context_id, artefact_id, artefact_instance):
    found = False

    provider_id = artefact_instance.orig_am_app_provider_id

    originating_ao_objects = OriginatingApplicationOnboardingManagement.objects(
        orig_ao_federation_context_id=federation_context_id,
        orig_ao_app_provider_id=provider_id
    )
    if not originating_ao_objects:
        return False

    instances_onboarding = originating_ao_objects.filter()
    for elem in instances_onboarding:
        list_specs = json.loads(elem.orig_ao_app_component_specs)
        for l in list_specs:
            if l.get("artefactId") == artefact_id:
                return True

    return found

def create_artefact_originatingOP(federation_id, partner_federation_id, body):
    component_spec_list = []
    for c in body.component_spec:

        exposed_interfaces_list = []
        for e in c.exposed_interfaces:
            data_ei = {
                "orig_ei_interface_id": e.interface_id,
                "orig_ei_comm_protocol": e.comm_protocol,
                "orig_ei_comm_port": e.comm_port,
                "orig_ei_visibility_type": e.visibility_type,
                "orig_ei_network": e.network,
                "orig_ei_interface_name": e.interface_name
            }
            exposed_interfaces_list.append(data_ei)

        gpu_list = []
        for g in c.compute_resource_profile.gpu:
            data_gpu = {
                "orig_g_gpu_vendor_type": g.gpu_vendor_type,
                "orig_g_gpu_mode_name": g.gpu_mode_name,
                "orig_g_gpu_memory": g.gpu_memory,
                "orig_g_num_gpu": g.num_gpu,
            }
            gpu_list.append(data_gpu)

        huge_pages_list = []
        for h in c.compute_resource_profile.hugepages:
            data_hp = {
                "orig_h_page_size": h.page_size,
                "orig_h_number": h.number
            }
            huge_pages_list.append(data_hp)

        comp_env_params_list = []
        for cep in c.comp_env_params:
            data_comp = {
                "orig_cep_env_var_name": cep.env_var_name,
                "orig_cep_env_value_type": cep.env_value_type,
                "orig_cep_env_var_value": cep.env_var_value,
                "orig_cep_env_var_src": cep.env_var_src
            }
            comp_env_params_list.append(data_comp)

        pv_list = []
        for v in c.persistent_volumes:
            data_pv = {
                "orig_pv_volume_size": v.volume_size,
                "orig_pv_volume_mounth_path": v.volume_mount_path,
                "orig_pv_volume_name": v.volume_name,
                "orig_pv_ephemeral_type": v.ephemeral_type,
                "orig_pv_access_mode": v.access_mode,
                "orig_pv_sharing_policy": v.sharing_policy
            }
            pv_list.append(data_pv)

        data_ce = {
            "orig_ce_component_name": c.component_name,
            "orig_ce_component_spec_images": c.images,
            "orig_ce_component_spec_num_of_instances": c.num_of_instances,
            "orig_ce_component_spec_restart_policy": c.restart_policy,
            "orig_ce_component_spec_command_line_params_command": c.command_line_params.command,
            "orig_ce_component_spec_command_line_params_command_args": c.command_line_params.command_args,
            "orig_ce_component_spec_exposed_interfaces": exposed_interfaces_list,
            "orig_ce_component_spec_compute_resource_profile_cpuarchtype": c.compute_resource_profile.cpu_arch_type,
            "orig_ce_component_spec_compute_resource_profile_numcpu_whole": c.compute_resource_profile.num_cpu.get(
                'whole').get('value'),
            "orig_ce_component_spec_compute_resource_profile_numcpu_decimal": c.compute_resource_profile.num_cpu.get(
                'decimal').get('value'),
            "orig_ce_component_spec_compute_resource_profile_numcpu_millivcpu": c.compute_resource_profile.num_cpu.get(
                'millivcpu').get('value'),
            "orig_ce_component_spec_compute_resource_profile_memory": c.compute_resource_profile.memory,
            "orig_ce_component_spec_compute_resource_profile_diskstorage": c.compute_resource_profile.disk_storage,
            "orig_ce_component_spec_compute_resource_profile_gpu": gpu_list,
            "orig_ce_component_spec_compute_resource_profile_vpu": c.compute_resource_profile.vpu,
            "orig_ce_component_spec_compute_resource_profile_fpga": c.compute_resource_profile.fpga,
            "orig_ce_component_spec_compute_resource_profile_hugepages": huge_pages_list,
            "orig_ce_component_spec_compute_resource_profile_cpuexclusivity": c.compute_resource_profile.cpu_exclusivity,
            "orig_ce_component_spec_comp_env_params": comp_env_params_list,
            "orig_ce_component_spec_deployment_config_config_type": c.deployment_config.config_type,
            "orig_ce_component_spec_deployment_config_contents": c.deployment_config.contents,
            "orig_ce_component_spec_persistent_volumes": pv_list
        }
        component_spec_list.append(data_ce)

    artefact_data = {
        "orig_am_federation_context_id": federation_id,
        "orig_am_artefact_id": body.artefact_id,
        "orig_am_app_provider_id": body.app_provider_id,
        "orig_am_artefact_name": body.artefact_name,
        "orig_am_artefact_version_info": body.artefact_version_info,
        "orig_am_artefact_description": body.artefact_description,
        "orig_am_artefact_virt_type": body.artefact_virt_type,
        "orig_am_artefact_filename": body.artefact_file_name,
        "orig_am_artefact_file_format": body.artefact_file_format,
        "orig_am_artefact_descriptor_type": body.artefact_descriptor_type,
        "orig_am_repo_type": body.repo_type,
        "orig_am_artefact_repo_location_repo_url": body.artefact_repo_location.repo_url,
        "orig_am_artefact_repo_location_user_name": body.artefact_repo_location.user_name,
        "orig_am_artefact_repo_location_password": body.artefact_repo_location.password,
        "orig_am_artefact_repo_location_token": body.artefact_repo_location.token,
        "orig_am_artefact_file": "",
        "orig_am_component_spec": json.dumps(component_spec_list),
        "partner_federation_id": partner_federation_id
    }
    # Create a new MongoEngine document and save it to MongoDB
    new_artefact = OriginatingArtefactManagementOriginatingOP(**artefact_data)
    new_artefact.save()

def find_artefact_at_orig_op(federation_id, artefact_id):
    originating_am_objects = OriginatingArtefactManagementOriginatingOP.objects(
        orig_am_federation_context_id=federation_id,
        orig_am_artefact_id=artefact_id)

    return originating_am_objects
