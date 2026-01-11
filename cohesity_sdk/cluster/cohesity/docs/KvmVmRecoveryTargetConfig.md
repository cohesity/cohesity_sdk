# KvmVmRecoveryTargetConfig

Specifies the target object parameters to recover KVM vms.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing Source Target. | 
**new_source_config** | [**RecoverKvmVmNewSourceConfig**](RecoverKvmVmNewSourceConfig.md) |  | [optional] 
**original_source_config** | [**RecoverKvmVmOriginalSourceConfig**](RecoverKvmVmOriginalSourceConfig.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


