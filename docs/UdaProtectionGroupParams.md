# UdaProtectionGroupParams

Specifies parameters related to the Universal Data Adapter Protection job.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[UdaProtectionGroupObjectParams]**](UdaProtectionGroupObjectParams.md) | Specifies a list of fully qualified names of the objects to be protected. | 
**source_id** | **int, none_type** | Specifies the source Id of the objects to be protected. | 
**backup_job_arguments** | [**[KeyValuePair], none_type**](KeyValuePair.md) | Specifies the map of custom arguments to be supplied to the various backup scripts. | [optional] 
**concurrency** | **int, none_type** | Specifies the maximum number of concurrent IO Streams that will be created to exchange data with the cluster. If not specified, the default value is taken as 1. | [optional]  if omitted the server will use the default value of 1
**et_log_backup** | **bool, none_type** | Specifies whether this Protection Group is created from a source having externally triggered log backup support. | [optional] [readonly] 
**exclude_object_ids** | **[int], none_type** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**full_backup_args** | **str, none_type** | Specifies the custom arguments to be supplied to the full backup script when a full backup is enabled in the policy. This field is deprecated. Use backupJobArguments instead. | [optional] 
**has_entity_support** | **bool, none_type** | Specifies whether this Protection Group is created from a source having entity support. | [optional] [readonly] 
**incr_backup_args** | **str, none_type** | Specifies the custom arguments to be supplied to the incremental backup script when an incremental backup is enabled in the policy. This field is deprecated. Use backupJobArguments instead. | [optional] 
**log_backup_args** | **str, none_type** | Specifies the custom arguments to be supplied to the log backup script when a log backup is enabled in the policy. This field is deprecated. Use backupJobArguments instead. | [optional] 
**mounts** | **int, none_type** | Specifies the maximum number of view mounts per host. If not specified, the default value is taken as 1. | [optional]  if omitted the server will use the default value of 1

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


