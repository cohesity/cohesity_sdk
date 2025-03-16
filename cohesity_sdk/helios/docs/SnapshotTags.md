# SnapshotTags

Snapshot and the tags associated with it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot** | [**Snapshot**](Snapshot.md) |  | 
**tags** | [**List[SnapshotTag]**](SnapshotTag.md) | This represents Tags associated with this snapshot. The tags included depend on the API this model is being used for. For AddSnapshotsTags api request parameters, it represents only the tags added to the snapshot by the API. For RemoveSnapshotsTags api request parameters, it represents only the tags removed from the snapshot by the API. For AddSnapshotsTags/GetSnapshotsTags/RemoveSnapshotsTags api response, it represents all tags associated with the snapshot.  | 

## Example

```python
from cohesity_sdk.helios.models.snapshot_tags import SnapshotTags

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotTags from a JSON string
snapshot_tags_instance = SnapshotTags.from_json(json)
# print the JSON string representation of the object
print(SnapshotTags.to_json())

# convert the object into a dict
snapshot_tags_dict = snapshot_tags_instance.to_dict()
# create an instance of SnapshotTags from a dict
snapshot_tags_from_dict = SnapshotTags.from_dict(snapshot_tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


