# SecurityConfigAccountLockout

Specifies security config for account lockout.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed_login_lock_time_duration_mins** | **int, none_type** | Specifies the time duration within which the consecutive failed login attempts causes a local user account to be locked and the lockout duration time due to that. | [optional] 
**inactivity_time_days** | **int, none_type** | Specifies the lockout inactivity time range in days. | [optional] 
**max_failed_login_attempts** | **int, none_type** | Specifies the maximum number of consecutive fail login attempts. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


