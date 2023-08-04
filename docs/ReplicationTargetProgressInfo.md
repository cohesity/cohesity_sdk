# ReplicationTargetProgressInfo

Specifies the progress of a replication run target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int, none_type** | Specifies the id of the cluster. | [optional] 
**cluster_incarnation_id** | **int, none_type** | Specifies the incarnation id of the cluster. | [optional] 
**cluster_name** | **str, none_type** | Specifies the name of the cluster. | [optional] [readonly] 
**aws_target_config** | [**AWSTargetConfig**](AWSTargetConfig.md) |  | [optional] 
**azure_target_config** | [**AzureTargetConfig**](AzureTargetConfig.md) |  | [optional] 
**status** | **str, none_type** | Specifies the current status of the progress task. | [optional] 
**percentage_completed** | **float, none_type** | Specifies the current completed percentage of the progress task. | [optional] 
**start_time_usecs** | **int, none_type** | Specifies the start time of the progress task in Unix epoch Timestamp(in microseconds). | [optional] 
**end_time_usecs** | **int, none_type** | Specifies the end time of the progress task in Unix epoch Timestamp(in microseconds). | [optional] 
**expected_remaining_time_usecs** | **int, none_type** | Specifies the expected remaining time of the progress task in Unix epoch Timestamp(in microseconds). | [optional] 
**events** | [**[ProgressTaskEvent]**](ProgressTaskEvent.md) | Specifies the event log created for progress Task. | [optional] 
**stats** | [**ProgressStats**](ProgressStats.md) |  | [optional] 
**objects** | [**[ObjectProgressInfo], none_type**](ObjectProgressInfo.md) | Specifies progress for objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


