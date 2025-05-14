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

CONFIG = ConfigParser()
CONFIG.read("conf/config.cfg")
SERVER_PARTNER = CONFIG.get("partner_op", "partner_op_server")
PORT_PARTNER = CONFIG.get("partner_op", "partner_op_port")
HOST_PARTNER = CONFIG.get("partner_op", "partner_op_host")
URL_PARTNER = f"{HOST_PARTNER}:{PORT_PARTNER}{SERVER_PARTNER}"

def create_federation(token, body):

    url = f"http://{URL_PARTNER}/partner"

    headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {token}"}
    response = requests.post(url, headers=headers, json=body)

    data_response = response.json()

    return data_response

def get_federation(federation_id, token):

    url = f"http://{URL_PARTNER}/{federation_id}/partner"

    headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)

    return response.json()

def update_federation(token, federation_id, body):

    url = f"http://{URL_PARTNER}/{federation_id}/partner"

    headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {token}"}
    response = requests.patch(url, headers=headers, json=body)

    data_response = response.json()

    return data_response

def delete_federation(federation_id, token):

    url = f"http://{URL_PARTNER}/{federation_id}/partner"

    headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {token}"}
    response = requests.delete(url, headers=headers)

    return response.json()

def create_availability_zones(federation_context_id, body, token):

    url = f"http://{URL_PARTNER}/{federation_context_id}/zones"

    headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {token}"}
    response = requests.post(url, headers=headers, json=body)

    data_response = response.json()

    return data_response

def get_availability_zones(federation_id, zone_id, token):

    url = f"http://{URL_PARTNER}/{federation_id}/zones/{zone_id}"

    headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)

    return response.json()

def delete_availability_zones(federation_id, zone_id, token):

    url = f"http://{URL_PARTNER}/{federation_id}/zones/{zone_id}"

    headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {token}"}
    response = requests.delete(url, headers=headers)

    return response.json()

def create_artefact(federation_context_id, body, token):

    url = f"http://{URL_PARTNER}/{federation_context_id}/artefact"

    headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {token}"}
    response = requests.post(url, headers=headers, json=body)

    data_response = response.json()

    return data_response


def get_artefact(federation_id, artefact_id, token):

    url = f"http://{URL_PARTNER}/{federation_id}/artefact/{artefact_id}"

    headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)

    return response.json()

def delete_artefact(federation_id, artefact_id, token):

    url = f"http://{URL_PARTNER}/{federation_id}/artefact/{artefact_id}"

    headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {token}"}
    response = requests.delete(url, headers=headers)

    return response.json()

def create_profile(federation_context_id, body, token):

    url = f"http://{URL_PARTNER}/{federation_context_id}/application/onboarding"

    headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {token}"}
    response = requests.post(url, headers=headers, json=body)

    data_response = response.json()

    return data_response

def delete_profile(federation_id, app_id, token):

    url = f"http://{URL_PARTNER}/{federation_id}/application/onboarding/app/{app_id}"

    headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {token}"}
    response = requests.delete(url, headers=headers)

    return response.json()

def update_profile(token, federation_id, app_id, body):

    url = f"http://{URL_PARTNER}/{federation_id}/application/onboarding/app/{app_id}"

    headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {token}"}
    response = requests.patch(url, headers=headers, json=body)

    data_response = response.json()

    return data_response

def get_profile(federation_id, app_id, token):

    url = f"http://{URL_PARTNER}/{federation_id}/application/onboarding/app/{app_id}"

    headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)

    return response.json()

def get_all_instances_deployment(federation_id, app_id, app_provider_id, token):

    url = f"http://{URL_PARTNER}/{federation_id}/application/lcm/app/{app_id}/appProvider/{app_provider_id}"

    headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)

    return response.json()

def get_instance_details_deployment(federation_id, app_id, app_instance_id, zone_id, token):

    url = f"http://{URL_PARTNER}/{federation_id}/application/lcm/app/{app_id}/instance/{app_instance_id}/zone/{zone_id}"

    headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)

    return response.json()

def install_app_deployment(federation_context_id, body, token):

    url = f"http://{URL_PARTNER}/{federation_context_id}/application/lcm"

    headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {token}"}
    response = requests.post(url, headers=headers, json=body)

    data_response = response.json()

    return data_response

def remove_app_deployment(federation_id, app_id, app_instance_id, zone_id, token):

    url = f"http://{URL_PARTNER}/{federation_id}/application/lcm/app/{app_id}/instance/{app_instance_id}/zone/{zone_id}"

    headers = {"Content-Type": "application/json; accept=application/json", "Authorization": f"Bearer {token}"}
    response = requests.delete(url, headers=headers)

    return response.json()
