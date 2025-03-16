# MountHyperVVolumeParams

Specifies the parameters to mount volumes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hyperv_target_params** | [**HyperVTargetParamsForMountVolume**](HyperVTargetParamsForMountVolume.md) |  | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.mount_hyper_v_volume_params import MountHyperVVolumeParams

# TODO update the JSON string below
json = "{}"
# create an instance of MountHyperVVolumeParams from a JSON string
mount_hyper_v_volume_params_instance = MountHyperVVolumeParams.from_json(json)
# print the JSON string representation of the object
print(MountHyperVVolumeParams.to_json())

# convert the object into a dict
mount_hyper_v_volume_params_dict = mount_hyper_v_volume_params_instance.to_dict()
# create an instance of MountHyperVVolumeParams from a dict
mount_hyper_v_volume_params_from_dict = MountHyperVVolumeParams.from_dict(mount_hyper_v_volume_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


