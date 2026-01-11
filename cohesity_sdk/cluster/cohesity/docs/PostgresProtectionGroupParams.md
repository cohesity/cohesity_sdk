# PostgresProtectionGroupParams

Specifies parameters related to the Postgres Protection group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[UdaProtectionGroupObjectParams]**](UdaProtectionGroupObjectParams.md) | Specifies a list of fully qualified names of the objects to be protected. | 
**source_id** | **int** | Specifies the source Id of the objects to be protected. | 
**convert_incremental_to_full_on_error** | **bool, none_type** | Specifies the flag to convert incremental backup to full backup on failure. | [optional] 
**max_view_counts_per_host** | **int, none_type** | Specifies the maximum number of view mounts per host. If not specified, the default value is taken as 1. | [optional]  if omitted the server will use the default value of 1
**num_concurrent_io_streams** | **int, none_type** | Specifies the maximum number of concurrent IO Streams that will be created to exchange data with the cluster. If not specified, the default value is taken as 1. | [optional]  if omitted the server will use the default value of 1
**postgres_user_name** | **str, none_type** | Postgres service user needed for accessing the Postgres source. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


