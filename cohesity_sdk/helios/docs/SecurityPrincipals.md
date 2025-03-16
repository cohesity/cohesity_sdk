# SecurityPrincipals

Specifies a list of security principals.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**security_principals** | [**List[SecurityPrincipal]**](SecurityPrincipal.md) | Specifies a list of security principals. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.security_principals import SecurityPrincipals

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityPrincipals from a JSON string
security_principals_instance = SecurityPrincipals.from_json(json)
# print the JSON string representation of the object
print(SecurityPrincipals.to_json())

# convert the object into a dict
security_principals_dict = security_principals_instance.to_dict()
# create an instance of SecurityPrincipals from a dict
security_principals_from_dict = SecurityPrincipals.from_dict(security_principals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


