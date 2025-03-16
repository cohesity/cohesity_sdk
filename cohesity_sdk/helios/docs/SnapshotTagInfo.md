# SnapshotTagInfo

Specifies the snapshot tag info for an object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_id** | **str** | Specifies Id of tag applied to the object. | 
**run_ids** | **List[str]** | Specifies runs the tags are applied to. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.snapshot_tag_info import SnapshotTagInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotTagInfo from a JSON string
snapshot_tag_info_instance = SnapshotTagInfo.from_json(json)
# print the JSON string representation of the object
print(SnapshotTagInfo.to_json())

# convert the object into a dict
snapshot_tag_info_dict = snapshot_tag_info_instance.to_dict()
# create an instance of SnapshotTagInfo from a dict
snapshot_tag_info_from_dict = SnapshotTagInfo.from_dict(snapshot_tag_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


