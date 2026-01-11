# DataUsageStatsDefinition

Specifies the data usage metric of the data stored on the Cohesity Cluster

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_data_written_bytes** | **int, none_type** | Specifies the total data written on cloud tiers, as computed by the Cohesity Cluster. | [optional] 
**cloud_data_written_bytes_timestamp_usec** | **int, none_type** | Specifies Timestamp of CloudDataWrittenBytes. | [optional] 
**cloud_total_physical_usage_bytes** | **int, none_type** | Specifies the total cloud capacity, as computed by the Cohesity Cluster, after the size of the data has been reduced by change-block tracking, compression and deduplication. | [optional] 
**cloud_total_physical_usage_bytes_timestamp_usec** | **int, none_type** | Specifies Timestamp of CloudTotalPhysicalUsageBytes. | [optional] 
**data_in_bytes** | **int, none_type** | Specifies the data read from the protected objects by the Cohesity Cluster before any data reduction using deduplication and compression. | [optional] 
**data_in_bytes_after_dedup** | **int, none_type** | Specifies the size of the data has been reduced by change-block tracking and deduplication but before compression or data is replicated to other nodes as per RF or Erasure Coding policy. | [optional] 
**data_in_bytes_after_dedup_timestamp_usec** | **int, none_type** | Specifies Timestamp of DataInBytesAfterDedup. | [optional] 
**data_in_bytes_prev** | **int, none_type** | Specifies the storage used before any data reduction using deduplication and compression. | [optional] 
**data_in_bytes_prev_timestamp_usec** | **int, none_type** | Specifies Timestamp of DataInBytesPrev | [optional] 
**data_in_bytes_timestamp_usec** | **int, none_type** | Specifies Timestamp of DataInBytes. | [optional] 
**data_protect_logical_usage_bytes** | **int, none_type** | Specifies the logical data used by Data Protect on Cohesity cluster. | [optional] 
**data_protect_logical_usage_bytes_timestamp_usec** | **int, none_type** | Specifies Timestamp of DataProtectLogicalUsageBytes. | [optional] 
**data_protect_physical_usage_bytes** | **int, none_type** | Specifies the physical data used by Data Protect on Cohesity cluster. | [optional] 
**data_protect_physical_usage_bytes_timestamp_usec** | **int, none_type** | Specifies Timestamp of DataProtectPhysicalUsageBytes. | [optional] 
**data_written_bytes** | **int, none_type** | Specifies the data written after it has been reduced by deduplication and compression. This does not include resiliency impact. | [optional] 
**data_written_bytes_prev** | **int, none_type** | Specifies the data written after it has been reduced by deduplication and compression at a previous time. | [optional] 
**data_written_bytes_prev_timestamp_usec** | **int, none_type** | Specifies Timestamp of DataWrittenBytesPrev | [optional] 
**data_written_bytes_timestamp_usec** | **int, none_type** | Specifies Timestamp of DataWrittenBytes. | [optional] 
**file_services_logical_usage_bytes** | **int, none_type** | Specifies the logical data used by File services on Cohesity cluster. | [optional] 
**file_services_logical_usage_bytes_timestamp_usec** | **int, none_type** | Specifies Timestamp of FileServicesLogicalUsageBytes. | [optional] 
**file_services_physical_usage_bytes** | **int, none_type** | Specifies the physical data used by File services on Cohesity cluster. | [optional] 
**file_services_physical_usage_bytes_timestamp_usec** | **int, none_type** | Specifies Timestamp of FileServicesPhysicalUsageBytes. | [optional] 
**local_data_written_bytes** | **int, none_type** | Specifies the total data written on local tiers, as computed by the Cohesity Cluster, after the size of the data has been reduced by change-block tracking, deduplication and compression. This does not include resiliency impact. | [optional] 
**local_data_written_bytes_timestamp_usec** | **int, none_type** | Specifies Timestamp of LocalDataWrittenBytes. | [optional] 
**local_tier_resiliency_impact_bytes** | **int, none_type** | Specifies the size of the data has been replicated to other nodes as per RF or Erasure Coding policy. | [optional] 
**local_tier_resiliency_impact_bytes_prev** | **int, none_type** | Specifies the size of the data has been replicated to other nodes as per RF or Erasure Coding policy at a specific time. | [optional] 
**local_tier_resiliency_impact_bytes_prev_timestamp_usec** | **int, none_type** | Specifies Timestamp of LocalTierResiliencyImpactBytesPrev. | [optional] 
**local_tier_resiliency_impact_bytes_timestamp_usec** | **int, none_type** | Specifies Timestamp of LocalTierResiliencyImpactBytes. | [optional] 
**local_total_physical_usage_bytes** | **int, none_type** | Specifies the total local capacity, as computed by the Cohesity Cluster, after the size of the data has been reduced by change-block tracking, compression and deduplication. | [optional] 
**local_total_physical_usage_bytes_timestamp_usec** | **int, none_type** | Specifies Timestamp of LocalTotalPhysicalUsageBytes. | [optional] 
**num_directories** | **int, none_type** | Specifies the number of directories. | [optional] 
**num_directories_prev** | **int, none_type** | Specifies the number of directories at a specific time. | [optional] 
**num_files** | **int, none_type** | Specifies the number of files. | [optional] 
**num_files_prev** | **int, none_type** | Specifies the number of files at a specific time. | [optional] 
**outdated_logical_usage_bytes** | **int, none_type** | Specifies the logical usage as computed by the Cohesity Cluster. | [optional] 
**outdated_logical_usage_bytes_timestamp_usec** | **int, none_type** | Specifies Timestamp of OutdatedLogicalUsageBytes. | [optional] 
**storage_consumed_bytes** | **int, none_type** | Specifies the total capacity, as computed by the Cohesity Cluster, after the size of the data has been reduced by change-block tracking, compression and deduplication. This includes resiliency impact. | [optional] 
**storage_consumed_bytes_prev** | **int, none_type** | Specifies the total capacity, as computed by the Cohesity Cluster, after the size of the data has been reduced by change-block tracking, compression and deduplication at a previous time to compare. | [optional] 
**storage_consumed_bytes_prev_timestamp_usec** | **int, none_type** | Specifies Timestamp of StorageConsumedBytesPrev. | [optional] 
**storage_consumed_bytes_timestamp_usec** | **int, none_type** | Specifies Timestamp of StorageConsumedBytes. | [optional] 
**total_logical_usage_bytes** | **int, none_type** | Provides the combined data residing on protected objects. The size of data before reduction by deduplication and compression. | [optional] 
**total_logical_usage_bytes_timestamp_usec** | **int, none_type** | Specifies Timestamp of TotalLogicalUsageBytes. | [optional] 
**unique_physical_data_bytes** | **int, none_type** | Specifies the unique physical data usage in bytes. | [optional] 
**unique_physical_data_bytes_timestamp_usec** | **int, none_type** | Specifies Timestamp of UniquePhysicalDataBytes. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


