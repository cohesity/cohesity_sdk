# AzureTargetParamsForRecoverAzurePostgreSQL

Specifies the recovery target params for Azure PostgreSQL target config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverAzureDbNewSourceConfig**](RecoverAzureDbNewSourceConfig.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing target. | 
**restore_metadata** | **bool** | Specifies whether to perform external metadata restore or not. Default value is false. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.azure_target_params_for_recover_azure_postgre_sql import AzureTargetParamsForRecoverAzurePostgreSQL

# TODO update the JSON string below
json = "{}"
# create an instance of AzureTargetParamsForRecoverAzurePostgreSQL from a JSON string
azure_target_params_for_recover_azure_postgre_sql_instance = AzureTargetParamsForRecoverAzurePostgreSQL.from_json(json)
# print the JSON string representation of the object
print(AzureTargetParamsForRecoverAzurePostgreSQL.to_json())

# convert the object into a dict
azure_target_params_for_recover_azure_postgre_sql_dict = azure_target_params_for_recover_azure_postgre_sql_instance.to_dict()
# create an instance of AzureTargetParamsForRecoverAzurePostgreSQL from a dict
azure_target_params_for_recover_azure_postgre_sql_from_dict = AzureTargetParamsForRecoverAzurePostgreSQL.from_dict(azure_target_params_for_recover_azure_postgre_sql_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


