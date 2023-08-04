# AgentUpgradeTaskState

Specifies the state of an agent upgrade task.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the name of the task. | [optional] 
**description** | **str, none_type** | Specifies the description of the task. | [optional] 
**id** | **int, none_type** | Specifies the ID of the task. | [optional] 
**start_time_usecs** | **int, none_type** | Specifies the time, as a Unix epoch timestamp in microseconds, when the task started execution. | [optional] 
**end_time_usecs** | **int, none_type** | Specifies the time when the upgrade task completed execution as a Unix epoch Timestamp (in microseconds). | [optional] 
**status** | **str, none_type** | Specifies the status of the task.&lt;br&gt; &#39;Scheduled&#39; indicates that the upgrade task is yet to start.&lt;br&gt; &#39;Running&#39; indicates that the upgrade task has started execution.&lt;br&gt; &#39;Succeeded&#39; indicates that the upgrade task completed without an error.&lt;br&gt; &#39;Failed&#39; indicates that upgrade has failed for all agents. &#39;PartiallyFailed&#39; indicates that upgrade has failed for some agents. | [optional] 
**agent_ids** | **[int], none_type** | Specifies the agents upgraded in the task. | [optional] 
**cluster_version** | **str, none_type** | Specifies the version to which agents are upgraded. | [optional] 
**type** | **str, none_type** | Specifes the type of task.&lt;br&gt; &#39;Auto&#39; indicates an auto agent upgrade task which is started after a cluster upgrade.&lt;br&gt; &#39;Manual&#39; indicates a schedule based agent upgrade task.&lt;br&gt; &#39;Retry&#39; indicates an agent upgrade task which was retried. | [optional] 
**schedule_time_usecs** | **int, none_type** | Specifies the time when the task should start execution as a Unix epoch Timestamp (in microseconds). If no schedule is specified, the task will start immediately. | [optional] 
**schedule_end_time_usecs** | **int, none_type** | Specifies the time before which the upgrade task should start execution as a Unix epoch Timestamp (in microseconds). If this is not specified the task will start anytime after scheduleTimeUsecs. | [optional] 
**retried_task_id** | **int, none_type** | Specifies ID of a task which was retried if type is &#39;Retry&#39;. | [optional] 
**is_retryable** | **bool, none_type** | Specifies if a task can be retried. | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**agents** | [**[AgentUpgradeInfoObject], none_type**](AgentUpgradeInfoObject.md) | Specifies the upgrade information for each agent. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


