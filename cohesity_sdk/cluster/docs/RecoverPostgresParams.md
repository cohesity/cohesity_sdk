# RecoverPostgresParams

Specifies the parameters to recover Postgres objects.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_to** | **int** | Specifies the &#39;Source Registration ID&#39; of the source where the objects are to be recovered. | 
**snapshots** | [**[RecoverUdaSnapshotParams]**](RecoverUdaSnapshotParams.md) | Specifies the snapshots to recover. | 
**apply_permissions** | **bool, none_type** | Specifies whether to apply the same permissions as the backup. | [optional] 
**default_permission** | **str, none_type** | Specifies the new permissions to be applied to the Postgres server. | [optional] 
**max_view_counts_per_host** | **int, none_type** | Specifies the maximum number of view mounts per host. If not specified, the default value is taken as 1. | [optional]  if omitted the server will use the default value of 1
**num_concurrent_io_streams** | **int, none_type** | Specifies the maximum number of concurrent IO Streams that will be created to exchange data with the cluster. If not specified, the default value is taken as 1. | [optional]  if omitted the server will use the default value of 1
**overwrite** | **bool, none_type** | Specifies whether to overwrite the existing objects. | [optional] 
**postgres_log_directory** | **str, none_type** | Specifies the directory where the Postgres logs are to be stored. | [optional] 
**postgres_server_cli_options** | **str, none_type** | Specifies the options to be passed to the Postgres server CLI. | [optional] 
**postgres_user_name** | **str, none_type** | Postgres service user needed for accessing the Postgres source. | [optional] 
**restore_type** | **str, none_type** | Specifies the type of restore to be performed. | [optional] 
**roll_forward_path** | **str, none_type** | Specifies the path to the local WAL files for doing roll forward. | [optional] 
**roll_forward_type** | **str, none_type** | Specifies the type of roll forward to be performed. | [optional] 
**ssl_server_certs_path** | **str, none_type** | Specifies the path to the SSL server certificates. | [optional] 
**start_server** | **bool, none_type** | Specifies whether to start the Postgres server after the recovery is complete. | [optional] 
**tablespace_dir** | **str, none_type** | Specifies the directory where the Postgres tablespaces need to be recovered. | [optional] 
**target_dir** | **str, none_type** | Specifies the target directory where the objects are to be recovered. | [optional] 
**warnings** | **[str], none_type** | This field will hold the warnings in cases where the job status is SucceededWithWarnings. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


