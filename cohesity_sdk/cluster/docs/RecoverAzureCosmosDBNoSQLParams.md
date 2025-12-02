# RecoverAzureCosmosDBNoSQLParams

Specifies the parameters to recover Azure CosmosDB NoSQL.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshots** | [**[RecoverAzureCosmosDBNoSQLSnapshotParams], none_type**](RecoverAzureCosmosDBNoSQLSnapshotParams.md) | Specifies the details of the azure cosmosdb nosql objects to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | defaults to "kAzure"
**azure_target_params** | [**AzureTargetParamsForRecoverAzureCosmosDBNoSQL**](AzureTargetParamsForRecoverAzureCosmosDBNoSQL.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


