# AzureTargetParamsForRecoverAzureSql

Specifies the recovery target params for Azure SQL target config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverAzureSqlNewSourceConfig**](RecoverAzureSqlNewSourceConfig.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing target. | 

## Example

```python
from cohesity_sdk.cluster.models.azure_target_params_for_recover_azure_sql import AzureTargetParamsForRecoverAzureSql

# TODO update the JSON string below
json = "{}"
# create an instance of AzureTargetParamsForRecoverAzureSql from a JSON string
azure_target_params_for_recover_azure_sql_instance = AzureTargetParamsForRecoverAzureSql.from_json(json)
# print the JSON string representation of the object
print(AzureTargetParamsForRecoverAzureSql.to_json())

# convert the object into a dict
azure_target_params_for_recover_azure_sql_dict = azure_target_params_for_recover_azure_sql_instance.to_dict()
# create an instance of AzureTargetParamsForRecoverAzureSql from a dict
azure_target_params_for_recover_azure_sql_from_dict = AzureTargetParamsForRecoverAzureSql.from_dict(azure_target_params_for_recover_azure_sql_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


