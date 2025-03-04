# SimpleAuthParams

Specifies the parameters for LDAP with 'Simple' authentication type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_ssl** | **bool** | Specifies whether to use SSL for LDAP connections. | [optional] 
**user_distinguished_name** | **str** | Specifies the user distinguished name that is used for LDAP authentication. | 
**user_password** | **str** | Specifies the user password that is used for LDAP authentication. | [optional] 

## Example

```python
from cohesity_sdk.models.simple_auth_params import SimpleAuthParams

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleAuthParams from a JSON string
simple_auth_params_instance = SimpleAuthParams.from_json(json)
# print the JSON string representation of the object
print(SimpleAuthParams.to_json())

# convert the object into a dict
simple_auth_params_dict = simple_auth_params_instance.to_dict()
# create an instance of SimpleAuthParams from a dict
simple_auth_params_from_dict = SimpleAuthParams.from_dict(simple_auth_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


