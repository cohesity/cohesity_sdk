# RecoverIsilonNasVolumeParams

Specifies the parameters to recover Isilon NAS volumes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elastifile_target_params** | [**RecoverOtherNasToElastifileVolumeTargetParams**](RecoverOtherNasToElastifileVolumeTargetParams.md) |  | [optional] 
**flashblade_target_params** | [**RecoverOtherNasToFlashbladeVolumeTargetParams**](RecoverOtherNasToFlashbladeVolumeTargetParams.md) |  | [optional] 
**generic_nas_target_params** | [**RecoverOtherNasToGenericNasVolumeTargetParams**](RecoverOtherNasToGenericNasVolumeTargetParams.md) |  | [optional] 
**gpfs_target_params** | [**RecoverOtherNasToGpfsVolumeTargetParams**](RecoverOtherNasToGpfsVolumeTargetParams.md) |  | [optional] 
**isilon_target_params** | [**RecoverIsilonToIsilonVolumeTargetParams**](RecoverIsilonToIsilonVolumeTargetParams.md) |  | [optional] 
**netapp_target_params** | [**RecoverOtherNasToNetappVolumeTargetParams**](RecoverOtherNasToNetappVolumeTargetParams.md) |  | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 
**view_target_params** | [**RecoverNasVolumeToViewParams**](RecoverNasVolumeToViewParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.recover_isilon_nas_volume_params import RecoverIsilonNasVolumeParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverIsilonNasVolumeParams from a JSON string
recover_isilon_nas_volume_params_instance = RecoverIsilonNasVolumeParams.from_json(json)
# print the JSON string representation of the object
print(RecoverIsilonNasVolumeParams.to_json())

# convert the object into a dict
recover_isilon_nas_volume_params_dict = recover_isilon_nas_volume_params_instance.to_dict()
# create an instance of RecoverIsilonNasVolumeParams from a dict
recover_isilon_nas_volume_params_from_dict = RecoverIsilonNasVolumeParams.from_dict(recover_isilon_nas_volume_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


