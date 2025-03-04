# AgentInfoObject

Specifies the upgrade state of the agent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time_usecs** | **int** | Specifies the time when the upgrade for an agent completed as a Unix epoch Timestamp (in microseconds). | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**name** | **str** | Specifies the name of the source where the agent is installed. | [optional] 
**previous_software_version** | **str** | Specifies the software version of the agent before upgrade. | [optional] 
**start_time_usecs** | **int** | Specifies the time when the upgrade for an agent started as a Unix epoch Timestamp (in microseconds). | [optional] 
**status** | **str** | Specifies the upgrade status of the agent.&lt;br&gt; &#39;Scheduled&#39; indicates that upgrade for the agent is yet to start.&lt;br&gt; &#39;Started&#39; indicates that upgrade for the agent is started.&lt;br&gt; &#39;Succeeded&#39; indicates that agent was upgraded successfully.&lt;br&gt; &#39;Failed&#39; indicates that upgrade for the agent has failed.&lt;br&gt; &#39;Skipped&#39; indicates that upgrade for the agent was skipped. | [optional] 

## Example

```python
from cohesity_sdk.models.agent_info_object import AgentInfoObject

# TODO update the JSON string below
json = "{}"
# create an instance of AgentInfoObject from a JSON string
agent_info_object_instance = AgentInfoObject.from_json(json)
# print the JSON string representation of the object
print(AgentInfoObject.to_json())

# convert the object into a dict
agent_info_object_dict = agent_info_object_instance.to_dict()
# create an instance of AgentInfoObject from a dict
agent_info_object_from_dict = AgentInfoObject.from_dict(agent_info_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


