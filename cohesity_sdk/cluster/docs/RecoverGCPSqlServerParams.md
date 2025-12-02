# RecoverGCPSqlServerParams

Specifies the parameters to recover GCP SQL Server database.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gcp_target_params** | [**GCPTargetParamsForRecoverGCPSqlServer**](GCPTargetParamsForRecoverGCPSqlServer.md) |  | 
**snapshots** | [**[RecoverGCPSqlServerSnapshotParams]**](RecoverGCPSqlServerSnapshotParams.md) | Specifies the details of the gcp sql server objects to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | defaults to "kGCP"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


