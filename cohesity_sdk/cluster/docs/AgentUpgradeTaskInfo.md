# AgentUpgradeTaskInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Agent Upgrade task. | [optional] 
**start_time_usecs** | **str** | Denotes the start time of the agent upgrade task. | [optional] 
**task_id** | **str** | Id of the Agent Upgrade task. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.agent_upgrade_task_info import AgentUpgradeTaskInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AgentUpgradeTaskInfo from a JSON string
agent_upgrade_task_info_instance = AgentUpgradeTaskInfo.from_json(json)
# print the JSON string representation of the object
print(AgentUpgradeTaskInfo.to_json())

# convert the object into a dict
agent_upgrade_task_info_dict = agent_upgrade_task_info_instance.to_dict()
# create an instance of AgentUpgradeTaskInfo from a dict
agent_upgrade_task_info_from_dict = AgentUpgradeTaskInfo.from_dict(agent_upgrade_task_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


