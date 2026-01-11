# RecoverDB2Params

Specifies the parameters to recover DB2 objects.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing Source Target. | 
**snapshots** | [**[RecoverUdaSnapshotParams], none_type**](RecoverUdaSnapshotParams.md) | Specifies the local snapshot ids and other details of the objects to be recovered. | 
**concurrency** | **int, none_type** | Specifies the maximum number of concurrent IO Streams that will be created to exchange data with the cluster. If not specified, the default value is taken as 1. | [optional]  if omitted the server will use the default value of 1
**mounts** | **int, none_type** | Specifies the maximum number of view mounts per host. If not specified, the default value is taken as 1. | [optional]  if omitted the server will use the default value of 1
**recovery_job_arguments** | [**[KeyValuePair], none_type**](KeyValuePair.md) | Specifies the map of custom arguments to be supplied to the restore job script. | [optional] 
**recovery_target_config** | [**RecoverDB2TargetConfig**](RecoverDB2TargetConfig.md) |  | [optional] 
**rollforward_database** | **bool, none_type** | Roll forward the database after the recovery is complete. Enabled by default. | [optional]  if omitted the server will use the default value of True
**warnings** | **[str], none_type** | This field will hold the warnings in cases where the job status is SucceededWithWarnings. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


