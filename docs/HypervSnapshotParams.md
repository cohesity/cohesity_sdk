# HypervSnapshotParams

Specifies parameters of HyperV type snapshots.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protection_type** | **str** | Specifies the protection type of HyperV snapshots. | [optional] 

## Example

```python
from cohesity_sdk.models.hyperv_snapshot_params import HypervSnapshotParams

# TODO update the JSON string below
json = "{}"
# create an instance of HypervSnapshotParams from a JSON string
hyperv_snapshot_params_instance = HypervSnapshotParams.from_json(json)
# print the JSON string representation of the object
print(HypervSnapshotParams.to_json())

# convert the object into a dict
hyperv_snapshot_params_dict = hyperv_snapshot_params_instance.to_dict()
# create an instance of HypervSnapshotParams from a dict
hyperv_snapshot_params_from_dict = HypervSnapshotParams.from_dict(hyperv_snapshot_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


