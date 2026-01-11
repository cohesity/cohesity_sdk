# RecoverAzureCosmosDBMongoDBParams

Specifies the parameters to recover Azure CosmosDB MongoDB.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshots** | [**[RecoverAzureCosmosDBMongoDBSnapshotParams], none_type**](RecoverAzureCosmosDBMongoDBSnapshotParams.md) | Specifies the details of the azure cosmosdb mongodb objects to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | defaults to "kAzure"
**azure_target_params** | [**AzureTargetParamsForRecoverAzureCosmosDBMongoDB**](AzureTargetParamsForRecoverAzureCosmosDBMongoDB.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


