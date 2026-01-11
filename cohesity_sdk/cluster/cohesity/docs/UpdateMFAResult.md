# UpdateMFAResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_name** | **str** | Specifies the TOTP account name to be configured for support user. | [optional] 
**totp_secret_key** | **str** | Specifies the TOTP secret key. | [optional] 
**totp_uri** | **str** | Specifies the TOTP key URI for generating MFA QR code. | [optional] 
**current_password** | **str, none_type** | Specifies the current password of the support user, required for making updates to the configuration. | [optional] 
**email** | **str, none_type** | This field is deprecated, use PUT /v2/support-user/mfa. Specifies email address of the support user. Used when MFA mode is email. | [optional] 
**enabled** | **bool** | Specifies whether MFA is enabled for support user. | [optional]  if omitted the server will use the default value of False
**is_quorum_managed** | **bool, none_type** | Specifies whether the MFA configuration is managed by quorum. | [optional] [readonly]  if omitted the server will use the default value of False
**mfa_code** | **str, none_type** | MFA code that needs to be passed when disabling MFA or changing email address when email based MFA is configured. | [optional] 
**mfa_type** | **str, none_type** | This field is deprecated, use PUT /v2/support-user/mfa. Specifies the mechanism to receive the OTP code. | [optional] 
**otp_verification_state** | **str, none_type** | Specifies the status of otp verification. | [optional] 
**reference_id** | **str, none_type** | Specifies a reference ID of OTP verification, required if mfaCode is not specified | [optional] 
**requires_password_auth** | **bool** | Specifies that this API requires current support user password for enabling/disabling MFA, and for updating mfaType and email. | [optional] [readonly]  if omitted the server will use the default value of True
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


