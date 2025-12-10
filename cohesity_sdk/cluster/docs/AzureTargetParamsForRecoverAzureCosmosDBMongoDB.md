# AzureTargetParamsForRecoverAzureCosmosDBMongoDB

Specifies the recovery target params for Azure CosmosDB MongoDB target config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverAzureDbNewSourceConfig**](RecoverAzureDbNewSourceConfig.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing target. | 

## Example

```python
from cohesity_sdk.cluster.models.azure_target_params_for_recover_azure_cosmos_db_mongo_db import AzureTargetParamsForRecoverAzureCosmosDBMongoDB

# TODO update the JSON string below
json = "{}"
# create an instance of AzureTargetParamsForRecoverAzureCosmosDBMongoDB from a JSON string
azure_target_params_for_recover_azure_cosmos_db_mongo_db_instance = AzureTargetParamsForRecoverAzureCosmosDBMongoDB.from_json(json)
# print the JSON string representation of the object
print(AzureTargetParamsForRecoverAzureCosmosDBMongoDB.to_json())

# convert the object into a dict
azure_target_params_for_recover_azure_cosmos_db_mongo_db_dict = azure_target_params_for_recover_azure_cosmos_db_mongo_db_instance.to_dict()
# create an instance of AzureTargetParamsForRecoverAzureCosmosDBMongoDB from a dict
azure_target_params_for_recover_azure_cosmos_db_mongo_db_from_dict = AzureTargetParamsForRecoverAzureCosmosDBMongoDB.from_dict(azure_target_params_for_recover_azure_cosmos_db_mongo_db_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


