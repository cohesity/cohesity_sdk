# ExternalTargetAuthMetadata

Specifies the authentication metadata for fetching external target information from external provider.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trusted_profile_id** | **str** | Specifies the trusted profile ID for fetching external targets. This ID will be used during multiple API calls made to the external target service. | 

## Example

```python
from cohesity_sdk.cluster.models.external_target_auth_metadata import ExternalTargetAuthMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalTargetAuthMetadata from a JSON string
external_target_auth_metadata_instance = ExternalTargetAuthMetadata.from_json(json)
# print the JSON string representation of the object
print(ExternalTargetAuthMetadata.to_json())

# convert the object into a dict
external_target_auth_metadata_dict = external_target_auth_metadata_instance.to_dict()
# create an instance of ExternalTargetAuthMetadata from a dict
external_target_auth_metadata_from_dict = ExternalTargetAuthMetadata.from_dict(external_target_auth_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


