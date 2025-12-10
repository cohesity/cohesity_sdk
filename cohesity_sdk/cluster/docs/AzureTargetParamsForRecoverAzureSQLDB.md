# AzureTargetParamsForRecoverAzureSQLDB

Specifies the recovery target params for Azure SQL Database target config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverAzureSQLDBNewSourceConfig**](RecoverAzureSQLDBNewSourceConfig.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing target. | 
**restore_metadata** | **bool** | Specifies whether to perform external metadata restore or not. Default value is false. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.azure_target_params_for_recover_azure_sqldb import AzureTargetParamsForRecoverAzureSQLDB

# TODO update the JSON string below
json = "{}"
# create an instance of AzureTargetParamsForRecoverAzureSQLDB from a JSON string
azure_target_params_for_recover_azure_sqldb_instance = AzureTargetParamsForRecoverAzureSQLDB.from_json(json)
# print the JSON string representation of the object
print(AzureTargetParamsForRecoverAzureSQLDB.to_json())

# convert the object into a dict
azure_target_params_for_recover_azure_sqldb_dict = azure_target_params_for_recover_azure_sqldb_instance.to_dict()
# create an instance of AzureTargetParamsForRecoverAzureSQLDB from a dict
azure_target_params_for_recover_azure_sqldb_from_dict = AzureTargetParamsForRecoverAzureSQLDB.from_dict(azure_target_params_for_recover_azure_sqldb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


