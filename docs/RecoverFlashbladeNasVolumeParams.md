# RecoverFlashbladeNasVolumeParams

Specifies the parameters to recover Flashblade NAS volumes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elastifile_target_params** | [**RecoverOtherNasToElastifileVolumeTargetParams**](RecoverOtherNasToElastifileVolumeTargetParams.md) |  | [optional] 
**flashblade_target_params** | [**RecoverFlashbladeToFlashbladeVolumeTargetParams**](RecoverFlashbladeToFlashbladeVolumeTargetParams.md) |  | [optional] 
**generic_nas_target_params** | [**RecoverOtherNasToGenericNasVolumeTargetParams**](RecoverOtherNasToGenericNasVolumeTargetParams.md) |  | [optional] 
**gpfs_target_params** | [**RecoverOtherNasToGpfsVolumeTargetParams**](RecoverOtherNasToGpfsVolumeTargetParams.md) |  | [optional] 
**isilon_target_params** | [**RecoverOtherNasToIsilonVolumeTargetParams**](RecoverOtherNasToIsilonVolumeTargetParams.md) |  | [optional] 
**netapp_target_params** | [**RecoverOtherNasToNetappVolumeTargetParams**](RecoverOtherNasToNetappVolumeTargetParams.md) |  | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 
**view_target_params** | [**RecoverNasVolumeToViewParams**](RecoverNasVolumeToViewParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.recover_flashblade_nas_volume_params import RecoverFlashbladeNasVolumeParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverFlashbladeNasVolumeParams from a JSON string
recover_flashblade_nas_volume_params_instance = RecoverFlashbladeNasVolumeParams.from_json(json)
# print the JSON string representation of the object
print(RecoverFlashbladeNasVolumeParams.to_json())

# convert the object into a dict
recover_flashblade_nas_volume_params_dict = recover_flashblade_nas_volume_params_instance.to_dict()
# create an instance of RecoverFlashbladeNasVolumeParams from a dict
recover_flashblade_nas_volume_params_from_dict = RecoverFlashbladeNasVolumeParams.from_dict(recover_flashblade_nas_volume_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


