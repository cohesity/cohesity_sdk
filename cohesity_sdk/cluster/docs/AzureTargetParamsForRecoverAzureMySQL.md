# AzureTargetParamsForRecoverAzureMySQL

Specifies the recovery target params for Azure MySQL target config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverAzureDbNewSourceConfig**](RecoverAzureDbNewSourceConfig.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing target. | 
**restore_metadata** | **bool** | Specifies whether to perform external metadata restore or not. Default value is false. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.azure_target_params_for_recover_azure_my_sql import AzureTargetParamsForRecoverAzureMySQL

# TODO update the JSON string below
json = "{}"
# create an instance of AzureTargetParamsForRecoverAzureMySQL from a JSON string
azure_target_params_for_recover_azure_my_sql_instance = AzureTargetParamsForRecoverAzureMySQL.from_json(json)
# print the JSON string representation of the object
print(AzureTargetParamsForRecoverAzureMySQL.to_json())

# convert the object into a dict
azure_target_params_for_recover_azure_my_sql_dict = azure_target_params_for_recover_azure_my_sql_instance.to_dict()
# create an instance of AzureTargetParamsForRecoverAzureMySQL from a dict
azure_target_params_for_recover_azure_my_sql_from_dict = AzureTargetParamsForRecoverAzureMySQL.from_dict(azure_target_params_for_recover_azure_my_sql_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


