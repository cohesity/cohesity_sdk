# SecurityConfigPasswordLifetime

Specifies security config for password lifetime.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_lifetime_days** | **int** | Specifies the maximum password lifetime in days. | [optional] 
**min_lifetime_days** | **int** | Specifies the minimum password lifetime in days. | [optional] 

## Example

```python
from cohesity_sdk.models.security_config_password_lifetime import SecurityConfigPasswordLifetime

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityConfigPasswordLifetime from a JSON string
security_config_password_lifetime_instance = SecurityConfigPasswordLifetime.from_json(json)
# print the JSON string representation of the object
print(SecurityConfigPasswordLifetime.to_json())

# convert the object into a dict
security_config_password_lifetime_dict = security_config_password_lifetime_instance.to_dict()
# create an instance of SecurityConfigPasswordLifetime from a dict
security_config_password_lifetime_from_dict = SecurityConfigPasswordLifetime.from_dict(security_config_password_lifetime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


