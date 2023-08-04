# ArchivalTargetProgressInfo

Specifies the progress of an archival run target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_id** | **int, none_type** | Specifies the archival target ID. | [optional] 
**archival_task_id** | **str, none_type** | Specifies the archival task id. This is a protection group UID which only applies when archival type is &#39;Tape&#39;. | [optional] 
**target_name** | **str, none_type** | Specifies the archival target name. | [optional] 
**target_type** | **str, none_type** | Specifies the archival target type. | [optional] 
**usage_type** | **str, none_type** | Specifies the usage type for the target. | [optional] 
**ownership_context** | **str, none_type** | Specifies the ownership context for the target. | [optional] 
**tier_settings** | [**ArchivalTargetTierInfo**](ArchivalTargetTierInfo.md) |  | [optional] 
**status** | **str, none_type** | Specifies the current status of the progress task. | [optional] 
**percentage_completed** | **float, none_type** | Specifies the current completed percentage of the progress task. | [optional] 
**start_time_usecs** | **int, none_type** | Specifies the start time of the progress task in Unix epoch Timestamp(in microseconds). | [optional] 
**end_time_usecs** | **int, none_type** | Specifies the end time of the progress task in Unix epoch Timestamp(in microseconds). | [optional] 
**expected_remaining_time_usecs** | **int, none_type** | Specifies the expected remaining time of the progress task in Unix epoch Timestamp(in microseconds). | [optional] 
**events** | [**[ProgressTaskEvent]**](ProgressTaskEvent.md) | Specifies the event log created for progress Task. | [optional] 
**stats** | [**ProgressStats**](ProgressStats.md) |  | [optional] 
**objects** | [**[ObjectProgressInfo], none_type**](ObjectProgressInfo.md) | Specifies progress for objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


