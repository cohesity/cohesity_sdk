# DomainControllersResponse

Specifies the response of get domain controllers request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_controllers** | [**List[DomainControllers]**](DomainControllers.md) | A list of domain names with a list of it&#39;s domain controllers. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.domain_controllers_response import DomainControllersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainControllersResponse from a JSON string
domain_controllers_response_instance = DomainControllersResponse.from_json(json)
# print the JSON string representation of the object
print(DomainControllersResponse.to_json())

# convert the object into a dict
domain_controllers_response_dict = domain_controllers_response_instance.to_dict()
# create an instance of DomainControllersResponse from a dict
domain_controllers_response_from_dict = DomainControllersResponse.from_dict(domain_controllers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


