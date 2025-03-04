# UpdateCertificateByCsrRequest

Specifies the request to update a certificate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | Specifies the certificate to be imported. | 
**csr_id** | **str** | Specifies the id of the csr corresponding to the certificate. | 

## Example

```python
from cohesity_sdk.models.update_certificate_by_csr_request import UpdateCertificateByCsrRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCertificateByCsrRequest from a JSON string
update_certificate_by_csr_request_instance = UpdateCertificateByCsrRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCertificateByCsrRequest.to_json())

# convert the object into a dict
update_certificate_by_csr_request_dict = update_certificate_by_csr_request_instance.to_dict()
# create an instance of UpdateCertificateByCsrRequest from a dict
update_certificate_by_csr_request_from_dict = UpdateCertificateByCsrRequest.from_dict(update_certificate_by_csr_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


