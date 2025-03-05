# ImportCertificateByClientcsrRequest

Specifies the request to import a certificate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_client** | **str** | Specifies the client certificate to be imported. | 
**certificate_server** | **str** | Specifies the server certificate to be imported. | 

## Example

```python
from cohesity_sdk.models.import_certificate_by_clientcsr_request import ImportCertificateByClientcsrRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportCertificateByClientcsrRequest from a JSON string
import_certificate_by_clientcsr_request_instance = ImportCertificateByClientcsrRequest.from_json(json)
# print the JSON string representation of the object
print(ImportCertificateByClientcsrRequest.to_json())

# convert the object into a dict
import_certificate_by_clientcsr_request_dict = import_certificate_by_clientcsr_request_instance.to_dict()
# create an instance of ImportCertificateByClientcsrRequest from a dict
import_certificate_by_clientcsr_request_from_dict = ImportCertificateByClientcsrRequest.from_dict(import_certificate_by_clientcsr_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


