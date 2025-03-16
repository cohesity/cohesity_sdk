# RecoverGenericNasNasVolumeParams

Specifies the parameters to recover Generic NAS volumes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elastifile_target_params** | [**RecoverOtherNasToElastifileVolumeTargetParams**](RecoverOtherNasToElastifileVolumeTargetParams.md) | Specifies the params for a Elastifile recovery target. | [optional] 
**flashblade_target_params** | [**RecoverOtherNasToFlashbladeVolumeTargetParams**](RecoverOtherNasToFlashbladeVolumeTargetParams.md) | Specifies the params for a Flashblade recovery target. | [optional] 
**generic_nas_target_params** | [**RecoverGenericNasToGenericNasVolumeTargetParams**](RecoverGenericNasToGenericNasVolumeTargetParams.md) | Specifies the params for a Generic NAS recovery target. | [optional] 
**gpfs_target_params** | [**RecoverOtherNasToGpfsVolumeTargetParams**](RecoverOtherNasToGpfsVolumeTargetParams.md) | Specifies the params for a GPFS recovery target. | [optional] 
**isilon_target_params** | [**RecoverOtherNasToIsilonVolumeTargetParams**](RecoverOtherNasToIsilonVolumeTargetParams.md) | Specifies the params for an Isilon recovery target. | [optional] 
**netapp_target_params** | [**RecoverOtherNasToNetappVolumeTargetParams**](RecoverOtherNasToNetappVolumeTargetParams.md) | Specifies the params for an Netapp recovery target. | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 
**view_target_params** | [**RecoverNasVolumeToViewParams**](RecoverNasVolumeToViewParams.md) | Specifies the params for a Cohesity view recovery target. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.recover_generic_nas_nas_volume_params import RecoverGenericNasNasVolumeParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverGenericNasNasVolumeParams from a JSON string
recover_generic_nas_nas_volume_params_instance = RecoverGenericNasNasVolumeParams.from_json(json)
# print the JSON string representation of the object
print(RecoverGenericNasNasVolumeParams.to_json())

# convert the object into a dict
recover_generic_nas_nas_volume_params_dict = recover_generic_nas_nas_volume_params_instance.to_dict()
# create an instance of RecoverGenericNasNasVolumeParams from a dict
recover_generic_nas_nas_volume_params_from_dict = RecoverGenericNasNasVolumeParams.from_dict(recover_generic_nas_nas_volume_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


