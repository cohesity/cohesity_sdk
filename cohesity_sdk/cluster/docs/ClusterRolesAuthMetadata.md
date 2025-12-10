# ClusterRolesAuthMetadata

Specifies the authentication metadata for fetching roles from external provider.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trusted_profile_id** | **str** | Specifies the trusted profile ID for fetching roles. This ID will be used during multiple API calls made to the external identity management service. | 

## Example

```python
from cohesity_sdk.cluster.models.cluster_roles_auth_metadata import ClusterRolesAuthMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterRolesAuthMetadata from a JSON string
cluster_roles_auth_metadata_instance = ClusterRolesAuthMetadata.from_json(json)
# print the JSON string representation of the object
print(ClusterRolesAuthMetadata.to_json())

# convert the object into a dict
cluster_roles_auth_metadata_dict = cluster_roles_auth_metadata_instance.to_dict()
# create an instance of ClusterRolesAuthMetadata from a dict
cluster_roles_auth_metadata_from_dict = ClusterRolesAuthMetadata.from_dict(cluster_roles_auth_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


