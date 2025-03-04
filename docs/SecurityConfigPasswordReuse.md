# SecurityConfigPasswordReuse

Specifies security config for password reuse.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_different_chars** | **int** | Specifies the number of characters in the new password that needs to be different from the old password (only applicable when changing the user&#39;s own password). | [optional] 
**num_disallowed_old_passwords** | **int** | Specifies the minimum number of old passwords that are not allowed for changing the password. | [optional] 

## Example

```python
from cohesity_sdk.models.security_config_password_reuse import SecurityConfigPasswordReuse

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityConfigPasswordReuse from a JSON string
security_config_password_reuse_instance = SecurityConfigPasswordReuse.from_json(json)
# print the JSON string representation of the object
print(SecurityConfigPasswordReuse.to_json())

# convert the object into a dict
security_config_password_reuse_dict = security_config_password_reuse_instance.to_dict()
# create an instance of SecurityConfigPasswordReuse from a dict
security_config_password_reuse_from_dict = SecurityConfigPasswordReuse.from_dict(security_config_password_reuse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


