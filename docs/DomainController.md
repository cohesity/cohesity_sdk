# DomainController

Specifies a domain controller.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the domain controller name. | 
**status** | **str** | Specifies the connection status. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.domain_controller import DomainController

# TODO update the JSON string below
json = "{}"
# create an instance of DomainController from a JSON string
domain_controller_instance = DomainController.from_json(json)
# print the JSON string representation of the object
print(DomainController.to_json())

# convert the object into a dict
domain_controller_dict = domain_controller_instance.to_dict()
# create an instance of DomainController from a dict
domain_controller_from_dict = DomainController.from_dict(domain_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


