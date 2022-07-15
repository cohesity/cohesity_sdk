# CommonTdmTaskResponseParamsf06bd8b0C5ac4884B47a096f10d64533TdmCloneTaskResponseParamsWrapper


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Specifies the unique ID of the task. | 
**action** | **str, none_type** | Specifies the TDM Task action. | 
**name** | **str, none_type** | Specifies the name of the task. | [optional] 
**start_time_usecs** | **int, none_type** | Specifies the time (in usecs from epoch) when the task was started. | [optional] 
**end_time_usecs** | **int, none_type** | Specifies the time (in usecs from epoch) when the task was completed. | [optional] 
**status** | **str, none_type** | Specifies the current status of the task. | [optional] 
**created_by_user** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the user, who created this task. | [optional] 
**progress_task_id** | **str, none_type** | Specifies the ID for tracking progress of this task. | [optional] 
**clone_params** | [**TdmCloneTaskResponseParams**](TdmCloneTaskResponseParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


