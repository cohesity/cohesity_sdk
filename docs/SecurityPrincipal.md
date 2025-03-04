# SecurityPrincipal

Specifies a security principal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | Specifies the domain name where the security principal account is maintained. | [optional] 
**full_name** | **str** | Specifies the full name (first and last name) of the security principal. | [optional] 
**object_class** | **str** | Specifies the object class of the security principal. | [optional] 
**principal_name** | **str** | Specifies the name of the security principal. | [optional] 
**sid** | **str** | Specifies the SID of the security principal. | [optional] 

## Example

```python
from cohesity_sdk.models.security_principal import SecurityPrincipal

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityPrincipal from a JSON string
security_principal_instance = SecurityPrincipal.from_json(json)
# print the JSON string representation of the object
print(SecurityPrincipal.to_json())

# convert the object into a dict
security_principal_dict = security_principal_instance.to_dict()
# create an instance of SecurityPrincipal from a dict
security_principal_from_dict = SecurityPrincipal.from_dict(security_principal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


