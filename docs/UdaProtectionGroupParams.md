# UdaProtectionGroupParams

Specifies parameters related to the Universal Data Adapter Protection job.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **int, none_type** | Specifies the source Id of the objects to be protected. | 
**objects** | [**[UdaProtectionGroupObjectParams]**](UdaProtectionGroupObjectParams.md) | Specifies a list of fully qualified names of the objects to be protected. | 
**full_backup_args** | **str, none_type** | Specifies the custom arguments to be supplied to the full backup script when a full backup is enabled in the policy. | [optional] 
**incr_backup_args** | **str, none_type** | Specifies the custom arguments to be supplied to the incremental backup script when an incremental backup is enabled in the policy. | [optional] 
**log_backup_args** | **str, none_type** | Specifies the custom arguments to be supplied to the log backup script when a log backup is enabled in the policy. | [optional] 
**concurrency** | **int, none_type** | Specifies the maximum number of concurrent IO Streams that will be created to exchange data with the cluster. If not specified, the default value is taken as 1. | [optional]  if omitted the server will use the default value of 1
**mounts** | **int, none_type** | Specifies the maximum number of view mounts per host. If not specified, the default value is taken as 1. | [optional]  if omitted the server will use the default value of 1

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


