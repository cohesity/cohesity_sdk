# IndexedObjectSnapshot

Specifies a snapshot containing the indexed object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempts** | **int** | Specifies the number of runs have been executed before the run completed successfully. | [optional] 
**external_target_info** | [**ArchivalTargetSummaryInfo**](ArchivalTargetSummaryInfo.md) |  | [optional] 
**indexed_object_name** | **str** | Specifies the indexed object name. | [optional] 
**indexed_object_source_uuid** | **str** | Specifies the unique identifier from the source of the item associated with this particular snapshot. It can get changed between the snapshots and therefore will be required for recovery. | [optional] 
**inode_id** | **int** | Specifies the source inode number of the file being recovered. | [optional] [readonly] 
**last_modified_time_usecs** | **int** | Specifies the last time file was modified in unix timestamp. | [optional] 
**object_snapshotid** | **str** | Specifies snapshot id of the object containing this indexed object. | [optional] 
**protection_group_id** | **str** | Specifies the protection group id which contains this snapshot. | [optional] 
**protection_group_name** | **str** | Specifies the protection group name which contains this snapshot. | [optional] 
**run_type** | **str** | Specifies the type of protection run created this snapshot. | [optional] 
**size_bytes** | **int** | Specifies the indexed object size in bytes. | [optional] 
**snapshot_timestamp_usecs** | **int** | Specifies a unix timestamp when the object snapshot was taken in micro seconds. | [optional] 
**storage_domain_id** | **int** | Specifies the storage domain id containing this snapshot. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.indexed_object_snapshot import IndexedObjectSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of IndexedObjectSnapshot from a JSON string
indexed_object_snapshot_instance = IndexedObjectSnapshot.from_json(json)
# print the JSON string representation of the object
print(IndexedObjectSnapshot.to_json())

# convert the object into a dict
indexed_object_snapshot_dict = indexed_object_snapshot_instance.to_dict()
# create an instance of IndexedObjectSnapshot from a dict
indexed_object_snapshot_from_dict = IndexedObjectSnapshot.from_dict(indexed_object_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


