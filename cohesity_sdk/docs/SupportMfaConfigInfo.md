# SupportMfaConfigInfo

Holds the MFA configuration to be returned or stored.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str, none_type** | Specifies email address of the support user. Used when MFA mode is email. | [optional] 
**enabled** | **bool** | Specifies whether MFA is enabled for support user. | [optional]  if omitted the server will use the default value of False
**mfa_code** | **str, none_type** | MFA code that needs to be passed when disabling MFA or changing email address when email based MFA is configured. | [optional] 
**mfa_type** | **str, none_type** | Specifies the mechanism to receive the OTP code. | [optional] 
**otp_verification_state** | **str, none_type** | Specifies the status of otp verification. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


