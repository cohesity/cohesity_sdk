# FullSnapshotInfo

Specifies the info regarding how to restore to a particular full or incremental snapshot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**restore_info** | [**RestoreInfo**](RestoreInfo.md) |  | [optional] 
**targets_configuration** | [**List[TargetsConfiguration]**](TargetsConfiguration.md) | Specifies the location holding snapshot copies that may be used for restore. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.full_snapshot_info import FullSnapshotInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FullSnapshotInfo from a JSON string
full_snapshot_info_instance = FullSnapshotInfo.from_json(json)
# print the JSON string representation of the object
print(FullSnapshotInfo.to_json())

# convert the object into a dict
full_snapshot_info_dict = full_snapshot_info_instance.to_dict()
# create an instance of FullSnapshotInfo from a dict
full_snapshot_info_from_dict = FullSnapshotInfo.from_dict(full_snapshot_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


