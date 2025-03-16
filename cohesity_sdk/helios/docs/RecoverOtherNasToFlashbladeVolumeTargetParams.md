# RecoverOtherNasToFlashbladeVolumeTargetParams

Specifies the params of the Flashblade recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool** | Specifies whether to continue recovering other volumes if one of the volumes fails to recover. Default value is false. | [optional] 
**encryption_enabled** | **bool** | Specifies whether encryption should be enabled during recovery. | [optional] 
**filter_ip_config** | [**FilterIpConfig**](FilterIpConfig.md) |  | [optional] 
**overwrite_existing_file** | **bool** | Specifies whether to overwrite existing file/folder during recovery. | [optional] 
**parent_source** | [**RecoverOtherNasToElastifileFilesTargetParamsParentSource**](RecoverOtherNasToElastifileFilesTargetParamsParentSource.md) |  | [optional] 
**preserve_file_attributes** | **bool** | Specifies whether to preserve file/folder attributes during recovery. | [optional] 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 
**volume** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the id and name of the parent volume to recover to. This volume will be the target of the recovery. | 

## Example

```python
from cohesity_sdk.helios.models.recover_other_nas_to_flashblade_volume_target_params import RecoverOtherNasToFlashbladeVolumeTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverOtherNasToFlashbladeVolumeTargetParams from a JSON string
recover_other_nas_to_flashblade_volume_target_params_instance = RecoverOtherNasToFlashbladeVolumeTargetParams.from_json(json)
# print the JSON string representation of the object
print(RecoverOtherNasToFlashbladeVolumeTargetParams.to_json())

# convert the object into a dict
recover_other_nas_to_flashblade_volume_target_params_dict = recover_other_nas_to_flashblade_volume_target_params_instance.to_dict()
# create an instance of RecoverOtherNasToFlashbladeVolumeTargetParams from a dict
recover_other_nas_to_flashblade_volume_target_params_from_dict = RecoverOtherNasToFlashbladeVolumeTargetParams.from_dict(recover_other_nas_to_flashblade_volume_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


