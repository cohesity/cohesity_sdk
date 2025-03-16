# SnapshotLabel

Specifies the snapshot label for incremental and full backup of Secondary Netapp volumes (Data-Protect Volumes).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_label** | **str** | Specifies the full snapshot label value | [optional] 
**incremental_label** | **str** | Specifies the incremental snapshot label value | [optional] 

## Example

```python
from cohesity_sdk.helios.models.snapshot_label import SnapshotLabel

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotLabel from a JSON string
snapshot_label_instance = SnapshotLabel.from_json(json)
# print the JSON string representation of the object
print(SnapshotLabel.to_json())

# convert the object into a dict
snapshot_label_dict = snapshot_label_instance.to_dict()
# create an instance of SnapshotLabel from a dict
snapshot_label_from_dict = SnapshotLabel.from_dict(snapshot_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


