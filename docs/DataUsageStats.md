# DataUsageStats

Specifies the data usage metric of the data stored on the Cohesity Cluster or Storage Domains (View Boxes).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_data_written_bytes** | **int** | Specifies the total data written on cloud tiers, as computed by the Cohesity Cluster. | [optional] 
**cloud_data_written_bytes_timestamp_usec** | **int** | Specifies Timestamp of CloudDataWrittenBytes. | [optional] 
**cloud_total_physical_usage_bytes** | **int** | Specifies the total cloud capacity, as computed by the Cohesity Cluster, after the size of the data has been reduced by change-block tracking, compression and deduplication. | [optional] 
**cloud_total_physical_usage_bytes_timestamp_usec** | **int** | Specifies Timestamp of CloudTotalPhysicalUsageBytes. | [optional] 
**data_in_bytes** | **int** | Specifies the data read from the protected objects by the Cohesity Cluster before any data reduction using deduplication and compression. | [optional] 
**data_in_bytes_after_dedup** | **int** | Specifies the size of the data has been reduced by change-block tracking and deduplication but before compression or data is replicated to other nodes as per RF or Erasure Coding policy. | [optional] 
**data_in_bytes_after_dedup_timestamp_usec** | **int** | Specifies Timestamp of DataInBytesAfterDedup. | [optional] 
**data_in_bytes_timestamp_usec** | **int** | Specifies Timestamp of DataInBytes. | [optional] 
**data_protect_logical_usage_bytes** | **int** | Specifies the logical data used by Data Protect on Cohesity cluster. | [optional] 
**data_protect_logical_usage_bytes_timestamp_usec** | **int** | Specifies Timestamp of DataProtectLogicalUsageBytes. | [optional] 
**data_protect_physical_usage_bytes** | **int** | Specifies the physical data used by Data Protect on Cohesity cluster. | [optional] 
**data_protect_physical_usage_bytes_timestamp_usec** | **int** | Specifies Timestamp of DataProtectPhysicalUsageBytes. | [optional] 
**data_written_bytes** | **int** | Specifies the data written after it has been reduced by deduplication and compression. This does not include resiliency impact. | [optional] 
**data_written_bytes_timestamp_usec** | **int** | Specifies Timestamp of DataWrittenBytes. | [optional] 
**file_services_logical_usage_bytes** | **int** | Specifies the logical data used by File services on Cohesity cluster. | [optional] 
**file_services_logical_usage_bytes_timestamp_usec** | **int** | Specifies Timestamp of FileServicesLogicalUsageBytes. | [optional] 
**file_services_physical_usage_bytes** | **int** | Specifies the physical data used by File services on Cohesity cluster. | [optional] 
**file_services_physical_usage_bytes_timestamp_usec** | **int** | Specifies Timestamp of FileServicesPhysicalUsageBytes. | [optional] 
**local_data_written_bytes** | **int** | Specifies the total data written on local tiers, as computed by the Cohesity Cluster, after the size of the data has been reduced by change-block tracking, deduplication and compression. This does not include resiliency impact. | [optional] 
**local_data_written_bytes_timestamp_usec** | **int** | Specifies Timestamp of LocalDataWrittenBytes. | [optional] 
**local_tier_resiliency_impact_bytes** | **int** | Specifies the size of the data has been replicated to other nodes as per RF or Erasure Coding policy. | [optional] 
**local_tier_resiliency_impact_bytes_timestamp_usec** | **int** | Specifies Timestamp of LocalTierResiliencyImpactBytes. | [optional] 
**local_total_physical_usage_bytes** | **int** | Specifies the total local capacity, as computed by the Cohesity Cluster, after the size of the data has been reduced by change-block tracking, compression and deduplication. | [optional] 
**local_total_physical_usage_bytes_timestamp_usec** | **int** | Specifies Timestamp of LocalTotalPhysicalUsageBytes. | [optional] 
**num_directories** | **int** | Specifies the number of directories. | [optional] 
**num_files** | **int** | Specifies the number of files. | [optional] 
**outdated_logical_usage_bytes** | **int** | Specifies the logical usage as computed by the Cohesity Cluster. This field is computed on a same frequency as &#39;StorageConsumedBytes&#39;, and it may not be the latest value. It is used to compute reduction ratio. | [optional] 
**outdated_logical_usage_bytes_timestamp_usec** | **int** | Specifies Timestamp of OutdatedLogicalUsageBytes. | [optional] 
**storage_consumed_bytes** | **int** | Specifies the total capacity, as computed by the Cohesity Cluster, after the size of the data has been reduced by change-block tracking, compression and deduplication. This includes resiliency impact. | [optional] 
**storage_consumed_bytes_timestamp_usec** | **int** | Specifies Timestamp of StorageConsumedBytes. | [optional] 
**total_logical_usage_bytes** | **int** | Provides the combined data residing on protected objects. The size of data before reduction by deduplication and compression. | [optional] 
**total_logical_usage_bytes_timestamp_usec** | **int** | Specifies Timestamp of TotalLogicalUsageBytes. | [optional] 
**unique_physical_data_bytes** | **int** | Specifies the unique physical data usage in bytes. | [optional] 

## Example

```python
from cohesity_sdk.models.data_usage_stats import DataUsageStats

# TODO update the JSON string below
json = "{}"
# create an instance of DataUsageStats from a JSON string
data_usage_stats_instance = DataUsageStats.from_json(json)
# print the JSON string representation of the object
print(DataUsageStats.to_json())

# convert the object into a dict
data_usage_stats_dict = data_usage_stats_instance.to_dict()
# create an instance of DataUsageStats from a dict
data_usage_stats_from_dict = DataUsageStats.from_dict(data_usage_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


