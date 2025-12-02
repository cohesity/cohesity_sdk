# HyperVTargetParamsForRecoverFileAndFolder

Specifies the parameters for a HyperV recovery target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_to_original_target** | **bool, none_type** | Specifies whether to recover to the original target. If true, originalTargetConfig must be specified. If false, newTargetConfig must be specified. | 
**continue_on_error** | **bool, none_type** | Specifies whether to continue recovering other files if one of files or folders failed to recover. Default value is false. | [optional] 
**new_target_config** | [**HyperVRecoverFilesNewTargetConfig**](HyperVRecoverFilesNewTargetConfig.md) |  | [optional] 
**original_target_config** | [**HyperVRecoverFilesOriginalTargetConfig**](HyperVRecoverFilesOriginalTargetConfig.md) |  | [optional] 
**overwrite_existing** | **bool, none_type** | Specifies whether to override the existing files. Default is true. | [optional] 
**preserve_attributes** | **bool, none_type** | Specifies whether to preserve original attributes. Default is true. | [optional] 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


