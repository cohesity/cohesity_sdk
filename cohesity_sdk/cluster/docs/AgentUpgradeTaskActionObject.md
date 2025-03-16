# AgentUpgradeTaskActionObject

Specifies the action on an upgrade task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**Error**](Error.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.agent_upgrade_task_action_object import AgentUpgradeTaskActionObject

# TODO update the JSON string below
json = "{}"
# create an instance of AgentUpgradeTaskActionObject from a JSON string
agent_upgrade_task_action_object_instance = AgentUpgradeTaskActionObject.from_json(json)
# print the JSON string representation of the object
print(AgentUpgradeTaskActionObject.to_json())

# convert the object into a dict
agent_upgrade_task_action_object_dict = agent_upgrade_task_action_object_instance.to_dict()
# create an instance of AgentUpgradeTaskActionObject from a dict
agent_upgrade_task_action_object_from_dict = AgentUpgradeTaskActionObject.from_dict(agent_upgrade_task_action_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


