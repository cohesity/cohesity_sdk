# RecoverElastifileNasVolumeParams

Specifies the parameters to recover Elastifile NAS volumes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elastifile_target_params** | [**RecoverElastifileToElastifileVolumeTargetParams**](RecoverElastifileToElastifileVolumeTargetParams.md) |  | [optional] 
**flashblade_target_params** | [**RecoverOtherNasToFlashbladeVolumeTargetParams**](RecoverOtherNasToFlashbladeVolumeTargetParams.md) |  | [optional] 
**generic_nas_target_params** | [**RecoverOtherNasToGenericNasVolumeTargetParams**](RecoverOtherNasToGenericNasVolumeTargetParams.md) |  | [optional] 
**gpfs_target_params** | [**RecoverOtherNasToGpfsVolumeTargetParams**](RecoverOtherNasToGpfsVolumeTargetParams.md) |  | [optional] 
**isilon_target_params** | [**RecoverOtherNasToIsilonVolumeTargetParams**](RecoverOtherNasToIsilonVolumeTargetParams.md) |  | [optional] 
**netapp_target_params** | [**RecoverOtherNasToNetappVolumeTargetParams**](RecoverOtherNasToNetappVolumeTargetParams.md) |  | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 
**view_target_params** | [**RecoverNasVolumeToViewParams**](RecoverNasVolumeToViewParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_elastifile_nas_volume_params import RecoverElastifileNasVolumeParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverElastifileNasVolumeParams from a JSON string
recover_elastifile_nas_volume_params_instance = RecoverElastifileNasVolumeParams.from_json(json)
# print the JSON string representation of the object
print(RecoverElastifileNasVolumeParams.to_json())

# convert the object into a dict
recover_elastifile_nas_volume_params_dict = recover_elastifile_nas_volume_params_instance.to_dict()
# create an instance of RecoverElastifileNasVolumeParams from a dict
recover_elastifile_nas_volume_params_from_dict = RecoverElastifileNasVolumeParams.from_dict(recover_elastifile_nas_volume_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


