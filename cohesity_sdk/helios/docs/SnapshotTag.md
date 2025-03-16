# SnapshotTag

Snapshot tag specified by its type id and label.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Type id of this tag. | [optional] 
**label** | **str** | Label of this tag. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.snapshot_tag import SnapshotTag

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotTag from a JSON string
snapshot_tag_instance = SnapshotTag.from_json(json)
# print the JSON string representation of the object
print(SnapshotTag.to_json())

# convert the object into a dict
snapshot_tag_dict = snapshot_tag_instance.to_dict()
# create an instance of SnapshotTag from a dict
snapshot_tag_from_dict = SnapshotTag.from_dict(snapshot_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


