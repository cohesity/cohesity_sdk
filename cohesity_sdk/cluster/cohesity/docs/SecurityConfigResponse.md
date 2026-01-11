# SecurityConfigResponse

Specifies the detail response the security config.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_lockout** | [**SecurityConfigAccountLockout**](SecurityConfigAccountLockout.md) |  | [optional] 
**auth_token_timeout_minutes** | **int, none_type** | Specifies the authentication token timeout in minutes. Applies both for API based access token and browser login cookie. | [optional] 
**certificate_based_auth** | [**SecurityConfigCertificateBasedAuth**](SecurityConfigCertificateBasedAuth.md) |  | [optional] 
**data_classification** | [**SecurityConfigDataClassification**](SecurityConfigDataClassification.md) |  | [optional] 
**inactivity_timeout_m_secs** | **int, none_type** | Specifies the UI inactivity timeout in milliseconds. Default value is 30 minutes. | [optional] 
**password_lifetime** | [**SecurityConfigPasswordLifetime**](SecurityConfigPasswordLifetime.md) |  | [optional] 
**password_reuse** | [**SecurityConfigPasswordReuse**](SecurityConfigPasswordReuse.md) |  | [optional] 
**password_strength** | [**SecurityConfigPasswordStrength**](SecurityConfigPasswordStrength.md) |  | [optional] 
**session_configuration** | [**SecurityConfigSessionConfiguration**](SecurityConfigSessionConfiguration.md) |  | [optional] 
**ssh_configuration** | [**SecurityConfigSshConfiguration**](SecurityConfigSshConfiguration.md) |  | [optional] 
**session_management_enabled** | **bool, none_type** | Specifies whether session management is enabled.  When true, sessionConfiguration from SecurityConfig will be used for for managing user sessions. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


