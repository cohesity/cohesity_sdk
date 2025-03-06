# DomainControllers

Specifies the domain controllers of a domain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controllers** | [**List[DomainController]**](DomainController.md) | Specifies a list of domain controllers of the domain. | [optional] 
**domain_name** | **str** | Specifies the domain name. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.domain_controllers import DomainControllers

# TODO update the JSON string below
json = "{}"
# create an instance of DomainControllers from a JSON string
domain_controllers_instance = DomainControllers.from_json(json)
# print the JSON string representation of the object
print(DomainControllers.to_json())

# convert the object into a dict
domain_controllers_dict = domain_controllers_instance.to_dict()
# create an instance of DomainControllers from a dict
domain_controllers_from_dict = DomainControllers.from_dict(domain_controllers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


