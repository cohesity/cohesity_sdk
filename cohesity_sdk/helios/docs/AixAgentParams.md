# AixAgentParams

Aix agent parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_type** | **str** | Specifies the type of agent. | 

## Example

```python
from cohesity_sdk.helios.models.aix_agent_params import AixAgentParams

# TODO update the JSON string below
json = "{}"
# create an instance of AixAgentParams from a JSON string
aix_agent_params_instance = AixAgentParams.from_json(json)
# print the JSON string representation of the object
print(AixAgentParams.to_json())

# convert the object into a dict
aix_agent_params_dict = aix_agent_params_instance.to_dict()
# create an instance of AixAgentParams from a dict
aix_agent_params_from_dict = AixAgentParams.from_dict(aix_agent_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


