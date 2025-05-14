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

import requests
from configparser import ConfigParser
import json
import base64
import os
from requests.models import Response
import util

CONFIG = ConfigParser()
CONFIG.read("conf/config.cfg")
HOST = CONFIG.get("i2edge", "host")
PORT = int(CONFIG.get("i2edge", "port"))
TIMEOUT_REQUESTS = 20


def get_zones_list():

    url = f"http://{HOST}:{PORT}/zones/list"
    response = requests.get(url, timeout=TIMEOUT_REQUESTS)

    if response.status_code != 200:
        return None

    data = response.json()

    return data


def get_zone_by_zone_id(zone_id):

    url = f"http://{HOST}:{PORT}/zone/{zone_id}"
    response = requests.get(url, timeout=TIMEOUT_REQUESTS)

    if response.status_code != 200:
        return None

    data = response.json()

    return data


def get_zones():

  url = f"http://{HOST}:{PORT}/zones"
  response = requests.get(url, timeout=TIMEOUT_REQUESTS)

  if response.status_code != 200:
    return None

  data = response.json()

  return data

def onboarding_artefact(body):
    posted = True
    params = {}
    files = {}
    file_path = ""

    if body.repo_type == util.RepoType.UPLOAD.value:
        base64_data = body.artefact_file

        # Decode base64_data to obtain file
        decoded_data = base64.b64decode(base64_data)

        # Define the path to save the decoded file
        file_path = f'/tmp/{body.artefact_name}.tgz'

        # Save the decoded bytes to a file
        with open(file_path, 'wb') as file:
             file.write(decoded_data)

        # Define the tar.gz file to be uploaded
        files = {
            'artefact_file': (f'{body.artefact_id}-{body.artefact_version_info}.tgz', open(file_path, 'rb'), 'application/x-compressed-tar')
        }

        params = {
            'artefact_id': body.artefact_id,
            'name': body.artefact_name,
            'repo_type': util.RepoType.UPLOAD.value
        }

    if body.repo_type == util.RepoType.PUBLIC.value:
        params = {
            'artefact_id': body.artefact_id,
            'name': body.artefact_name,
            'repo_url': body.artefact_repo_location.repo_url,
            'repo_type': util.RepoType.PUBLIC.value
        }

    if body.repo_type == util.RepoType.PRIVATE.value:
        params = {
            'artefact_id': body.artefact_id,
            'name': body.artefact_name,
            'repo_url': body.artefact_repo_location.repo_url,
            'repo_user_name': body.artefact_repo_location.user_name,
            'repo_password': body.artefact_repo_location.password,
            'repo_token': body.artefact_repo_location.token,
            'repo_type': util.RepoType.PRIVATE.value
        }

    url = f"http://{HOST}:{PORT}/artefact"

    headers = {
        'Accept': 'application/json'
    }

    # Make the POST request
    try:
        if body.repo_type == util.RepoType.UPLOAD.value:
            response = requests.post(url, headers=headers, files=files, data=params, timeout=TIMEOUT_REQUESTS)
            # Close the file handles and clean up temporary files
            files['artefact_file'][1].close()
            os.remove(file_path)
        else:
            response = requests.post(url, headers=headers, data=params, timeout=TIMEOUT_REQUESTS)
    except Exception as error:
        if body.repo_type == util.RepoType.UPLOAD.value:
            try:
                # Close the file handles and clean up temporary files
                files['artefact_file'][1].close()
                os.remove(file_path)
            except:
                pass
        definition = f"Unable to upload artefact. Reason: {error}"
        dict = {"message": definition}
        content = json.dumps(dict)
        status_code = 422
        response = create_manual_response(content, status_code)
        return response

    return response

def get_helm_chart(artefact_name):
    helm_chart = None

    url = f"http://{HOST}:{PORT}/helmcharts/{artefact_name}"

    response = requests.get(url)

    if response.status_code != 200:
        return None

    helm_chart = response.json()

    return helm_chart[0]

def delete_helm_chart(artefact_name, version):
    deleted = True

    url = f"http://{HOST}:{PORT}/helmchart/{artefact_name}/{version}"

    response = requests.delete(url)

    if response.status_code != 200:
        return False

    return deleted

def delete_artefact(artefact_id):
    response = None

    try:
        url = f"http://{HOST}:{PORT}/artefact/{artefact_id}"
        response = requests.delete(url)
    except Exception as error:
        definition = f"Unexpected Error: {error}"
        dict = {"message": definition}
        content = json.dumps(dict)
        status_code = 500
        response = create_manual_response(content, status_code)

    return response

def post_onboarding(onboarding_data):
    response = None

    try:
        url = f"http://{HOST}:{PORT}/application/onboarding/"
        headers = {"Content-Type": "application/json; accept=application/json"}
        response = requests.post(url, headers=headers, json=onboarding_data)
    except Exception as error:
        definition = f"Unexpected Error: {error}"
        dict = {"message": definition}
        content = json.dumps(dict)
        status_code = 500
        response = create_manual_response(content, status_code)

    return response


def update_onboarding(app_id, onboarding_data):
    response = None

    try:
        url = f"http://{HOST}:{PORT}/application/onboarding/{app_id}"
        headers = {"Content-Type": "application/json; accept=application/json"}
        response = requests.patch(url, headers=headers, json=onboarding_data)
    except Exception as error:
        definition = f"Unexpected Error: {error}"
        dict = {"message": definition}
        content = json.dumps(dict)
        status_code = 500
        response = create_manual_response(content, status_code)

    return response


def delete_onboarding(app_id):
    response = None

    try:
        url = f"http://{HOST}:{PORT}/application/onboarding/{app_id}"
        response = requests.delete(url)
    except Exception as error:
        definition = f"Unexpected Error: {error}"
        dict = {"message": definition}
        content = json.dumps(dict)
        status_code = 500
        response = create_manual_response(content, status_code)

    return response


def get_onboarding(app_id):
    response = None

    try:
        url = f"http://{HOST}:{PORT}/application/onboarding/{app_id}"
        response = requests.get(url)
    except Exception as error:
        definition = f"Unexpected Error: {error}"
        dict = {"message": definition}
        content = json.dumps(dict)
        status_code = 500
        response = create_manual_response(content, status_code)

    return response


def post_app_command(app_command_data):
    response = None

    try:
        url = f"http://{HOST}:{PORT}/app/"
        headers = {"Content-Type": "application/json; accept=application/json"}
        response = requests.post(url, headers=headers, json=app_command_data)
    except Exception as error:
        definition = f"Unexpected Error: {error}"
        dict = {"message": definition}
        content = json.dumps(dict)
        status_code = 500
        response = create_manual_response(content, status_code)

    return response


def get_app_by_zone(zone_id):
    response = None

    try:
        url = f"http://{HOST}:{PORT}/apps/{zone_id}"
        response = requests.get(url)
    except Exception as error:
        definition = f"Unexpected Error: {error}"
        dict = {"message": definition}
        content = json.dumps(dict)
        status_code = 500
        response = create_manual_response(content, status_code)

    return response


def get_app_by_zone_ap_name(zone_id, app_name):
    response = None

    try:
        url = f"http://{HOST}:{PORT}/app/{zone_id}/{app_name}"
        response = requests.get(url)
    except Exception as error:
        definition = f"Unexpected Error: {error}"
        dict = {"message": definition}
        content = json.dumps(dict)
        status_code = 500
        response = create_manual_response(content, status_code)

    return response


def delete_app(app_name):
    response = None

    try:
        url = f"http://{HOST}:{PORT}/app/{app_name}"
        response = requests.delete(url)
    except Exception as error:
        definition = f"Unexpected Error: {error}"
        dict = {"message": definition}
        content = json.dumps(dict)
        status_code = 500
        response = create_manual_response(content, status_code)

    return response

def create_manual_response(content, status_code):
    # Create a new Response object
    response = Response()

    # Set the status code
    response.status_code = status_code

    # Set the content (must be bytes)
    response._content = content.encode('utf-8')

    # Optionally, set other attributes like headers
    response.headers['Content-Type'] = 'application/json'

    return response
