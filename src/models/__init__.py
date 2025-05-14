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

# flake8: noqa
from __future__ import absolute_import
# import models into model package
from models.app_app_id_body import AppAppIdBody
from models.app_component_specs import AppComponentSpecs
from models.app_component_specs_inner import AppComponentSpecsInner
from models.app_id_zone_forbid_body import AppIdZoneForbidBody
from models.app_identifier import AppIdentifier
from models.app_meta_data import AppMetaData
from models.app_provider_id import AppProviderId
from models.app_qo_s_profile import AppQoSProfile
from models.application_lcm_body import ApplicationLcmBody
from models.application_onboarding_body import ApplicationOnboardingBody
from models.artefact_id import ArtefactId
from models.authorization_token import AuthorizationToken
from models.cpu_arch_type import CPUArchType
from models.callback_credentials import CallbackCredentials
from models.command_line_params import CommandLineParams
from models.comp_env_params import CompEnvParams
from models.component_spec import ComponentSpec
from models.compute_resource_info import ComputeResourceInfo
from models.country_code import CountryCode
from models.deployment_config import DeploymentConfig
from models.federation_context_id import FederationContextId
from models.federation_context_id_artefact_body import FederationContextIdArtefactBody
from models.federation_context_id_files_body import FederationContextIdFilesBody
from models.federation_context_id_partner_body import FederationContextIdPartnerBody
from models.federation_context_idapplicationlcm_zone_info import FederationContextIdapplicationlcmZoneInfo
from models.federation_context_idapplicationlcmappapp_idapp_providerapp_provider_id_app_instance_info import FederationContextIdapplicationlcmappappIdappProviderappProviderIdAppInstanceInfo
from models.federation_context_idapplicationonboardingappapp_id_app_component_specs import FederationContextIdapplicationonboardingappappIdAppComponentSpecs
from models.federation_context_idapplicationonboardingappapp_id_app_upd_qo_s_profile import FederationContextIdapplicationonboardingappappIdAppUpdQoSProfile
from models.federation_identifier import FederationIdentifier
from models.federation_request_data import FederationRequestData
from models.federation_response_data import FederationResponseData
from models.file_id import FileId
from models.fixed_network_ids import FixedNetworkIds
from models.flavour import Flavour
from models.flavour_id import FlavourId
from models.fqdn import Fqdn
from models.geo_location import GeoLocation
from models.gpu_info import GpuInfo
from models.huge_page import HugePage
from models.inline_response2001 import InlineResponse2001
from models.inline_response2002 import InlineResponse2002
from models.inline_response2005 import InlineResponse2005
from models.inline_response2006 import InlineResponse2006
from models.inline_response2007 import InlineResponse2007
from models.inline_response2007_app_deployment_zones import InlineResponse2007AppDeploymentZones
from models.inline_response2008 import InlineResponse2008
from models.inline_response2008_accesspoint_info import InlineResponse2008AccesspointInfo
from models.inline_response2009 import InlineResponse2009
from models.inline_response202 import InlineResponse202
from models.instance_identifier import InstanceIdentifier
from models.instance_state import InstanceState
from models.interface_details import InterfaceDetails
from models.invalid_param import InvalidParam
from models.ipv4_addr import Ipv4Addr
from models.ipv6_addr import Ipv6Addr
from models.mcc import Mcc
from models.mnc import Mnc
from models.mobile_network_ids import MobileNetworkIds
from models.os_type import OSType
from models.object_repo_location import ObjectRepoLocation
from models.persistent_volume_details import PersistentVolumeDetails
from models.port import Port
from models.problem_details import ProblemDetails
from models.service_endpoint import ServiceEndpoint
from models.uri import Uri
from models.vcpu import Vcpu
from models.version import Version
from models.virt_image_type import VirtImageType
from models.zone_details import ZoneDetails
from models.zone_identifier import ZoneIdentifier
from models.zone_registered_data import ZoneRegisteredData
from models.zone_registered_data_network_resources import ZoneRegisteredDataNetworkResources
from models.zone_registered_data_zone_service_level_objs_info import ZoneRegisteredDataZoneServiceLevelObjsInfo
from models.zone_registered_data_zone_service_level_objs_info_jitter_ranges import ZoneRegisteredDataZoneServiceLevelObjsInfoJitterRanges
from models.zone_registered_data_zone_service_level_objs_info_latency_ranges import ZoneRegisteredDataZoneServiceLevelObjsInfoLatencyRanges
from models.zone_registered_data_zone_service_level_objs_info_throughput_ranges import ZoneRegisteredDataZoneServiceLevelObjsInfoThroughputRanges
from models.zone_registration_request_data import ZoneRegistrationRequestData
from models.zone_registration_response_data import ZoneRegistrationResponseData
