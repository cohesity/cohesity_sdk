# ScriptHost

Specifies the params for the host of a pre / post script.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_type** | **str** | Specifies the Operating system type of the host. | [optional] 
**hostname** | **str** | Specifies the Hostname or IP address of the host where the pre and post script will be run. | [optional] 
**username** | **str** | Specifies the username for the host. | [optional] 

## Example

```python
from cohesity_sdk.models.script_host import ScriptHost

# TODO update the JSON string below
json = "{}"
# create an instance of ScriptHost from a JSON string
script_host_instance = ScriptHost.from_json(json)
# print the JSON string representation of the object
print(ScriptHost.to_json())

# convert the object into a dict
script_host_dict = script_host_instance.to_dict()
# create an instance of ScriptHost from a dict
script_host_from_dict = ScriptHost.from_dict(script_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


