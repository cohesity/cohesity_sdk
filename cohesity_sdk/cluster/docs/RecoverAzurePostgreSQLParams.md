# RecoverAzurePostgreSQLParams

Specifies the parameters to recover Azure PostgreSQL.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshots** | [**[RecoverAzurePostgreSQLSnapshotParams], none_type**](RecoverAzurePostgreSQLSnapshotParams.md) | Specifies the details of the azure PostgreSQL objects to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | defaults to "kAzure"
**azure_target_params** | [**AzureTargetParamsForRecoverAzurePostgreSQL**](AzureTargetParamsForRecoverAzurePostgreSQL.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


