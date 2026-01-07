# MfaConfigInfo

Holds the MFA configuration to be returned or stored.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_types** | **[str], none_type** | Specifies the list of mechanism to receive the OTP code. | [optional] 
**enabled** | **bool** | Specifies whether MFA is enabled on a cluster level. | [optional]  if omitted the server will use the default value of False
**retain_user_mfa_settings** | **bool, none_type** | Specifies whether user MFA setting needs to be retained. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


