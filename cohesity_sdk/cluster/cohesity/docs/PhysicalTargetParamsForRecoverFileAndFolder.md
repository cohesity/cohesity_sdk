# PhysicalTargetParamsForRecoverFileAndFolder

Specifies the parameters for a Physical recovery target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_target** | [**RecoverTarget**](RecoverTarget.md) |  | 
**alternate_restore_directory** | **str, none_type** | Specifies the directory path where restore should happen if restore_to_original_paths is set to false. | [optional] 
**continue_on_error** | **bool, none_type** | Specifies whether to continue recovering other volumes if one of the volumes fails to recover. Default value is false. | [optional] 
**mount_credentials** | [**MountUserCreds**](MountUserCreds.md) |  | [optional] 
**overwrite_existing** | **bool, none_type** | Specifies whether to overwrite existing file/folder during recovery. | [optional] 
**preserve_acls** | **bool, none_type** | Whether to preserve the ACLs of the original file. | [optional] 
**preserve_attributes** | **bool, none_type** | Specifies whether to preserve file/folder attributes during recovery. | [optional] 
**preserve_timestamps** | **bool, none_type** | Whether to preserve the original time stamps. | [optional] 
**restore_entity_type** | **str, none_type** | Specifies the restore type (restore everything or ACLs only) when restoring or downloading files or folders from a Physical file based or block based backup snapshot. | [optional] 
**restore_exclusion_param** | **[str], none_type** | Specifies list of exclusions that needs to be applicable for the current file level restores. Applicable only for file level restores. | [optional] 
**restore_to_original_paths** | **bool, none_type** | If this is true, then files will be restored to original paths. | [optional] 
**save_success_files** | **bool, none_type** | Specifies whether to save success files or not. Default value is false | [optional] 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


