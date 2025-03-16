# McmAgentInfo

Specifies the information for agents related to the source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_display_name** | **str** | Specifies the hostname/ip address of the source. | [optional] 
**agent_id** | **int** | Specifies the ids of the agents related to the source. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_agent_info import McmAgentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of McmAgentInfo from a JSON string
mcm_agent_info_instance = McmAgentInfo.from_json(json)
# print the JSON string representation of the object
print(McmAgentInfo.to_json())

# convert the object into a dict
mcm_agent_info_dict = mcm_agent_info_instance.to_dict()
# create an instance of McmAgentInfo from a dict
mcm_agent_info_from_dict = McmAgentInfo.from_dict(mcm_agent_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


