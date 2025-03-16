# RecoverOtherNasToGpfsVolumeTargetParams

Specifies the params of the GPFS recovery target.

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
from cohesity_sdk.helios.models.recover_other_nas_to_gpfs_volume_target_params import RecoverOtherNasToGpfsVolumeTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverOtherNasToGpfsVolumeTargetParams from a JSON string
recover_other_nas_to_gpfs_volume_target_params_instance = RecoverOtherNasToGpfsVolumeTargetParams.from_json(json)
# print the JSON string representation of the object
print(RecoverOtherNasToGpfsVolumeTargetParams.to_json())

# convert the object into a dict
recover_other_nas_to_gpfs_volume_target_params_dict = recover_other_nas_to_gpfs_volume_target_params_instance.to_dict()
# create an instance of RecoverOtherNasToGpfsVolumeTargetParams from a dict
recover_other_nas_to_gpfs_volume_target_params_from_dict = RecoverOtherNasToGpfsVolumeTargetParams.from_dict(recover_other_nas_to_gpfs_volume_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


