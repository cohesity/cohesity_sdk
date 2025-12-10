# AzureTargetParamsForRecoverAzureTableStorage

Specifies the recovery target params for Azure Table Storage target config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverAzureDbNewSourceConfig**](RecoverAzureDbNewSourceConfig.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing target. | 
**restore_metadata** | **bool** | Specifies whether to perform external metadata restore or not. Default value is false. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.azure_target_params_for_recover_azure_table_storage import AzureTargetParamsForRecoverAzureTableStorage

# TODO update the JSON string below
json = "{}"
# create an instance of AzureTargetParamsForRecoverAzureTableStorage from a JSON string
azure_target_params_for_recover_azure_table_storage_instance = AzureTargetParamsForRecoverAzureTableStorage.from_json(json)
# print the JSON string representation of the object
print(AzureTargetParamsForRecoverAzureTableStorage.to_json())

# convert the object into a dict
azure_target_params_for_recover_azure_table_storage_dict = azure_target_params_for_recover_azure_table_storage_instance.to_dict()
# create an instance of AzureTargetParamsForRecoverAzureTableStorage from a dict
azure_target_params_for_recover_azure_table_storage_from_dict = AzureTargetParamsForRecoverAzureTableStorage.from_dict(azure_target_params_for_recover_azure_table_storage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


