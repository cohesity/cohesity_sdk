# RecoverAzureCosmosDBMongoDBParams

Specifies the parameters to recover Azure CosmosDB MongoDB.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_target_params** | [**AzureTargetParamsForRecoverAzureCosmosDBMongoDB**](AzureTargetParamsForRecoverAzureCosmosDBMongoDB.md) |  | [optional] 
**snapshots** | [**List[RecoverAzureCosmosDBMongoDBSnapshotParams]**](RecoverAzureCosmosDBMongoDBSnapshotParams.md) | Specifies the details of the azure cosmosdb mongodb objects to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_azure_cosmos_db_mongo_db_params import RecoverAzureCosmosDBMongoDBParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAzureCosmosDBMongoDBParams from a JSON string
recover_azure_cosmos_db_mongo_db_params_instance = RecoverAzureCosmosDBMongoDBParams.from_json(json)
# print the JSON string representation of the object
print(RecoverAzureCosmosDBMongoDBParams.to_json())

# convert the object into a dict
recover_azure_cosmos_db_mongo_db_params_dict = recover_azure_cosmos_db_mongo_db_params_instance.to_dict()
# create an instance of RecoverAzureCosmosDBMongoDBParams from a dict
recover_azure_cosmos_db_mongo_db_params_from_dict = RecoverAzureCosmosDBMongoDBParams.from_dict(recover_azure_cosmos_db_mongo_db_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


