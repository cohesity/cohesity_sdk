# CreateOrUpdateAPIKeyRequest

Specified the request to create a new user API key.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the API key name. | 
**expiry_time_msecs** | **int, none_type** | Specifies the time in milliseconds when the API key will expire. Set null for no expiry. | [optional] 
**is_active** | **bool, none_type** | Specifies if the API key is active. | [optional]  if omitted the server will use the default value of True

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


