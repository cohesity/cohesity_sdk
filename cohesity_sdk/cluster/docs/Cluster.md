# Cluster

Specifies the cluster details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aes_encryption_mode** | **str** | Specifies the default AES Encryption mode on the cluster. | [optional] 
**amqp_target_config** | [**ClusterAMQPTargetConfig**](ClusterAMQPTargetConfig.md) |  | [optional] 
**apps_subnet** | [**SubnetDefinition**](SubnetDefinition.md) |  | [optional] 
**assigned_racks_count** | **int** | Specifies the number of racks in cluster with at least one rack assigned. | [optional] 
**attempt_agent_ports_upgrade** | **bool** | To attempt agent connection on port 21213 first. | [optional] 
**auth_support_for_pkg_downloads** | **bool** | Specifies if cluster can support authHeaders for upgrade. | [optional] 
**auth_type** | **str** | Specifies the authentication scheme for the cluster. | [optional] 
**authorized_ssh_public_keys** | **List[str]** | Specifies a list of authorized SSH public keys that have been uploaded to this Cohesity Cluster. | [optional] 
**available_metadata_space** | **int** | Specifies information about storage available for metadata | [optional] 
**banner_enabled** | **bool** | Specifies whether UI banner is enabled on the cluster or not. | [optional] 
**centralized_patching_enabled** | **bool** | Specifies if cluster can support patching via Helios. | [optional] 
**chassis_count** | **int** | Specifies the number of chassis in cluster. | [optional] 
**cloud_rf1_enabled** | **bool** | Specifies if Cloud RF1 is enabled. | [optional] 
**cluster_audit_log_config** | [**ClusterAuditLogConfig**](ClusterAuditLogConfig.md) |  | [optional] 
**cluster_deployment_type** | **str** | Type of Cluster Deployment. | [optional] 
**cluster_size** | **str** | Specifies the size of the cloud platforms. | [optional] [readonly] 
**cluster_software_version** | **str** | Specifies the current release of the Cohesity software running on the Cohesity Cluster. | [optional] 
**cluster_type** | **str** | Specifies the environment type of the cluster. | [optional] [readonly] 
**cohesion_cluster_params** | [**CohesionClusterConfigParams**](CohesionClusterConfigParams.md) |  | [optional] 
**created_time_msecs** | **int** | Specifies the time when the Cohesity Cluster was created. | [optional] 
**current_op_scheduled_time_secs** | **int** | Specifies the time scheduled by the Cohesity Cluster to start the current running operation. | [optional] 
**current_operation** | **str** | Specifies the current Cluster-level operation in progress. | [optional] 
**current_time_msecs** | **int** | Specifies the current system time on the Cohesity Cluster. | [optional] 
**description** | **str** | Description of the cluster. | [optional] 
**disk_count_by_tier** | [**List[CountByTier]**](CountByTier.md) | Specifies the number of disks on the cluster by Storage Tier. | [optional] 
**dns_server_ips** | **List[str]** | Specifies the IP addresses of the DNS Servers used by the Cohesity Cluster. | [optional] 
**domain_names** | **List[str]** | Specifies array of Domain Names. | [optional] 
**enable_active_monitoring** | **bool** | Specifies if Cohesity can receive monitoring information from the Cohesity Cluster. | [optional] 
**enable_encryption** | **bool** | Specifies whether or not encryption is enabled. If encryption is enabled, all data on the Cluster will be encrypted. | [optional] [readonly] 
**enable_patches_download** | **bool** | Specifies whether to enable downloading patches from Cohesity download site. | [optional] 
**enable_upgrade_pkg_polling** | **bool** | If &#39;true&#39;, Cohesity&#39;s upgrade server is polled for new releases. | [optional] 
**encryption_key_rotation_period_secs** | **int** | Specifies the period of time (in seconds) when encryption keys are rotated | [optional] 
**eula_config** | [**EulaConfig**](EulaConfig.md) |  | [optional] 
**fault_tolerance_level** | **str** | Specifies the level which &#39;MetadataFaultToleranceFactor&#39; applies to. | [optional] 
**file_services_audit_log_config** | [**AuditLogConfig**](AuditLogConfig.md) |  | [optional] 
**fips_cert_version** | **str** | FIPS Certification Version | [optional] [readonly] 
**gateway** | **str** | Specifies the gateway IP address. | [optional] 
**google_analytics_enabled** | **bool** | Specifies whether Google Analytics is enabled. | [optional] 
**hardware_encryption_enabled** | **bool** | Specifies if hardware encryption(SED) is enabled. | [optional] 
**hardware_info** | [**ClusterHardwareInfo**](ClusterHardwareInfo.md) |  | [optional] 
**id** | **int** | Specifies the cluster id of the cluster. | [optional] [readonly] 
**incarnation_id** | **int** | Specifies the incarnation id of the cluster. | [optional] [readonly] 
**ip_preference** | **int** | Specifies IP preference. | [optional] 
**is_athena_subnet_clash** | **bool** | Specifies whether or not athena subnet is clashing with some other internal subnet | [optional] 
**is_cluster_mfa_enabled** | **bool** | Specifies if MFA is enabled on cluster. | [optional] 
**is_documentation_local** | **bool** | Specifies what version of the documentation is used. | [optional] 
**is_patch_apply_aborted** | **bool** | Specifies that the patch apply was aborted. | [optional] 
**is_patch_revert_aborted** | **bool** | Specifies that the patch revert was aborted. | [optional] 
**is_upgrade_aborted** | **bool** | Specifies if the current upgrade has been aborted. | [optional] 
**kms_server_id** | **int** | Specifies the KMS Server Id. | [optional] 
**language_locale** | **str** | Specifies the language and locale for this Cohesity Cluster. | [optional] 
**license_state** | [**LicenseState**](LicenseState.md) |  | [optional] 
**load_balancer_vip_config** | [**LoadBalancerConfig**](LoadBalancerConfig.md) |  | [optional] 
**local_auth_domain_name** | **str** | Specifies domain name for SMB local authentication. | [optional] 
**local_groups_enabled** | **bool** | Specifies whether to enable local groups on cluster. | [optional] 
**metadata** | [**ClusterMetadataRequest**](ClusterMetadataRequest.md) |  | [optional] 
**metadata_fault_tolerance_factor** | **int** | Specifies metadata fault tolerance setting for the cluster. | [optional] 
**minimum_failure_domains_needed** | **int** | Specifies minimum failure domains needed in the cluster. | [optional] 
**multi_tenancy_enabled** | **bool** | Specifies if multi tenancy is enabled in the cluster. | [optional] 
**name** | **str** | Name of the cluster. | [optional] 
**network_config** | [**ClusterCreateNetworkConfig**](ClusterCreateNetworkConfig.md) |  | [optional] 
**node_count** | **int** | Specifies the number of Nodes in the Cohesity Cluster. | [optional] 
**node_ips** | **str** | Specifies IP addresses of nodes in the cluster. | [optional] 
**ntp_settings** | [**NTPSettings**](NTPSettings.md) |  | [optional] 
**patch_apply_failure_error_message** | **str** | Specifies the error message for a failed patch apply. | [optional] 
**patch_revert_failure_error_message** | **str** | Specifies the error message for a failed patch revert. | [optional] 
**patch_revert_version** | **str** | Specifies the target version for reverting the patch. | [optional] 
**patch_target_version** | **str** | Specifies the target version for applying the patch. | [optional] 
**patch_v2_reverts_allowed** | **bool** | Specifies if cluster can support patch reverts. | [optional] 
**patch_version** | **str** | Specifies the patch version applied to cluster. | [optional] 
**pcie_ssd_tier_rebalance_delay_secs** | **int** | Specifies the rebalance delay in seconds for cluster PcieSSD storage tier. | [optional] 
**proto_rpc_encryption_enabled** | **bool** | Specifies if protorpc encryption is enabled or not. | [optional] 
**proxy_server_config** | [**ClusterProxyServerConfig**](ClusterProxyServerConfig.md) |  | [optional] 
**proxy_vm_subnet** | **str** | Specifies the subnet reserved for ProxyVM. | [optional] 
**reverse_tunnel_enabled** | **bool** | If &#39;true&#39;, Cohesity&#39;s Remote Tunnel is enabled. | [optional] 
**reverse_tunnel_end_time_msecs** | **int** | Specifies the end time in milliseconds since epoch until when the reverse tunnel will stay enabled. | [optional] 
**rigel_cluster_params** | [**RigelClusterConfigParams**](RigelClusterConfigParams.md) |  | [optional] 
**s3_virtual_hosted_domain_names** | **List[str]** | Specifies the list of domain names for S3. | [optional] 
**sata_hdd_tier_admission_control** | **int** | Specifies the admission control for cluster SATAHDD storage tier. | [optional] 
**schema_info_list** | [**List[SchemaInfo]**](SchemaInfo.md) | Specifies the time series schema info of the cluster. | [optional] 
**security_mode_dod** | **bool** | Specifies if Security Mode DOD is enabled or not. | [optional] 
**smb_ad_disabled** | **bool** | Specifies if Active Directory should be disabled for authentication of SMB shares. | [optional] 
**smb_multichannel_enabled** | **bool** | Specifies whether SMB multichannel is enabled on the cluster. | [optional] 
**software_type** | **str** |  Specifies the type of Cohesity Software. | [optional] 
**split_key_host_access** | **bool** | Specifies if split key host access is enabled. | [optional] 
**stats** | [**ClusterStats**](ClusterStats.md) |  | [optional] 
**supported_config** | [**SupportedConfig**](SupportedConfig.md) |  | [optional] 
**sw_version** | **str** | Software version of the cluster. | [optional] [readonly] 
**target_software_version** | **str** | Specifies the Cohesity release that this Cluster is being upgraded to if an upgrade operation is in progress. | [optional] 
**tenant_viewbox_sharing_enabled** | **bool** | Specifies whether multiple tenants can be placed on the same viewbox. | [optional] 
**tiering_audit_log_config** | [**AuditLogConfig**](AuditLogConfig.md) |  | [optional] 
**timezone** | **str** | Specifies the timezone to use. | [optional] 
**trust_domain** | **str** | Specifies the Trust Domain. | [optional] 
**turbo_mode** | **bool** | Specifies if the cluster is in Turbo mode.. | [optional] 
**type** | **str** | Specifies the type of the cluster. | [optional] [readonly] 
**upgrade_failure_error_string** | **str** | Error string to capture why the upgrade failed. | [optional] 
**use_default_agent_ports** | **bool** | To use default ports 50051 &amp; 21213. | [optional] 
**use_heimdall** | **bool** | Specifies whether to enable Heimdall which tells whether services should use temporary fleet instances to mount disks by talking to Heimdall. | [optional] 
**used_metadata_space_pct** | **float** | Measures the percentage about storage used for metadata over the total storage available for metadata | [optional] 
**views_global_settings** | [**ViewsGlobalSettings**](ViewsGlobalSettings.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster import Cluster

# TODO update the JSON string below
json = "{}"
# create an instance of Cluster from a JSON string
cluster_instance = Cluster.from_json(json)
# print the JSON string representation of the object
print(Cluster.to_json())

# convert the object into a dict
cluster_dict = cluster_instance.to_dict()
# create an instance of Cluster from a dict
cluster_from_dict = Cluster.from_dict(cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


