# TdmTask

Specifies a TDM task.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str, none_type** | Specifies the TDM Task action. | 
**id** | **str, none_type** | Specifies the unique ID of the task. | 
**created_by_user** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the user, who created this task. | [optional] 
**end_time_usecs** | **int, none_type** | Specifies the time (in usecs from epoch) when the task was completed. | [optional] 
**name** | **str, none_type** | Specifies the name of the task. | [optional] 
**progress_task_id** | **str, none_type** | Specifies the ID for tracking progress of this task. | [optional] 
**start_time_usecs** | **int, none_type** | Specifies the time (in usecs from epoch) when the task was started. | [optional] 
**status** | **str, none_type** | Specifies the current status of the task. | [optional] 
**clone_params** | [**TdmCloneTaskResponseParams**](TdmCloneTaskResponseParams.md) |  | [optional] 
**refresh_params** | [**TdmRefreshTaskResponseParams**](TdmRefreshTaskResponseParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


