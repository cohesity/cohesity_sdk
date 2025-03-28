# AgentUpgradeTaskState

Specifies the state of an agent upgrade task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_ids** | **List[int]** | Specifies the agents upgraded in the task. | [optional] 
**agents** | [**List[AgentUpgradeInfoObject]**](AgentUpgradeInfoObject.md) | Specifies the upgrade information for each agent. | [optional] 
**cluster_version** | **str** | Specifies the version to which agents are upgraded. | [optional] 
**description** | **str** | Specifies the description of the task. | [optional] 
**end_time_usecs** | **int** | Specifies the time when the upgrade task completed execution as a Unix epoch Timestamp (in microseconds). | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**id** | **int** | Specifies the ID of the task. | [optional] 
**is_retryable** | **bool** | Specifies if a task can be retried. | [optional] 
**name** | **str** | Specifies the name of the task. | [optional] 
**retried_task_id** | **int** | Specifies ID of a task which was retried if type is &#39;Retry&#39;. | [optional] 
**schedule_end_time_usecs** | **int** | Specifies the time before which the upgrade task should start execution as a Unix epoch Timestamp (in microseconds). If this is not specified the task will start anytime after scheduleTimeUsecs. | [optional] 
**schedule_time_usecs** | **int** | Specifies the time when the task should start execution as a Unix epoch Timestamp (in microseconds). If no schedule is specified, the task will start immediately. | [optional] 
**start_time_usecs** | **int** | Specifies the time, as a Unix epoch timestamp in microseconds, when the task started execution. | [optional] 
**status** | **str** | Specifies the status of the task.&lt;br&gt; &#39;Scheduled&#39; indicates that the upgrade task is yet to start.&lt;br&gt; &#39;Running&#39; indicates that the upgrade task has started execution.&lt;br&gt; &#39;Succeeded&#39; indicates that the upgrade task completed without an error.&lt;br&gt; &#39;Failed&#39; indicates that upgrade has failed for all agents. &#39;PartiallyFailed&#39; indicates that upgrade has failed for some agents. | [optional] 
**type** | **str** | Specifes the type of task.&lt;br&gt; &#39;Auto&#39; indicates an auto agent upgrade task which is started after a cluster upgrade.&lt;br&gt; &#39;Manual&#39; indicates a schedule based agent upgrade task.&lt;br&gt; &#39;Retry&#39; indicates an agent upgrade task which was retried. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.agent_upgrade_task_state import AgentUpgradeTaskState

# TODO update the JSON string below
json = "{}"
# create an instance of AgentUpgradeTaskState from a JSON string
agent_upgrade_task_state_instance = AgentUpgradeTaskState.from_json(json)
# print the JSON string representation of the object
print(AgentUpgradeTaskState.to_json())

# convert the object into a dict
agent_upgrade_task_state_dict = agent_upgrade_task_state_instance.to_dict()
# create an instance of AgentUpgradeTaskState from a dict
agent_upgrade_task_state_from_dict = AgentUpgradeTaskState.from_dict(agent_upgrade_task_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


