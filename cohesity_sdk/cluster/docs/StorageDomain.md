# StorageDomain

Specifies a Storage Domain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_domain_name** | **str** | Specifies the Active Directory domain name that this Storage Domain is mapped to. | [optional] 
**blob_brick_size_bytes** | **int** | Specifies the brick size used for blobs in this Storage Domain. | [optional] 
**cloud_domain_id** | **int** | Specifies the cloud domain Id. | [optional] 
**cloud_down_water_fall_params** | [**CloudDownWaterFallParams**](CloudDownWaterFallParams.md) |  | [optional] 
**cluster_partition_id** | **int** | Specifies the cluster partition id of the Storage Domain. | 
**cluster_partition_name** | **str** | Specifies the cluster partition name of the Storage Domain. | [optional] [readonly] 
**default_user_quota** | [**QuotaPolicy**](QuotaPolicy.md) |  | [optional] 
**default_view_quota** | [**QuotaPolicy**](QuotaPolicy.md) |  | [optional] 
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
**physical_quota** | [**QuotaPolicy**](QuotaPolicy.md) |  | [optional] 
**recommended** | **bool** | Specifies whether Storage Domain is recommended for the specified View template. | [optional] [readonly] 
**removal_state** | **str** | Specifies the current removal state of the Storage Domain. &#39;DontRemove&#39; means the state of object is functional and it is not being removed. &#39;MarkedForRemoval&#39; means the object is being removed. &#39;OkToRemove&#39; means the object has been removed on the Cohesity Cluster and if the object is physical, it can be removed from the Cohesity Cluster. | [optional] [readonly] 
**s3_buckets_enabled** | **bool** | Specifies whether to enable creation of S3 bucket on this Storage Domain. | [optional] 
**schemas** | [**List[ModelSchema]**](ModelSchema.md) | Specifies the Storage Domain schemas. | [optional] [readonly] 
**stats** | [**DataUsageStats**](DataUsageStats.md) |  | [optional] 
**storage_policy** | [**StoragePolicy**](StoragePolicy.md) |  | [optional] 
**subnet_whitelist** | [**List[Subnet]**](Subnet.md) | Specifies a list of Subnets with IP addresses that have permissions to access the Storage Domain. | [optional] 
**tenant_ids** | **List[str]** | Specifies a list of tenant ids that that Storage Domain belongs. There can only be one tenant id in this field unless Storage Domain sharing between tenants is allowed on this cluster. | [optional] 
**treat_file_sync_as_data_sync** | **bool** | If &#39;true&#39;, when the Cohesity Cluster is writing to a file, the file modification time is not persisted synchronously during the file write, so the modification time may not be accurate. (Typically the file modification time is off by 30 seconds but it can be longer.) | [optional] 
**vault_id** | **int** | Specifies the vault Id associated with cloud domain ID. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.storage_domain import StorageDomain

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDomain from a JSON string
storage_domain_instance = StorageDomain.from_json(json)
# print the JSON string representation of the object
print(StorageDomain.to_json())

# convert the object into a dict
storage_domain_dict = storage_domain_instance.to_dict()
# create an instance of StorageDomain from a dict
storage_domain_from_dict = StorageDomain.from_dict(storage_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


