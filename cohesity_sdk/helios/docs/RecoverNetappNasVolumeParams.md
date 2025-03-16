# RecoverNetappNasVolumeParams

Specifies the parameters to recover Netapp NAS volumes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elastifile_target_params** | [**RecoverOtherNasToElastifileVolumeTargetParams**](RecoverOtherNasToElastifileVolumeTargetParams.md) | Specifies the params for an Elastifile recovery target. | [optional] 
**flashblade_target_params** | [**RecoverOtherNasToFlashbladeVolumeTargetParams**](RecoverOtherNasToFlashbladeVolumeTargetParams.md) | Specifies the params for a Flashblade recovery target. | [optional] 
**generic_nas_target_params** | [**RecoverOtherNasToGenericNasVolumeTargetParams**](RecoverOtherNasToGenericNasVolumeTargetParams.md) | Specifies the params for a generic NAS recovery target. | [optional] 
**gpfs_target_params** | [**RecoverOtherNasToGpfsVolumeTargetParams**](RecoverOtherNasToGpfsVolumeTargetParams.md) | Specifies the params for a GPFS recovery target. | [optional] 
**is_from_source_initiated_protection** | **bool** | Specifies if the snapshot trying to recover is from a source initiated protection. | [optional] 
**isilon_target_params** | [**RecoverOtherNasToIsilonVolumeTargetParams**](RecoverOtherNasToIsilonVolumeTargetParams.md) | Specifies the params for an Isilon recovery target. | [optional] 
**netapp_target_params** | [**RecoverNetappToNetappVolumeTargetParams**](RecoverNetappToNetappVolumeTargetParams.md) | Specifies the params for a Netapp recovery target. | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 
**view_target_params** | [**RecoverNasVolumeToViewParams**](RecoverNasVolumeToViewParams.md) | Specifies the params for a Cohesity view recovery target. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.recover_netapp_nas_volume_params import RecoverNetappNasVolumeParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverNetappNasVolumeParams from a JSON string
recover_netapp_nas_volume_params_instance = RecoverNetappNasVolumeParams.from_json(json)
# print the JSON string representation of the object
print(RecoverNetappNasVolumeParams.to_json())

# convert the object into a dict
recover_netapp_nas_volume_params_dict = recover_netapp_nas_volume_params_instance.to_dict()
# create an instance of RecoverNetappNasVolumeParams from a dict
recover_netapp_nas_volume_params_from_dict = RecoverNetappNasVolumeParams.from_dict(recover_netapp_nas_volume_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


