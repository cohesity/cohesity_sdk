# LinuxAgentParams

Linux agent parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_type** | **str** | Specifies the type of installer. | 

## Example

```python
from cohesity_sdk.models.linux_agent_params import LinuxAgentParams

# TODO update the JSON string below
json = "{}"
# create an instance of LinuxAgentParams from a JSON string
linux_agent_params_instance = LinuxAgentParams.from_json(json)
# print the JSON string representation of the object
print(LinuxAgentParams.to_json())

# convert the object into a dict
linux_agent_params_dict = linux_agent_params_instance.to_dict()
# create an instance of LinuxAgentParams from a dict
linux_agent_params_from_dict = LinuxAgentParams.from_dict(linux_agent_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


