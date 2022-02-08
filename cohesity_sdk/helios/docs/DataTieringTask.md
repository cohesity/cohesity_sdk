# DataTieringTask

Specifies the data tiering task details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the name of the data tiering task. | 
**type** | **str, none_type** | Type of data tiering task.   &#39;Downtier&#39; indicates downtiering task.   &#39;Uptier&#39; indicates uptiering task. | 
**id** | **str, none_type** | Specifies the id of the data tiering task. | [optional] 
**description** | **str, none_type** | Specifies a description of the data tiering task. | [optional] 
**alert_policy** | [**ProtectionGroupAlertingPolicy**](ProtectionGroupAlertingPolicy.md) |  | [optional] 
**source** | [**DataTieringSource**](DataTieringSource.md) |  | [optional] 
**target** | [**DataTieringTarget**](DataTieringTarget.md) |  | [optional] 
**schedule** | [**DataTieringSchedule**](DataTieringSchedule.md) |  | [optional] 
**last_run** | [**DataTieringTaskRun**](DataTieringTaskRun.md) |  | [optional] 
**is_active** | **bool, none_type** | Whether the data tiering task is active or not. | [optional]  if omitted the server will use the default value of True
**is_paused** | **bool, none_type** | Whether the data tiering task is paused. New runs are not scheduled   for the paused tasks. Active run of the task (if any) is not   impacted. | [optional]  if omitted the server will use the default value of True
**is_deleted** | **bool, none_type** | Tracks whether the backup job has actually been deleted. | [optional]  if omitted the server will use the default value of True
**downtiering_policy** | [**DowntieringPolicy**](DowntieringPolicy.md) |  | [optional] 
**uptiering_policy** | [**UptieringPolicy**](UptieringPolicy.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


