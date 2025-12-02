# CertificateStoreListResponse

Specifies a response for environment certificate store APIs returning a list of certificates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificates** | [**List[CertificateObjectWithMetadata]**](CertificateObjectWithMetadata.md) | List of certificate objects. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.certificate_store_list_response import CertificateStoreListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateStoreListResponse from a JSON string
certificate_store_list_response_instance = CertificateStoreListResponse.from_json(json)
# print the JSON string representation of the object
print(CertificateStoreListResponse.to_json())

# convert the object into a dict
certificate_store_list_response_dict = certificate_store_list_response_instance.to_dict()
# create an instance of CertificateStoreListResponse from a dict
certificate_store_list_response_from_dict = CertificateStoreListResponse.from_dict(certificate_store_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


