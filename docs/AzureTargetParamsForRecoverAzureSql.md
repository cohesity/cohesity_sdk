# AzureTargetParamsForRecoverAzureSql

Specifies the recovery target params for Azure SQL target config.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_to_new_source** | **bool, none_type** | Specifies the parameter whether the recovery should be performed to a new or an existing target. | 
**new_source_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the new destination Source configuration parameters where the Azure SQL instances will be recovered. This is mandatory if recoverToNewSource is set to true. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


