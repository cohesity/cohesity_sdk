# DomainScopeParams

Specifies the parameters for domain type scope

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | Specifies the domain name. | 

## Example

```python
from cohesity_sdk.models.domain_scope_params import DomainScopeParams

# TODO update the JSON string below
json = "{}"
# create an instance of DomainScopeParams from a JSON string
domain_scope_params_instance = DomainScopeParams.from_json(json)
# print the JSON string representation of the object
print(DomainScopeParams.to_json())

# convert the object into a dict
domain_scope_params_dict = domain_scope_params_instance.to_dict()
# create an instance of DomainScopeParams from a dict
domain_scope_params_from_dict = DomainScopeParams.from_dict(domain_scope_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


