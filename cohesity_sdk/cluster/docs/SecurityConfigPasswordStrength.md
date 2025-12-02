# SecurityConfigPasswordStrength

Specifies security config for password strength.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_lower_letter** | **bool** | Specifies if the password needs to have at least one lowercase letter. | [optional] 
**include_number** | **bool** | Specifies if the password needs to have at least one number. | [optional] 
**include_special_char** | **bool** | Specifies if the password needs to have at least one special character. | [optional] 
**include_upper_letter** | **bool** | Specifies if the password needs to have at least one uppercase letter. | [optional] 
**min_length** | **int** | Specifies the password minimum length. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.security_config_password_strength import SecurityConfigPasswordStrength

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityConfigPasswordStrength from a JSON string
security_config_password_strength_instance = SecurityConfigPasswordStrength.from_json(json)
# print the JSON string representation of the object
print(SecurityConfigPasswordStrength.to_json())

# convert the object into a dict
security_config_password_strength_dict = security_config_password_strength_instance.to_dict()
# create an instance of SecurityConfigPasswordStrength from a dict
security_config_password_strength_from_dict = SecurityConfigPasswordStrength.from_dict(security_config_password_strength_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


