# StoragePolicy

Specifies the storage policy of a Storage Domain.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deduplication_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies deduplication settings for a Storage Domain. | [optional] 
**compression_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies compression settings for a Storage Domain. | [optional] 
**deduplication_compression_delay_secs** | **int, none_type** | Specifies the time in seconds when deduplication and compression of the Storage Domain starts. | [optional] 
**erasure_coding_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the erasure coding parameters for a Storage Domain. | [optional] 
**encryption_type** | **str, none_type** | Specifies the encryption type for a Storage Domain. | [optional] 
**cloud_spill_vault_id** | **int, none_type** | Specifies the vault id assigned for cloud spill for a Storage Domain. | [optional] 
**num_disk_failures_tolerated** | **int, none_type** | Specifies the number of disk failures to tolerate for a Storage Domain. By default, this field is 1 for cluster with three or more nodes. If erasure coding is enabled, this field will be the same as numCodedStripes. | [optional] 
**num_node_failures_tolerated** | **int, none_type** | Specifies the number of node failures to tolerate for a Storage Domain. By default this field is replication factor minus 1 for replication chunk files and is the same as numCodedStripes for erasure coding chunk files. | [optional] 
**app_marker_detection_enabled** | **bool, none_type** | Specifies whether app marker detection is enabled. When enabled, app markers will be removed from data and put in separate chunks. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


