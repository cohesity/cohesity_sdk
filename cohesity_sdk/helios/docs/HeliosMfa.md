# HeliosMfa

Specifies MFA configuration for an account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mfa** | **bool, none_type** | Specifies whether MFA is enabled or disabled. | 
**authentication_types** | **[str], none_type** | Specifies the list of mechanism to receive the OTP code. Supported types are:   TOTP (Helios OnPrem Only) -&gt; Time based OTP.   Email OTP (Helios OnPrem Only) -&gt; OTP via Email.   Salesforce (Helios Only) -&gt; MFA setup via Salesforce.  | [optional] 
**retain_user_mfa_settings** | **bool, none_type** | Specifies whether user level MFA config needs to be retained when account level MFA is enabled or disabled. | [optional]  if omitted the server will use the default value of False

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


