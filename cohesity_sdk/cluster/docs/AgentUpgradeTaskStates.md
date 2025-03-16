# AgentUpgradeTaskStates

List of agent upgrade tasks.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tasks** | [**List[AgentUpgradeTaskState]**](AgentUpgradeTaskState.md) | Specifies the list of agent upgrade tasks. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.agent_upgrade_task_states import AgentUpgradeTaskStates

# TODO update the JSON string below
json = "{}"
# create an instance of AgentUpgradeTaskStates from a JSON string
agent_upgrade_task_states_instance = AgentUpgradeTaskStates.from_json(json)
# print the JSON string representation of the object
print(AgentUpgradeTaskStates.to_json())

# convert the object into a dict
agent_upgrade_task_states_dict = agent_upgrade_task_states_instance.to_dict()
# create an instance of AgentUpgradeTaskStates from a dict
agent_upgrade_task_states_from_dict = AgentUpgradeTaskStates.from_dict(agent_upgrade_task_states_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


