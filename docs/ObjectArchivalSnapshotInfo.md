# ObjectArchivalSnapshotInfo

Specifies the Archival snapshot information for the object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_task_id** | **str** | Specifies the archival task id. This is a protection group UID which only applies when archival type is &#39;Tape&#39;. | [optional] 
**ownership_context** | **str** | Specifies the ownership context for the target. | [optional] 
**target_id** | **int** | Specifies the archival target ID. | [optional] 
**target_name** | **str** | Specifies the archival target name. | [optional] 
**target_type** | **str** | Specifies the archival target type. | [optional] 
**tier_settings** | [**ArchivalTargetTierInfo**](ArchivalTargetTierInfo.md) |  | [optional] 
**usage_type** | **str** | Specifies the usage type for the target. | [optional] 
**logical_size_bytes** | **int** | Specifies the logical size of this snapshot in bytes. | [optional] 
**snapshot_id** | **str** | Specifies the id of the archival snapshot for the object. | [optional] 

## Example

```python
from cohesity_sdk.models.object_archival_snapshot_info import ObjectArchivalSnapshotInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectArchivalSnapshotInfo from a JSON string
object_archival_snapshot_info_instance = ObjectArchivalSnapshotInfo.from_json(json)
# print the JSON string representation of the object
print(ObjectArchivalSnapshotInfo.to_json())

# convert the object into a dict
object_archival_snapshot_info_dict = object_archival_snapshot_info_instance.to_dict()
# create an instance of ObjectArchivalSnapshotInfo from a dict
object_archival_snapshot_info_from_dict = ObjectArchivalSnapshotInfo.from_dict(object_archival_snapshot_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


