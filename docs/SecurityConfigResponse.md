# SecurityConfigResponse

Specifies the detail response the security config.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password_strength** | [**SecurityConfigPasswordStrength**](SecurityConfigPasswordStrength.md) |  | [optional] 
**password_reuse** | [**SecurityConfigPasswordReuse**](SecurityConfigPasswordReuse.md) |  | [optional] 
**password_lifetime** | [**SecurityConfigPasswordLifetime**](SecurityConfigPasswordLifetime.md) |  | [optional] 
**account_lockout** | [**SecurityConfigAccountLockout**](SecurityConfigAccountLockout.md) |  | [optional] 
**data_classification** | [**SecurityConfigDataClassification**](SecurityConfigDataClassification.md) |  | [optional] 
**session_configuration** | [**SecurityConfigSessionConfiguration**](SecurityConfigSessionConfiguration.md) |  | [optional] 
**certificate_based_auth** | [**SecurityConfigCertificateBasedAuth**](SecurityConfigCertificateBasedAuth.md) |  | [optional] 
**auth_token_timeout_minutes** | **int, none_type** | Specifies the authentication token timeout in minutes. Applies both for API based access token and browser login cookie. | [optional] 
**inactivity_timeout_m_secs** | **int, none_type** | Specifies the UI inactivity timeout in milliseconds. Default value is 30 minutes. | [optional] 
**ssh_configuration** | [**SecurityConfigSshConfiguration**](SecurityConfigSshConfiguration.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


