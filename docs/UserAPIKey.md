# UserAPIKey

Specifies a user API key instance.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Specifies the unique id of the API key. | [optional] [readonly] 
**name** | **str, none_type** | Specifies the API key name. | [optional] [readonly] 
**is_active** | **bool, none_type** | Specifies if the API key is active. | [optional] [readonly]  if omitted the server will use the default value of True
**is_expired** | **bool, none_type** | Specifies if the API key has expired. | [optional] [readonly] 
**user_sid** | **str, none_type** | Specifies the user who owns the API key. | [optional] [readonly] 
**created_by_user_sid** | **str, none_type** | Specifies the user SID who created the API key. | [optional] [readonly] 
**created_time_msecs** | **int, none_type** | Specifies the time in milliseconds when the API key was created. | [optional] [readonly] 
**last_rotated_time_msecs** | **int, none_type** | Specifies the time in milliseconds when the API key was last rotated. | [optional] [readonly] 
**expiry_time_msecs** | **int, none_type** | Specifies the time in milliseconds when the API key will expire. null signifies no-expiry. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


