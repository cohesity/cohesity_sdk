# TrustedDomainInfo

Specifies the information regarding domain controllers and preferred domain controllers of a trusted domain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_controllers** | **List[str]** | Specifies the list of its domain controllers. | [optional] 
**preferred_domain_controllers** | **List[str]** | Specifies the list of its preferred domain controllers. | [optional] 
**trusted_domain_name** | **str** | Specifies the domain name of this trusted domain. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.trusted_domain_info import TrustedDomainInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TrustedDomainInfo from a JSON string
trusted_domain_info_instance = TrustedDomainInfo.from_json(json)
# print the JSON string representation of the object
print(TrustedDomainInfo.to_json())

# convert the object into a dict
trusted_domain_info_dict = trusted_domain_info_instance.to_dict()
# create an instance of TrustedDomainInfo from a dict
trusted_domain_info_from_dict = TrustedDomainInfo.from_dict(trusted_domain_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


