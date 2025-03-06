# ImportCertificateByClientcsrResponseBody

Specifies the response to import a certificate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_server** | **str** | Specifies the server certificate. | [optional] 
**file_server_cert** | **str** | Specifies the path to the file to be uploaded to server. This file has the server cert, id and encrypted private key | [optional] 
**private_key** | **str** | Specifies the private key of agent. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.import_certificate_by_clientcsr_response_body import ImportCertificateByClientcsrResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of ImportCertificateByClientcsrResponseBody from a JSON string
import_certificate_by_clientcsr_response_body_instance = ImportCertificateByClientcsrResponseBody.from_json(json)
# print the JSON string representation of the object
print(ImportCertificateByClientcsrResponseBody.to_json())

# convert the object into a dict
import_certificate_by_clientcsr_response_body_dict = import_certificate_by_clientcsr_response_body_instance.to_dict()
# create an instance of ImportCertificateByClientcsrResponseBody from a dict
import_certificate_by_clientcsr_response_body_from_dict = ImportCertificateByClientcsrResponseBody.from_dict(import_certificate_by_clientcsr_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


