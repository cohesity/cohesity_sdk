# AgentInformation

Specifies the agent details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_sw_version** | **str** | Specifies the software version of the agent | [optional] 
**connection_status** | **str** | Specifies the status of agent connection. | [optional] 
**host_setting_checks** | [**List[HostSettingCheck]**](HostSettingCheck.md) | Specifies the list of host checks and its results. | [optional] 
**last_fetched_time_in_usecs** | **int** | Specifies the time in usecs when the last agent info was fetched. | [optional] 
**support_status** | **str** | Specifies the whether agent version is compatible with cluster version ro use various features. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.agent_information import AgentInformation

# TODO update the JSON string below
json = "{}"
# create an instance of AgentInformation from a JSON string
agent_information_instance = AgentInformation.from_json(json)
# print the JSON string representation of the object
print(AgentInformation.to_json())

# convert the object into a dict
agent_information_dict = agent_information_instance.to_dict()
# create an instance of AgentInformation from a dict
agent_information_from_dict = AgentInformation.from_dict(agent_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


