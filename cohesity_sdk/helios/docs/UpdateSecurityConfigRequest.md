# UpdateSecurityConfigRequest

Specifies the request params for updating the security config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_lockout** | [**SecurityConfigAccountLockout**](SecurityConfigAccountLockout.md) |  | [optional] 
**auth_token_timeout_minutes** | **int** | Specifies the authentication token timeout in minutes. Applies both for API based access token and browser login cookie. | [optional] 
**certificate_based_auth** | [**SecurityConfigCertificateBasedAuth**](SecurityConfigCertificateBasedAuth.md) |  | [optional] 
**data_classification** | [**SecurityConfigDataClassification**](SecurityConfigDataClassification.md) |  | [optional] 
**inactivity_timeout_m_secs** | **int** | Specifies the UI inactivity timeout in milliseconds. Default value is 30 minutes. | [optional] 
**password_lifetime** | [**SecurityConfigPasswordLifetime**](SecurityConfigPasswordLifetime.md) |  | [optional] 
**password_reuse** | [**SecurityConfigPasswordReuse**](SecurityConfigPasswordReuse.md) |  | [optional] 
**password_strength** | [**SecurityConfigPasswordStrength**](SecurityConfigPasswordStrength.md) |  | [optional] 
**session_configuration** | [**SecurityConfigSessionConfiguration**](SecurityConfigSessionConfiguration.md) |  | [optional] 
**ssh_configuration** | [**SecurityConfigSshConfiguration**](SecurityConfigSshConfiguration.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.update_security_config_request import UpdateSecurityConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSecurityConfigRequest from a JSON string
update_security_config_request_instance = UpdateSecurityConfigRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSecurityConfigRequest.to_json())

# convert the object into a dict
update_security_config_request_dict = update_security_config_request_instance.to_dict()
# create an instance of UpdateSecurityConfigRequest from a dict
update_security_config_request_from_dict = UpdateSecurityConfigRequest.from_dict(update_security_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


