# RecoverGcpParams

Specifies the recovery options specific to GCP environment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 
**download_file_and_folder_params** | [**CommonDownloadFileAndFolderParams**](CommonDownloadFileAndFolderParams.md) |  | [optional] 
**gcp_alloy_db_postgre_sql_params** | [**RecoverGCPAlloyDBPostgreSQLParams**](RecoverGCPAlloyDBPostgreSQLParams.md) |  | [optional] 
**gcp_big_query_params** | [**RecoverGCPBigQueryParams**](RecoverGCPBigQueryParams.md) |  | [optional] 
**gcp_firestore_params** | [**RecoverGCPFirestoreParams**](RecoverGCPFirestoreParams.md) |  | [optional] 
**gcp_my_sql_params** | [**RecoverGCPMySqlParams**](RecoverGCPMySqlParams.md) |  | [optional] 
**gcp_postgre_sql_params** | [**RecoverGCPPostgreSQLParams**](RecoverGCPPostgreSQLParams.md) |  | [optional] 
**gcp_sql_server_params** | [**RecoverGCPSqlServerParams**](RecoverGCPSqlServerParams.md) |  | [optional] 
**google_spanner_params** | [**RecoverGoogleSpannerParams**](RecoverGoogleSpannerParams.md) |  | [optional] 
**objects** | [**[CommonRecoverObjectSnapshotParams], none_type**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of recover Object parameters. This property is mandatory for all recovery action types except recover vms. While recovering VMs, a user can specify snapshots of VM&#39;s or a Protection Group Run details to recover all the VM&#39;s that are backed up by that Run. | [optional] 
**recover_file_and_folder_params** | [**RecoverGcpFileAndFolderParams**](RecoverGcpFileAndFolderParams.md) |  | [optional] 
**recover_vm_params** | [**RecoverGcpVmParams**](RecoverGcpVmParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


