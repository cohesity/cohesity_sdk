# EndpointOnlyRegistrationParams

Specifies an endpoint to register a source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Specifies the description of the source being registered. | [optional] 
**endpoint** | **str** | Specifies the endpoint IPaddress, URL or hostname of the host. | 

## Example

```python
from cohesity_sdk.helios.models.endpoint_only_registration_params import EndpointOnlyRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointOnlyRegistrationParams from a JSON string
endpoint_only_registration_params_instance = EndpointOnlyRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(EndpointOnlyRegistrationParams.to_json())

# convert the object into a dict
endpoint_only_registration_params_dict = endpoint_only_registration_params_instance.to_dict()
# create an instance of EndpointOnlyRegistrationParams from a dict
endpoint_only_registration_params_from_dict = EndpointOnlyRegistrationParams.from_dict(endpoint_only_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


