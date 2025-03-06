# SecurityConfigAccountLockout

Specifies security config for account lockout.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed_login_lock_time_duration_mins** | **int** | Specifies the time duration within which the consecutive failed login attempts causes a local user account to be locked and the lockout duration time due to that. | [optional] 
**inactivity_time_days** | **int** | Specifies the lockout inactivity time range in days. | [optional] 
**max_failed_login_attempts** | **int** | Specifies the maximum number of consecutive fail login attempts. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.security_config_account_lockout import SecurityConfigAccountLockout

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityConfigAccountLockout from a JSON string
security_config_account_lockout_instance = SecurityConfigAccountLockout.from_json(json)
# print the JSON string representation of the object
print(SecurityConfigAccountLockout.to_json())

# convert the object into a dict
security_config_account_lockout_dict = security_config_account_lockout_instance.to_dict()
# create an instance of SecurityConfigAccountLockout from a dict
security_config_account_lockout_from_dict = SecurityConfigAccountLockout.from_dict(security_config_account_lockout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


