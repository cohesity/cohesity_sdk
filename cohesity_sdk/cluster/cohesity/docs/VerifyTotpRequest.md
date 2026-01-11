# VerifyTotpRequest

Holds the Totp code to be verified.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purpose** | **str, none_type** | Specifies the purpose of the totp code verification. * &#x60;DisableMfa&#x60; - To be used when disabling the MFA. * &#x60;VerifyOtp&#x60; (Default) - To be used when verifying OTP. | [optional] 
**support_user_password** | **str, none_type** | Specifies the support user password, required for totp verification while disabling MFA. | [optional] 
**totp_code** | **str, none_type** | Specifies the Totp code. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


