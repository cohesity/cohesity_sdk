# ProgressTask

This specifies the details about the Progress Task.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Specifies the task id of the Progress task. | [optional] 
**end_time_usecs** | **int, none_type** | Specifies the end time of the progress task in Unix epoch Timestamp(in microseconds). | [optional] 
**events** | [**[ProgressTaskEvent]**](ProgressTaskEvent.md) | Specifies the event log created for progress Task. | [optional] 
**expected_remaining_time_usecs** | **int, none_type** | Specifies the expected remaining time of the progress task in Unix epoch Timestamp(in microseconds). | [optional] 
**percentage_completed** | **float, none_type** | Specifies the current completed percentage of the progress task. | [optional] 
**start_time_usecs** | **int, none_type** | Specifies the start time of the progress task in Unix epoch Timestamp(in microseconds). | [optional] 
**stats** | [**ProgressStats**](ProgressStats.md) |  | [optional] 
**status** | **str, none_type** | Specifies the current status of the progress task. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


