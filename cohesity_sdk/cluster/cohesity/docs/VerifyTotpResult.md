# VerifyTotpResult

Result of verifying totp code for support user.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str, none_type** | Specifies message of otp verification result. | [optional] 
**reference_id** | **str, none_type** | Specifies the reference id of the otp verification request. Generated when TOTP is verified for disabling MFA. | [optional] 
**success** | **bool** | Specifies whether or not verification of totp code is success. | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


