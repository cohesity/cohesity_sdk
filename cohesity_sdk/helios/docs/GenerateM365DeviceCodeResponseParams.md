# GenerateM365DeviceCodeResponseParams

Specifies the response containing the user and device codes along with the verification URI needed for Device Authorization grant.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_code** | **str, none_type** | Specifies the string used to verify the session between the client and the authorization server. The client uses this parameter to request the access token from the authorization server. | [optional] 
**user_code** | **str, none_type** | A short string shown to the user that&#39;s used to identify the session on a secondary device. | [optional] 
**verification_uri** | **str, none_type** | The URI the user should go to with the userCode in order to sign in. | [optional] 
**expires_in_secs** | **int, none_type** | The number of seconds before the deviceCode and userCode expire. | [optional] 
**interval_secs** | **int, none_type** | The number of seconds the client should wait between polling requests to check for token. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


