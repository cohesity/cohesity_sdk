# SecurityConfigCertificateBasedAuth

Specifies security config for certificate based authentication.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_mapping** | **str** | Specifies the field to be used in AD user for authentication. | [optional] 
**certificate_mapping** | **str** | Specifies the field to be used in certificate for authentication. | [optional] 
**enable_mapping_based_authentication** | **bool** | If true, certfication based authentication is done via configured mapping. Else it will proceed based on legacy serial number match. | [optional] 

## Example

```python
from cohesity_sdk.models.security_config_certificate_based_auth import SecurityConfigCertificateBasedAuth

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityConfigCertificateBasedAuth from a JSON string
security_config_certificate_based_auth_instance = SecurityConfigCertificateBasedAuth.from_json(json)
# print the JSON string representation of the object
print(SecurityConfigCertificateBasedAuth.to_json())

# convert the object into a dict
security_config_certificate_based_auth_dict = security_config_certificate_based_auth_instance.to_dict()
# create an instance of SecurityConfigCertificateBasedAuth from a dict
security_config_certificate_based_auth_from_dict = SecurityConfigCertificateBasedAuth.from_dict(security_config_certificate_based_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


