# UpdateStorageDomainParam

Specifies the parameter to update a Storage Domain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_domain_name** | **str** | Specifies the Active Directory domain name that this Storage Domain is mapped to. | [optional] 
**blob_brick_size_bytes** | **int** | Specifies the brick size used for blobs in this Storage Domain. | [optional] 
**cloud_domain_id** | **int** | Specifies the cloud domain Id. | [optional] 
**cloud_down_water_fall_params** | [**CloudDownWaterFallParams**](CloudDownWaterFallParams.md) | Specifies the cloud down water fall parameters for this Storage Domain. | [optional] 
**cluster_partition_id** | **int** | Specifies the cluster partition id of the Storage Domain. | 
**cluster_partition_name** | **str** | Specifies the cluster partition name of the Storage Domain. | [optional] [readonly] 
**default_user_quota** | [**QuotaPolicy**](QuotaPolicy.md) | Specifies a default user quota limit for users within views in this Storage Domain. | [optional] 
**default_view_quota** | [**QuotaPolicy**](QuotaPolicy.md) | Specifies a default logical quota limit for all views in this Storage Domain. This quota can be overwritten by a view level quota. | [optional] 
**dek_rotation_enabled** | **bool** | Specifies whether DEK(Data Encryption Key) rotation is enabled for this Storage Domain. This is applicable only when the Storage Domain uses AWS or similar KMS in which the KEK (Key Encryption Key) is not created and maintained by Cohesity. For Internal KMS and keys stored in Safenet servers, DEK rotation will not be performed. | [optional] 
**direct_archive_enabled** | **bool** | Specifies whether to enable driect archive on this Storage Domain. If enabled, this Storage Domain can be used as a staging area while copying a large dataset that can&#39;t fit on the cluster to an external target. | [optional] 
**file_count_by_size** | [**List[FileCount]**](FileCount.md) | Specifies the file count by size for the View. | [optional] [readonly] 
**id** | **int** | Specifies the Storage Domain id. | [optional] [readonly] 
**kerberos_realm_name** | **str** | Specifies the Kerberos realm name that this Storage Domain is mapped to. | [optional] 
**kms_server_id** | **int** | Specifies the associated KMS server id. | [optional] 
**last_key_rotation_timestamp_msecs** | **int** | Last key rotation timestamp in msecs for storage domain. | [optional] 
**ldap_provider_id** | **int** | Specifies the LDAP provider id that this Storage Domain is mapped to. | [optional] 
**name** | **str** | Specifies the Storage Domain name. | 
**nis_domain_names** | **List[str]** | Specifies the NIS domain names that this Storage Domain is mapped to. | [optional] 
**physical_quota** | [**QuotaPolicy**](QuotaPolicy.md) | Specifies a quota limit for physical usage of this Storage Domain. This quota defines a limit of data that can be physically (after data size is reduced by block tracking, compression and deduplication) stored on this storage domain. A new write will not be allowed when the storage domain usage will exceeds the specified quota. Due to the latency of calculating usage across all nodes, the actual storage domain usage may exceed the quota limit by a little bit. | [optional] 
**recommended** | **bool** | Specifies whether Storage Domain is recommended for the specified View template. | [optional] [readonly] 
**removal_state** | **str** | Specifies the current removal state of the Storage Domain. &#39;DontRemove&#39; means the state of object is functional and it is not being removed. &#39;MarkedForRemoval&#39; means the object is being removed. &#39;OkToRemove&#39; means the object has been removed on the Cohesity Cluster and if the object is physical, it can be removed from the Cohesity Cluster. | [optional] [readonly] 
**s3_buckets_enabled** | **bool** | Specifies whether to enable creation of S3 bucket on this Storage Domain. | [optional] 
**schemas** | [**List[ModelSchema]**](ModelSchema.md) | Specifies the Storage Domain schemas. | [optional] [readonly] 
**stats** | [**DataUsageStats**](DataUsageStats.md) | Specifies the Storage Domain stats. | [optional] 
**storage_policy** | [**StoragePolicy**](StoragePolicy.md) | Specifies the storage policy for this Storage Domain. | [optional] 
**subnet_whitelist** | [**List[Subnet]**](Subnet.md) | Specifies a list of Subnets with IP addresses that have permissions to access the Storage Domain. | [optional] 
**tenant_ids** | **List[str]** | Specifies a list of tenant ids that that Storage Domain belongs. There can only be one tenant id in this field unless Storage Domain sharing between tenants is allowed on this cluster. | [optional] 
**treat_file_sync_as_data_sync** | **bool** | If &#39;true&#39;, when the Cohesity Cluster is writing to a file, the file modification time is not persisted synchronously during the file write, so the modification time may not be accurate. (Typically the file modification time is off by 30 seconds but it can be longer.) | [optional] 
**vault_id** | **int** | Specifies the vault Id associated with cloud domain ID. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.update_storage_domain_param import UpdateStorageDomainParam

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStorageDomainParam from a JSON string
update_storage_domain_param_instance = UpdateStorageDomainParam.from_json(json)
# print the JSON string representation of the object
print(UpdateStorageDomainParam.to_json())

# convert the object into a dict
update_storage_domain_param_dict = update_storage_domain_param_instance.to_dict()
# create an instance of UpdateStorageDomainParam from a dict
update_storage_domain_param_from_dict = UpdateStorageDomainParam.from_dict(update_storage_domain_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


