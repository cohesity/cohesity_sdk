# CreateUpgradeTaskRequest

Specifies the params to create a schedule based agent upgrade task.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the name of the task. | [optional] 
**description** | **str, none_type** | Specifies the description of the task. | [optional] 
**agent_ids** | **[int], none_type** | Specifies agent IDs to be upgraded in the task. | [optional] 
**schedule_time_usecs** | **int, none_type** | Specifies the start time of the task specified by the user as a Unix epoch Timestamp (in microseconds). If no schedule is specified, the agents will be upgraded immediately. | [optional] 
**schedule_end_time_usecs** | **int, none_type** | Specifies the time before which the upgrade task should start execution as a Unix epoch Timestamp (in microseconds). If this is not specified the task will start anytime after scheduleTimeUsecs. | [optional] 
**retry_task_id** | **int, none_type** | Specifies the task that needs to be retried. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


