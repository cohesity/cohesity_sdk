# RecoverAzureTableAPIParams

Specifies the parameters to recover Azure Table API.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshots** | [**[RecoverAzureTableAPISnapshotParams], none_type**](RecoverAzureTableAPISnapshotParams.md) | Specifies the details of the azure table api objects to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | defaults to "kAzure"
**azure_target_params** | [**AzureTargetParamsForRecoverAzureTableAPI**](AzureTargetParamsForRecoverAzureTableAPI.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


