# SecurityConfigSessionConfiguration

Specifies configuration for user sessions.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**absolute_timeout** | **int, none_type** | Specifies absolute session expiration time in seconds. | [optional] 
**inactivity_timeout** | **int, none_type** | Specifies inactivity session expiration time in seconds. | [optional] 
**limit_sessions** | **bool, none_type** | Specifies if limitations on number of active sessions is enabled or not. | [optional] 
**session_limit_per_user** | **int, none_type** | Specifies maximum number of active sessions allowed per user. This applies only when limitSessions is enabled. | [optional] 
**session_limit_system_wide** | **int, none_type** | Specifies maximum number of active sessions allowed system wide. This applies only when limitSessions is enabled. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


