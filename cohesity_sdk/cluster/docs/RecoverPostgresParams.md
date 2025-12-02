# RecoverPostgresParams

Specifies the parameters to recover Postgres objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apply_permissions** | **bool** | Specifies whether to apply the same permissions as the backup. | [optional] 
**default_permission** | **str** | Specifies the new permissions to be applied to the Postgres server. | [optional] 
**max_view_counts_per_host** | **int** | Specifies the maximum number of view mounts per host. If not specified, the default value is taken as 1. | [optional] [default to 1]
**num_concurrent_io_streams** | **int** | Specifies the maximum number of concurrent IO Streams that will be created to exchange data with the cluster. If not specified, the default value is taken as 1. | [optional] [default to 1]
**overwrite** | **bool** | Specifies whether to overwrite the existing objects. | [optional] 
**postgres_log_directory** | **str** | Specifies the directory where the Postgres logs are to be stored. | [optional] 
**postgres_server_cli_options** | **str** | Specifies the options to be passed to the Postgres server CLI. | [optional] 
**postgres_user_name** | **str** | Postgres service user needed for accessing the Postgres source. | [optional] 
**recover_to** | **int** | Specifies the &#39;Source Registration ID&#39; of the source where the objects are to be recovered. | 
**restore_type** | **str** | Specifies the type of restore to be performed. | [optional] 
**roll_forward_path** | **str** | Specifies the path to the local WAL files for doing roll forward. | [optional] 
**roll_forward_type** | **str** | Specifies the type of roll forward to be performed. | [optional] 
**snapshots** | [**List[RecoverUdaSnapshotParams]**](RecoverUdaSnapshotParams.md) | Specifies the snapshots to recover. | 
**ssl_server_certs_path** | **str** | Specifies the path to the SSL server certificates. | [optional] 
**start_server** | **bool** | Specifies whether to start the Postgres server after the recovery is complete. | [optional] 
**tablespace_dir** | **str** | Specifies the directory where the Postgres tablespaces need to be recovered. | [optional] 
**target_dir** | **str** | Specifies the target directory where the objects are to be recovered. | [optional] 
**warnings** | **List[str]** | This field will hold the warnings in cases where the job status is SucceededWithWarnings. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.recover_postgres_params import RecoverPostgresParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverPostgresParams from a JSON string
recover_postgres_params_instance = RecoverPostgresParams.from_json(json)
# print the JSON string representation of the object
print(RecoverPostgresParams.to_json())

# convert the object into a dict
recover_postgres_params_dict = recover_postgres_params_instance.to_dict()
# create an instance of RecoverPostgresParams from a dict
recover_postgres_params_from_dict = RecoverPostgresParams.from_dict(recover_postgres_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


