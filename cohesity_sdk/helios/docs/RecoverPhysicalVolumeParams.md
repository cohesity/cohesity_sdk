# RecoverPhysicalVolumeParams

Specifies the parameters to recover Physical Volumes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**physical_target_params** | [**PhysicalTargetParamsForRecoverVolume**](PhysicalTargetParamsForRecoverVolume.md) | Specifies the params for recovering to a physical target. | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.helios.models.recover_physical_volume_params import RecoverPhysicalVolumeParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverPhysicalVolumeParams from a JSON string
recover_physical_volume_params_instance = RecoverPhysicalVolumeParams.from_json(json)
# print the JSON string representation of the object
print(RecoverPhysicalVolumeParams.to_json())

# convert the object into a dict
recover_physical_volume_params_dict = recover_physical_volume_params_instance.to_dict()
# create an instance of RecoverPhysicalVolumeParams from a dict
recover_physical_volume_params_from_dict = RecoverPhysicalVolumeParams.from_dict(recover_physical_volume_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


