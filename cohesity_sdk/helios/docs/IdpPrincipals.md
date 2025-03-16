# IdpPrincipals

Specifies a list of IDP Principals.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principals** | [**List[IdpPrincipal]**](IdpPrincipal.md) | Specifies a list of IDP Principals. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.idp_principals import IdpPrincipals

# TODO update the JSON string below
json = "{}"
# create an instance of IdpPrincipals from a JSON string
idp_principals_instance = IdpPrincipals.from_json(json)
# print the JSON string representation of the object
print(IdpPrincipals.to_json())

# convert the object into a dict
idp_principals_dict = idp_principals_instance.to_dict()
# create an instance of IdpPrincipals from a dict
idp_principals_from_dict = IdpPrincipals.from_dict(idp_principals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


