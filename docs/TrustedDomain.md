# TrustedDomain

Specifies the details of a trusted domain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_controllers_deny_list** | **List[Optional[str]]** | Specifies a list of denied domain controllers of this domain. | [optional] 
**domain_name** | **str** | Specifies a domain name. | [optional] 
**preferred_domain_controllers** | [**List[DomainController]**](DomainController.md) | Specifies a list of preferred domain controllers for this domain. | [optional] 

## Example

```python
from cohesity_sdk.models.trusted_domain import TrustedDomain

# TODO update the JSON string below
json = "{}"
# create an instance of TrustedDomain from a JSON string
trusted_domain_instance = TrustedDomain.from_json(json)
# print the JSON string representation of the object
print(TrustedDomain.to_json())

# convert the object into a dict
trusted_domain_dict = trusted_domain_instance.to_dict()
# create an instance of TrustedDomain from a dict
trusted_domain_from_dict = TrustedDomain.from_dict(trusted_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


