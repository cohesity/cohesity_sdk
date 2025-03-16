# ContinuousSnapshotParams

Specifies the source snapshots to be taken even if there is a pending run in a protection group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** | Specifies whether source snapshots should be taken even if there is a pending run. | 
**max_allowed_snapshots** | **int** | Specifies the maximum number of source snapshots allowed for a given object in a protection group. This is only applicable if isContinuousSnapshottingEnabled is set to true. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.continuous_snapshot_params import ContinuousSnapshotParams

# TODO update the JSON string below
json = "{}"
# create an instance of ContinuousSnapshotParams from a JSON string
continuous_snapshot_params_instance = ContinuousSnapshotParams.from_json(json)
# print the JSON string representation of the object
print(ContinuousSnapshotParams.to_json())

# convert the object into a dict
continuous_snapshot_params_dict = continuous_snapshot_params_instance.to_dict()
# create an instance of ContinuousSnapshotParams from a dict
continuous_snapshot_params_from_dict = ContinuousSnapshotParams.from_dict(continuous_snapshot_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


