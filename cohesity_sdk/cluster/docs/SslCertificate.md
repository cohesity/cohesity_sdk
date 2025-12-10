# SslCertificate

Specifies the certificate and service name of SSL Certificate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | Specifies the certificate in PEM format. | [readonly] 
**last_update_time_msecs** | **int** | Specifies the time when the certificate was updated. | [optional] [readonly] 
**service_name** | **str** | Specifies the service name that uses this SSL certificate. | [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.ssl_certificate import SslCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of SslCertificate from a JSON string
ssl_certificate_instance = SslCertificate.from_json(json)
# print the JSON string representation of the object
print(SslCertificate.to_json())

# convert the object into a dict
ssl_certificate_dict = ssl_certificate_instance.to_dict()
# create an instance of SslCertificate from a dict
ssl_certificate_from_dict = SslCertificate.from_dict(ssl_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


