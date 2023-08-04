# UpdateStorageDomainParam

Specifies the parameter to update a Storage Domain.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the Storage Domain name. | 
**cluster_partition_id** | **int, none_type** | Specifies the cluster partition id of the Storage Domain. | 
**id** | **int, none_type** | Specifies the Storage Domain id. | [optional] [readonly] 
**cluster_partition_name** | **str, none_type** | Specifies the cluster partition name of the Storage Domain. | [optional] [readonly] 
**subnet_whitelist** | [**[Subnet], none_type**](Subnet.md) | Specifies a list of Subnets with IP addresses that have permissions to access the Storage Domain. | [optional] 
**storage_policy** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the storage policy for this Storage Domain. | [optional] 
**physical_quota** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies a quota limit for physical usage of this Storage Domain. This quota defines a limit of data that can be physically (after data size is reduced by block tracking, compression and deduplication) stored on this storage domain. A new write will not be allowed when the storage domain usage will exceeds the specified quota. Due to the latency of calculating usage across all nodes, the actual storage domain usage may exceed the quota limit by a little bit. | [optional] 
**cloud_down_water_fall_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the cloud down water fall parameters for this Storage Domain. | [optional] 
**default_view_quota** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies a default logical quota limit for all views in this Storage Domain. This quota can be overwritten by a view level quota. | [optional] 
**default_user_quota** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies a default user quota limit for users within views in this Storage Domain. | [optional] 
**s3_buckets_enabled** | **bool, none_type** | Specifies whether to enable creation of S3 bucket on this Storage Domain. | [optional] 
**ad_domain_name** | **str, none_type** | Specifies the Active Directory domain name that this Storage Domain is mapped to. | [optional] 
**nis_domain_names** | **[str], none_type** | Specifies the NIS domain names that this Storage Domain is mapped to. | [optional] 
**kerberos_realm_name** | **str, none_type** | Specifies the Kerberos realm name that this Storage Domain is mapped to. | [optional] 
**ldap_provider_id** | **int, none_type** | Specifies the LDAP provider id that this Storage Domain is mapped to. | [optional] 
**tenant_ids** | **[str], none_type** | Specifies a list of tenant ids that that Storage Domain belongs. There can only be one tenant id in this field unless Storage Domain sharing between tenants is allowed on this cluster. | [optional] 
**direct_archive_enabled** | **bool, none_type** | Specifies whether to enable driect archive on this Storage Domain. If enabled, this Storage Domain can be used as a staging area while copying a large dataset that can&#39;t fit on the cluster to an external target. | [optional] 
**blob_brick_size_bytes** | **int, none_type** | Specifies the brick size used for blobs in this Storage Domain. | [optional] 
**kms_server_id** | **int, none_type** | Specifies the associated KMS server id. | [optional] 
**dek_rotation_enabled** | **bool, none_type** | Specifies whether DEK(Data Encryption Key) rotation is enabled for this Storage Domain. This is applicable only when the Storage Domain uses AWS or similar KMS in which the KEK (Key Encryption Key) is not created and maintained by Cohesity. For Internal KMS and keys stored in Safenet servers, DEK rotation will not be performed. | [optional] 
**treat_file_sync_as_data_sync** | **bool, none_type** | If &#39;true&#39;, when the Cohesity Cluster is writing to a file, the file modification time is not persisted synchronously during the file write, so the modification time may not be accurate. (Typically the file modification time is off by 30 seconds but it can be longer.) | [optional] 
**recommended** | **bool, none_type** | Specifies whether Storage Domain is recommended for the specified View template. | [optional] [readonly] 
**stats** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the Storage Domain stats. | [optional] 
**schemas** | [**[Schema], none_type**](Schema.md) | Specifies the Storage Domain schemas. | [optional] [readonly] 
**file_count_by_size** | [**[FileCount], none_type**](FileCount.md) | Specifies the file count by size for the View. | [optional] [readonly] 
**cloud_domain_id** | **int, none_type** | Specifies the cloud domain Id. | [optional] 
**vault_id** | **int, none_type** | Specifies the vault Id associated with cloud domain ID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


