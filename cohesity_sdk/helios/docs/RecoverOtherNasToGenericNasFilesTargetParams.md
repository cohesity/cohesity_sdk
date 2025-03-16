# RecoverOtherNasToGenericNasFilesTargetParams

Specifies the params of the Generic Nas recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_path** | **str** | Specifies the path location to recover files to. | 
**continue_on_error** | **bool** | Specifies whether to continue recovering other files if one of the files fails to recover. Default value is false. | [optional] 
**encryption_enabled** | **bool** | Specifies whether encryption should be enabled during recovery. | [optional] 
**overwrite_existing_file** | **bool** | Specifies whether to overwrite existing file/folder during recovery. | [optional] 
**parent_source** | [**RecoverOtherNasToElastifileFilesTargetParamsParentSource**](RecoverOtherNasToElastifileFilesTargetParamsParentSource.md) |  | [optional] 
**preserve_file_attributes** | **bool** | Specifies whether to preserve file/folder attributes during recovery. | [optional] 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 
**volume** | [**RecoverTarget**](RecoverTarget.md) | Specifies the id and name of the parent NAS to recover to. This volume will be the target of the recovery. | 

## Example

```python
from cohesity_sdk.helios.models.recover_other_nas_to_generic_nas_files_target_params import RecoverOtherNasToGenericNasFilesTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverOtherNasToGenericNasFilesTargetParams from a JSON string
recover_other_nas_to_generic_nas_files_target_params_instance = RecoverOtherNasToGenericNasFilesTargetParams.from_json(json)
# print the JSON string representation of the object
print(RecoverOtherNasToGenericNasFilesTargetParams.to_json())

# convert the object into a dict
recover_other_nas_to_generic_nas_files_target_params_dict = recover_other_nas_to_generic_nas_files_target_params_instance.to_dict()
# create an instance of RecoverOtherNasToGenericNasFilesTargetParams from a dict
recover_other_nas_to_generic_nas_files_target_params_from_dict = RecoverOtherNasToGenericNasFilesTargetParams.from_dict(recover_other_nas_to_generic_nas_files_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


