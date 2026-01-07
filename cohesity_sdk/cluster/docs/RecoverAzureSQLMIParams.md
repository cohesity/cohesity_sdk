# RecoverAzureSQLMIParams

Specifies the parameters to recover Azure SQL Managed Instance.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshots** | [**[RecoverAzureSQLMISnapshotParams], none_type**](RecoverAzureSQLMISnapshotParams.md) | Specifies the details of the azure SQL Managed Instance objects to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | defaults to "kAzure"
**azure_target_params** | [**AzureTargetParamsForRecoverAzureSQLMI**](AzureTargetParamsForRecoverAzureSQLMI.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


