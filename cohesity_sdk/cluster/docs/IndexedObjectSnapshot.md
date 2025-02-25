# IndexedObjectSnapshot

Specifies a snapshot containing the indexed object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempts** | **int, none_type** | Specifies the number of runs have been executed before the run completed successfully. | [optional] 
**external_target_info** | [**ArchivalTargetSummaryInfo**](ArchivalTargetSummaryInfo.md) |  | [optional] 
**indexed_object_name** | **str, none_type** | Specifies the indexed object name. | [optional] 
**indexed_object_source_uuid** | **str, none_type** | Specifies the unique identifier from the source of the item associated with this particular snapshot. It can get changed between the snapshots and therefore will be required for recovery. | [optional] 
**inode_id** | **int, none_type** | Specifies the source inode number of the file being recovered. | [optional] [readonly] 
**last_modified_time_usecs** | **int, none_type** | Specifies the last time file was modified in unix timestamp. | [optional] 
**object_snapshotid** | **str, none_type** | Specifies snapshot id of the object containing this indexed object. | [optional] 
**protection_group_id** | **str, none_type** | Specifies the protection group id which contains this snapshot. | [optional] 
**protection_group_name** | **str, none_type** | Specifies the protection group name which contains this snapshot. | [optional] 
**run_type** | **str, none_type** | Specifies the type of protection run created this snapshot. | [optional] 
**size_bytes** | **int, none_type** | Specifies the indexed object size in bytes. | [optional] 
**snapshot_timestamp_usecs** | **int, none_type** | Specifies a unix timestamp when the object snapshot was taken in micro seconds. | [optional] 
**storage_domain_id** | **int, none_type** | Specifies the storage domain id containing this snapshot. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


