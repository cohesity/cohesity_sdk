# AgentUpgradeTaskActionRequest

Specifies the params to perform an action on an agent upgrade task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specifies the action type.&lt;br&gt; &#39;Cancel&#39; indicates that the upgrade task needs to be cancelled. | [optional] 
**id** | **int** | Specifies the ID of the task. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.agent_upgrade_task_action_request import AgentUpgradeTaskActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentUpgradeTaskActionRequest from a JSON string
agent_upgrade_task_action_request_instance = AgentUpgradeTaskActionRequest.from_json(json)
# print the JSON string representation of the object
print(AgentUpgradeTaskActionRequest.to_json())

# convert the object into a dict
agent_upgrade_task_action_request_dict = agent_upgrade_task_action_request_instance.to_dict()
# create an instance of AgentUpgradeTaskActionRequest from a dict
agent_upgrade_task_action_request_from_dict = AgentUpgradeTaskActionRequest.from_dict(agent_upgrade_task_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


