# MountPhysicalVolumeParams

Specifies the parameters to Mount Physical Volumes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**physical_target_params** | [**PhysicalTargetParamsForMountVolume**](PhysicalTargetParamsForMountVolume.md) | Specifies the params for recovering to a physical target. | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.helios.models.mount_physical_volume_params import MountPhysicalVolumeParams

# TODO update the JSON string below
json = "{}"
# create an instance of MountPhysicalVolumeParams from a JSON string
mount_physical_volume_params_instance = MountPhysicalVolumeParams.from_json(json)
# print the JSON string representation of the object
print(MountPhysicalVolumeParams.to_json())

# convert the object into a dict
mount_physical_volume_params_dict = mount_physical_volume_params_instance.to_dict()
# create an instance of MountPhysicalVolumeParams from a dict
mount_physical_volume_params_from_dict = MountPhysicalVolumeParams.from_dict(mount_physical_volume_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


