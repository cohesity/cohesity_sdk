# AzureTargetParamsForRecoverFileAndFolder

Specifies the parameters for an Azure files and folders recovery target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_to_original_target** | **bool, none_type** | Specifies whether to recover to the original target. If true, originalTargetConfig must be specified. If false, newTargetConfig must be specified. | 
**continue_on_error** | **bool, none_type** | Specifies whether to continue recovering other files if one of the objects encounters an error. Default is false. | [optional] 
**new_target_config** | [**AzureRecoverFilesNewTargetConfig**](AzureRecoverFilesNewTargetConfig.md) |  | [optional] 
**original_target_config** | [**AzureRecoverFilesOriginalTargetConfig**](AzureRecoverFilesOriginalTargetConfig.md) |  | [optional] 
**overwrite_existing** | **bool, none_type** | Specifies whether to overwrite the existing files. Default is true. | [optional] 
**preserve_attributes** | **bool, none_type** | Specifies whether to preserve original file/folder attributes. Default is true. | [optional] 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


