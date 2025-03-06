# SecurityConfigSessionConfiguration

Specifies configuration for user sessions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**absolute_timeout** | **int** | Specifies absolute session expiration time in seconds. | [optional] 
**inactivity_timeout** | **int** | Specifies inactivity session expiration time in seconds. | [optional] 
**limit_sessions** | **bool** | Specifies if limitations on number of active sessions is enabled or not. | [optional] 
**session_limit_per_user** | **int** | Specifies maximum number of active sessions allowed per user. This applies only when limitSessions is enabled. | [optional] 
**session_limit_system_wide** | **int** | Specifies maximum number of active sessions allowed system wide. This applies only when limitSessions is enabled. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.security_config_session_configuration import SecurityConfigSessionConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityConfigSessionConfiguration from a JSON string
security_config_session_configuration_instance = SecurityConfigSessionConfiguration.from_json(json)
# print the JSON string representation of the object
print(SecurityConfigSessionConfiguration.to_json())

# convert the object into a dict
security_config_session_configuration_dict = security_config_session_configuration_instance.to_dict()
# create an instance of SecurityConfigSessionConfiguration from a dict
security_config_session_configuration_from_dict = SecurityConfigSessionConfiguration.from_dict(security_config_session_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


