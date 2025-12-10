# MutableCertificateMetadata

Specifies the fields of a certicate metadata, which can be updated via update certificate request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Display name of the certificate. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.mutable_certificate_metadata import MutableCertificateMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of MutableCertificateMetadata from a JSON string
mutable_certificate_metadata_instance = MutableCertificateMetadata.from_json(json)
# print the JSON string representation of the object
print(MutableCertificateMetadata.to_json())

# convert the object into a dict
mutable_certificate_metadata_dict = mutable_certificate_metadata_instance.to_dict()
# create an instance of MutableCertificateMetadata from a dict
mutable_certificate_metadata_from_dict = MutableCertificateMetadata.from_dict(mutable_certificate_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


