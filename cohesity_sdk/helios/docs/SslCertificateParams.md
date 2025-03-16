# SslCertificateParams

Specifies the parameters of an SSL Certificate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssl_certificate** | **str** | Specifies an SSL Certificate. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.ssl_certificate_params import SslCertificateParams

# TODO update the JSON string below
json = "{}"
# create an instance of SslCertificateParams from a JSON string
ssl_certificate_params_instance = SslCertificateParams.from_json(json)
# print the JSON string representation of the object
print(SslCertificateParams.to_json())

# convert the object into a dict
ssl_certificate_params_dict = ssl_certificate_params_instance.to_dict()
# create an instance of SslCertificateParams from a dict
ssl_certificate_params_from_dict = SslCertificateParams.from_dict(ssl_certificate_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


