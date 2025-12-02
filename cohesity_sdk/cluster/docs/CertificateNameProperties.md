# CertificateNameProperties

Specifies the name (subject or issuer) properties of a certificate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_name** | **str** | Common Name (CN) of the certificate. | [optional] 
**organization** | **str** | Organization (O) name of the certificate. | [optional] 
**organization_unit** | **str** | Organization unit (OU) of the certificate. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.certificate_name_properties import CertificateNameProperties

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateNameProperties from a JSON string
certificate_name_properties_instance = CertificateNameProperties.from_json(json)
# print the JSON string representation of the object
print(CertificateNameProperties.to_json())

# convert the object into a dict
certificate_name_properties_dict = certificate_name_properties_instance.to_dict()
# create an instance of CertificateNameProperties from a dict
certificate_name_properties_from_dict = CertificateNameProperties.from_dict(certificate_name_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


