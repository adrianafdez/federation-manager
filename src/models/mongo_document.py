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

from mongoengine import (Document, DateTimeField, ReferenceField, StringField, ListField, IntField,
                         FloatField, BooleanField)


#####################
# Operator Platform #
#####################
class OriginatingOperatorPlatform(Document):
    orig_op_federation_id = StringField()
    orig_op_country_code = StringField()
    orig_op_mobile_network_codes_mcc = StringField()
    orig_op_mobile_network_codes_mncs = ListField(StringField())
    orig_op_fixed_network_codes = ListField(StringField())
    initial_date = DateTimeField()
    partner_status_link = StringField()
    partner_callback_credentials_token_url = StringField()
    partner_callback_credentials_client_id = StringField()
    partner_callback_credentials_client_secret = StringField()
    partner_bearer_token = StringField(required=True)


class OriginatingOperatorPlatformUpdate(Document):
    object_type = StringField()
    operation_type = StringField()
    modification_date = DateTimeField()
    add_mobile_network_ids_mcc = StringField()
    add_mobile_network_ids_mncs = ListField(StringField())
    remove_mobile_network_ids_mcc = StringField()
    remove_mobile_network_ids_mncs = ListField(StringField())
    add_fixed_network_ids = ListField(StringField())
    remove_fixed_network_ids = ListField(StringField())
    federation_context_id = ReferenceField(OriginatingOperatorPlatform)


class OriginatingOperatorPlatformOriginatingOP(Document):
    orig_op_federation_id = StringField()
    orig_op_country_code = StringField()
    orig_op_mobile_network_codes_mcc = StringField()
    orig_op_mobile_network_codes_mncs = ListField(StringField())
    orig_op_fixed_network_codes = ListField(StringField())
    initial_date = DateTimeField()
    partner_status_link = StringField()
    partner_callback_credentials_token_url = StringField()
    partner_callback_credentials_client_id = StringField()
    partner_callback_credentials_client_secret = StringField()
    partner_bearer_token = StringField(required=True)
    partner_federation_id = StringField()


class OriginatingOperatorPlatformUpdateOriginatingOP(Document):
    object_type = StringField()
    operation_type = StringField()
    modification_date = DateTimeField()
    add_mobile_network_ids_mcc = StringField()
    add_mobile_network_ids_mncs = ListField(StringField())
    remove_mobile_network_ids_mcc = StringField()
    remove_mobile_network_ids_mncs = ListField(StringField())
    add_fixed_network_ids = ListField(StringField())
    remove_fixed_network_ids = ListField(StringField())
    federation_context_id = ReferenceField(OriginatingOperatorPlatformOriginatingOP)
    partner_federation_id = StringField()


######################
# Availability Zones #
######################
class OriginatingZoneInfo(Document):
    orig_zi_federation_context_id = StringField()
    orig_zi_acceptedAvailabilityZones = ListField(StringField())
    orig_zi_availZoneNotifLink = StringField()


class OriginatingZoneInfoOriginatingOP(Document):
    orig_zi_federation_context_id = StringField()
    orig_zi_acceptedAvailabilityZones = ListField(StringField())
    orig_zi_availZoneNotifLink = StringField()
    partner_federation_id = StringField()


#######################
# Artefact Management #
#######################
class ExposedInterfaces(Document):
    orig_ei_interface_id = StringField()
    orig_ei_comm_protocol = StringField()
    orig_ei_comm_port = IntField()
    orig_ei_visibility_type = StringField()
    orig_ei_network = StringField()
    orig_ei_interface_name = StringField()


class Gpu(Document):
    orig_g_gpu_vendor_type = StringField()
    orig_g_gpu_mode_name = StringField()
    orig_g_gpu_memory = IntField()
    orig_g_num_gpu = IntField()


class HugePages(Document):
    orig_h_page_size = StringField()
    orig_h_number = IntField()


class CompEnvParams(Document):
    orig_cep_env_var_name = StringField()
    orig_cep_env_value_type = StringField()
    orig_cep_env_var_value = StringField()
    orig_cep_env_var_src = StringField()


class PersistentVolumes(Document):
    orig_pv_volume_size = StringField()
    orig_pv_volume_mounth_path = StringField()
    orig_pv_volume_name = StringField()
    orig_pv_ephemeral_type = BooleanField()
    orig_pv_access_mode = StringField()
    orig_pv_sharing_policy = StringField()


class ComponentSpec(Document):
    orig_ce_component_name = StringField()
    orig_ce_component_spec_images = ListField(StringField())
    orig_ce_component_spec_num_of_instances = IntField()
    orig_ce_component_spec_restart_policy = StringField()
    orig_ce_component_spec_command_line_params_command = ListField(StringField())
    orig_ce_component_spec_command_line_params_command_args = ListField(StringField())
    orig_ce_component_spec_exposed_interfaces = ListField(ReferenceField(ExposedInterfaces))
    orig_ce_component_spec_compute_resource_profile_cpuarchtype = StringField()
    orig_ce_component_spec_compute_resource_profile_numcpu_whole = StringField()
    orig_ce_component_spec_compute_resource_profile_numcpu_decimal = FloatField()
    orig_ce_component_spec_compute_resource_profile_numcpu_millivcpu = StringField()
    orig_ce_component_spec_compute_resource_profile_memory = IntField()
    orig_ce_component_spec_compute_resource_profile_diskstorage = IntField()
    orig_ce_component_spec_compute_resource_profile_gpu = ListField(ReferenceField(Gpu))
    orig_ce_component_spec_compute_resource_profile_vpu = IntField()
    orig_ce_component_spec_compute_resource_profile_fpga = IntField()
    orig_ce_component_spec_compute_resource_profile_hugepages = ListField(ReferenceField(HugePages))
    orig_ce_component_spec_compute_resource_profile_cpuexclusivity = BooleanField()
    orig_ce_component_spec_comp_env_params = ListField(ReferenceField(CompEnvParams))
    orig_ce_component_spec_deployment_config_config_type = StringField()
    orig_ce_component_spec_deployment_config_contents = StringField()
    orig_ce_component_spec_persistent_volumes = ListField(ReferenceField(PersistentVolumes))


class OriginatingArtefactManagement(Document):
    orig_am_federation_context_id = StringField()
    orig_am_artefact_id = StringField()
    orig_am_app_provider_id = StringField()
    orig_am_artefact_name = StringField()
    orig_am_artefact_version_info = StringField()
    orig_am_artefact_description = StringField()
    orig_am_artefact_virt_type = StringField()
    orig_am_artefact_filename = StringField()
    orig_am_artefact_file_format = StringField()
    orig_am_artefact_descriptor_type = StringField()
    orig_am_repo_type = StringField()
    orig_am_artefact_repo_location_repo_url = StringField()
    orig_am_artefact_repo_location_user_name = StringField()
    orig_am_artefact_repo_location_password = StringField()
    orig_am_artefact_repo_location_token = StringField()
    orig_am_artefact_file = StringField()
    orig_am_component_spec = StringField()
    #orig_am_component_spec = ListField(ReferenceField(ComponentSpec))


class OriginatingArtefactManagementOriginatingOP(Document):
    orig_am_federation_context_id = StringField()
    orig_am_artefact_id = StringField()
    orig_am_app_provider_id = StringField()
    orig_am_artefact_name = StringField()
    orig_am_artefact_version_info = StringField()
    orig_am_artefact_description = StringField()
    orig_am_artefact_virt_type = StringField()
    orig_am_artefact_filename = StringField()
    orig_am_artefact_file_format = StringField()
    orig_am_artefact_descriptor_type = StringField()
    orig_am_repo_type = StringField()
    orig_am_artefact_repo_location_repo_url = StringField()
    orig_am_artefact_repo_location_user_name = StringField()
    orig_am_artefact_repo_location_password = StringField()
    orig_am_artefact_repo_location_token = StringField()
    orig_am_artefact_file = StringField()
    orig_am_component_spec = StringField()
    partner_federation_id = StringField()


class OriginatingArtefactFileManagement(Document):
    orig_af_federation_context_id = StringField()
    orig_af_file_id = StringField()
    orig_af_app_provider_id = StringField()
    orig_af_file_name = StringField()
    orig_af_file_description = StringField()
    orig_af_file_version_info = StringField()
    orig_af_file_type = StringField()
    orig_af_checksum = StringField()
    orig_af_img_os_type_architecture = StringField()
    orig_af_img_os_type_distribution = StringField()
    orig_af_img_os_type_version = StringField()
    orig_af_img_os_type_license = StringField()
    orig_af_img_ins_set_arch = StringField()
    orig_af_repo_type = StringField()
    orig_af_file_repo_location_repo_url = StringField()
    orig_af_file_repo_location_user_name = StringField()
    orig_af_file_repo_location_password = StringField()
    orig_af_file_repo_location_token = StringField()
    orig_af_file = StringField()


#####################################
# Application Onboarding Management #
#####################################
class OriginatingApplicationOnboardingManagement(Document):
    orig_ao_federation_context_id = StringField()
    orig_ao_app_id = StringField()
    orig_ao_app_provider_id = StringField()
    orig_ao_app_deployment_zones = ListField(StringField())
    orig_ao_app_meta_data_app_name = StringField()
    orig_ao_app_meta_data_version = StringField()
    orig_ao_app_meta_data_app_description = StringField()
    orig_ao_app_meta_data_mobility_support = BooleanField()
    orig_ao_app_meta_data_access_token = StringField()
    orig_ao_app_meta_data_category = StringField()
    orig_ao_app_qos_profile_latency_constraints = StringField()
    orig_ao_app_qos_profile_bandwidth_required = IntField()
    orig_ao_app_qos_profile_multi_user_clients = StringField()
    orig_ao_app_qos_profile_no_of_users_per_app_inst = IntField()
    orig_ao_app_qos_profile_app_provisioning = BooleanField()
    orig_ao_app_component_specs = StringField()
    orig_ao_app_status_callback_link = StringField()


class OriginatingApplicationOnboardingManagementUpdate(Document):
    app_qos_profile_latency_constraints = StringField()
    app_qos_profile_bandwidth_required = IntField()
    app_qos_profile_multi_user_clients = StringField()
    app_qos_profile_no_of_users_per_app_inst = IntField()
    app_qos_profile_app_provisioning = BooleanField()
    app_component_specs = StringField()
    federation_context_app_id = ReferenceField(OriginatingApplicationOnboardingManagement)


class OriginatingApplicationOnboardingManagementOriginatingOP(Document):
    orig_ao_federation_context_id = StringField()
    orig_ao_app_id = StringField()
    orig_ao_app_provider_id = StringField()
    orig_ao_app_deployment_zones = ListField(StringField())
    orig_ao_app_meta_data_app_name = StringField()
    orig_ao_app_meta_data_version = StringField()
    orig_ao_app_meta_data_app_description = StringField()
    orig_ao_app_meta_data_mobility_support = BooleanField()
    orig_ao_app_meta_data_access_token = StringField()
    orig_ao_app_meta_data_category = StringField()
    orig_ao_app_qos_profile_latency_constraints = StringField()
    orig_ao_app_qos_profile_bandwidth_required = IntField()
    orig_ao_app_qos_profile_multi_user_clients = StringField()
    orig_ao_app_qos_profile_no_of_users_per_app_inst = IntField()
    orig_ao_app_qos_profile_app_provisioning = BooleanField()
    orig_ao_app_component_specs = StringField()
    orig_ao_app_status_callback_link = StringField()
    partner_federation_id = StringField()


class OriginatingApplicationOnboardingManagementUpdateOriginatingOP(Document):
    app_qos_profile_latency_constraints = StringField()
    app_qos_profile_bandwidth_required = IntField()
    app_qos_profile_multi_user_clients = StringField()
    app_qos_profile_no_of_users_per_app_inst = IntField()
    app_qos_profile_app_provisioning = BooleanField()
    app_component_specs = StringField()
    federation_context_app_id = ReferenceField(OriginatingApplicationOnboardingManagementOriginatingOP)
    partner_federation_id = StringField()


#####################################
# Application Deployment Management #
#####################################
class OriginatingApplicationDeploymentManagement(Document):
    orig_ad_federation_context_id = StringField()
    orig_ad_instance_id = StringField()
    orig_ad_app_id = StringField()
    orig_ad_app_version = StringField()
    orig_ad_app_provider_id = StringField()
    orig_ad_zone_info_zone_id = StringField()
    orig_ad_zone_info_flavour_id = StringField()
    orig_ad_zone_info_resource_consumption = StringField()
    orig_ad_zone_info_res_pool = StringField()
    orig_ad_app_inst_callback_link = StringField()


class OriginatingApplicationDeploymentManagementOriginatingOP(Document):
    orig_ad_federation_context_id = StringField()
    orig_ad_instance_id = StringField()
    orig_ad_app_id = StringField()
    orig_ad_app_version = StringField()
    orig_ad_app_provider_id = StringField()
    orig_ad_zone_info_zone_id = StringField()
    orig_ad_zone_info_flavour_id = StringField()
    orig_ad_zone_info_resource_consumption = StringField()
    orig_ad_zone_info_res_pool = StringField()
    orig_ad_app_inst_callback_link = StringField()
    partner_federation_id = StringField()
