# StandaloneHostRegistrationParams

Specifies parameters to register standalone HyperV host.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Specifies the description of the source being registered. | [optional] 
**endpoint** | **str** | Specifies the endpoint IPaddress, URL or hostname of the host. | 

## Example

```python
from cohesity_sdk.models.standalone_host_registration_params import StandaloneHostRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of StandaloneHostRegistrationParams from a JSON string
standalone_host_registration_params_instance = StandaloneHostRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(StandaloneHostRegistrationParams.to_json())

# convert the object into a dict
standalone_host_registration_params_dict = standalone_host_registration_params_instance.to_dict()
# create an instance of StandaloneHostRegistrationParams from a dict
standalone_host_registration_params_from_dict = StandaloneHostRegistrationParams.from_dict(standalone_host_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


