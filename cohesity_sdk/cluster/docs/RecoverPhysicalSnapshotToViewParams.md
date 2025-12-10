# RecoverPhysicalSnapshotToViewParams

Specifies the parameters to restore a snapshot to a new Cohesity view.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view_target_params** | [**ViewTargetParamsForRecoverPhysical**](ViewTargetParamsForRecoverPhysical.md) |  | 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_physical_snapshot_to_view_params import RecoverPhysicalSnapshotToViewParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverPhysicalSnapshotToViewParams from a JSON string
recover_physical_snapshot_to_view_params_instance = RecoverPhysicalSnapshotToViewParams.from_json(json)
# print the JSON string representation of the object
print(RecoverPhysicalSnapshotToViewParams.to_json())

# convert the object into a dict
recover_physical_snapshot_to_view_params_dict = recover_physical_snapshot_to_view_params_instance.to_dict()
# create an instance of RecoverPhysicalSnapshotToViewParams from a dict
recover_physical_snapshot_to_view_params_from_dict = RecoverPhysicalSnapshotToViewParams.from_dict(recover_physical_snapshot_to_view_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


