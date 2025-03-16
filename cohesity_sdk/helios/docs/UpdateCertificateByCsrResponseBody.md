# UpdateCertificateByCsrResponseBody

Specifies the response to update a certificate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | Specifies the certificate. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.update_certificate_by_csr_response_body import UpdateCertificateByCsrResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCertificateByCsrResponseBody from a JSON string
update_certificate_by_csr_response_body_instance = UpdateCertificateByCsrResponseBody.from_json(json)
# print the JSON string representation of the object
print(UpdateCertificateByCsrResponseBody.to_json())

# convert the object into a dict
update_certificate_by_csr_response_body_dict = update_certificate_by_csr_response_body_instance.to_dict()
# create an instance of UpdateCertificateByCsrResponseBody from a dict
update_certificate_by_csr_response_body_from_dict = UpdateCertificateByCsrResponseBody.from_dict(update_certificate_by_csr_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


