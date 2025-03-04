# ObjectLocalSnapshotInfo

Specifies the Local snapshot information for the object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logical_size_bytes** | **int** | Specifies the logical size of this snapshot in bytes. | [optional] 
**snapshot_id** | **str** | Specifies the id of the local snapshot for the object. | [optional] 

## Example

```python
from cohesity_sdk.models.object_local_snapshot_info import ObjectLocalSnapshotInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectLocalSnapshotInfo from a JSON string
object_local_snapshot_info_instance = ObjectLocalSnapshotInfo.from_json(json)
# print the JSON string representation of the object
print(ObjectLocalSnapshotInfo.to_json())

# convert the object into a dict
object_local_snapshot_info_dict = object_local_snapshot_info_instance.to_dict()
# create an instance of ObjectLocalSnapshotInfo from a dict
object_local_snapshot_info_from_dict = ObjectLocalSnapshotInfo.from_dict(object_local_snapshot_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


