# KmsAuthMetadata

Specifies the authentication metadata for fetching Key Management Service (KMS) from external provider.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trusted_profile_id** | **str** | Specifies the trusted profile ID for fetching KMS information. This ID will be used during multiple API calls made to the external Key management service (KMS). | 

## Example

```python
from cohesity_sdk.cluster.models.kms_auth_metadata import KmsAuthMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of KmsAuthMetadata from a JSON string
kms_auth_metadata_instance = KmsAuthMetadata.from_json(json)
# print the JSON string representation of the object
print(KmsAuthMetadata.to_json())

# convert the object into a dict
kms_auth_metadata_dict = kms_auth_metadata_instance.to_dict()
# create an instance of KmsAuthMetadata from a dict
kms_auth_metadata_from_dict = KmsAuthMetadata.from_dict(kms_auth_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


