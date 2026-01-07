# RecoverGCPAlloyDBPostgreSQLParams

Specifies the parameters to recover GCP AlloyDB PostgreSQL database.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gcp_target_params** | [**GCPTargetParamsForRecoverGCPPostgreSQL**](GCPTargetParamsForRecoverGCPPostgreSQL.md) |  | 
**snapshots** | [**[RecoverGCPPostgreSQLSnapshotParams]**](RecoverGCPPostgreSQLSnapshotParams.md) | Specifies the details of the GCP AlloyDB PostgreSQL objects to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | defaults to "kGCP"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


