# PhysicalTargetParamsForRecoverFileAndFolder

Specifies the parameters for a Physical recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_restore_directory** | **str** | Specifies the directory path where restore should happen if restore_to_original_paths is set to false. | [optional] 
**continue_on_error** | **bool** | Specifies whether to continue recovering other volumes if one of the volumes fails to recover. Default value is false. | [optional] 
**overwrite_existing** | **bool** | Specifies whether to overwrite existing file/folder during recovery. | [optional] 
**preserve_acls** | **bool** | Whether to preserve the ACLs of the original file. | [optional] 
**preserve_attributes** | **bool** | Specifies whether to preserve file/folder attributes during recovery. | [optional] 
**preserve_timestamps** | **bool** | Whether to preserve the original time stamps. | [optional] 
**recover_target** | [**RecoverTarget**](RecoverTarget.md) |  | 
**restore_entity_type** | **str** | Specifies the restore type (restore everything or ACLs only) when restoring or downloading files or folders from a Physical file based or block based backup snapshot. | [optional] 
**restore_to_original_paths** | **bool** | If this is true, then files will be restored to original paths. | [optional] 
**save_success_files** | **bool** | Specifies whether to save success files or not. Default value is false | [optional] 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.physical_target_params_for_recover_file_and_folder import PhysicalTargetParamsForRecoverFileAndFolder

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalTargetParamsForRecoverFileAndFolder from a JSON string
physical_target_params_for_recover_file_and_folder_instance = PhysicalTargetParamsForRecoverFileAndFolder.from_json(json)
# print the JSON string representation of the object
print(PhysicalTargetParamsForRecoverFileAndFolder.to_json())

# convert the object into a dict
physical_target_params_for_recover_file_and_folder_dict = physical_target_params_for_recover_file_and_folder_instance.to_dict()
# create an instance of PhysicalTargetParamsForRecoverFileAndFolder from a dict
physical_target_params_for_recover_file_and_folder_from_dict = PhysicalTargetParamsForRecoverFileAndFolder.from_dict(physical_target_params_for_recover_file_and_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


