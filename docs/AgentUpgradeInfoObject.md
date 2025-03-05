# AgentUpgradeInfoObject

Specifies the agent upgrade state.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the agent. | [optional] 
**info** | [**AgentInfoObject**](AgentInfoObject.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.agent_upgrade_info_object import AgentUpgradeInfoObject

# TODO update the JSON string below
json = "{}"
# create an instance of AgentUpgradeInfoObject from a JSON string
agent_upgrade_info_object_instance = AgentUpgradeInfoObject.from_json(json)
# print the JSON string representation of the object
print(AgentUpgradeInfoObject.to_json())

# convert the object into a dict
agent_upgrade_info_object_dict = agent_upgrade_info_object_instance.to_dict()
# create an instance of AgentUpgradeInfoObject from a dict
agent_upgrade_info_object_from_dict = AgentUpgradeInfoObject.from_dict(agent_upgrade_info_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


