# AzureTargetParamsForRecoverAzureSQLMI

Specifies the recovery target params for Azure SQL Managed Instance target config.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_to_new_source** | **bool, none_type** | Specifies the parameter whether the recovery should be performed to a new or an existing target. | 
**new_source_config** | [**RecoverAzureSQLMINewSourceConfig**](RecoverAzureSQLMINewSourceConfig.md) |  | [optional] 
**restore_metadata** | **bool, none_type** | Specifies whether to perform external metadata restore or not. Default value is false. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


