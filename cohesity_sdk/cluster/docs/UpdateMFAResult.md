# UpdateMFAResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_name** | **str** | Specifies the TOTP account name to be configured for support user. | [optional] 
**totp_secret_key** | **str** | Specifies the TOTP secret key. | [optional] 
**totp_uri** | **str** | Specifies the TOTP key URI for generating MFA QR code. | [optional] 
**email** | **str, none_type** | Specifies email address of the support user. Used when MFA mode is email. | [optional] 
**enabled** | **bool** | Specifies whether MFA is enabled for support user. | [optional]  if omitted the server will use the default value of False
**mfa_code** | **str, none_type** | MFA code that needs to be passed when disabling MFA or changing email address when email based MFA is configured. | [optional] 
**mfa_type** | **str, none_type** | Specifies the mechanism to receive the OTP code. | [optional] 
**otp_verification_state** | **str, none_type** | Specifies the status of otp verification. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


