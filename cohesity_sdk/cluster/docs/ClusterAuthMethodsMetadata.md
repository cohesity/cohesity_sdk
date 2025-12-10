# ClusterAuthMethodsMetadata

Specifies the metadata for various authentication methods that can be used to validate the cluster access.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_target_authentication** | [**ExternalTargetAuthMetadata**](ExternalTargetAuthMetadata.md) |  | [optional] 
**fetch_roles_authentication** | [**ClusterRolesAuthMetadata**](ClusterRolesAuthMetadata.md) |  | 
**kms_authentication** | [**KmsAuthMetadata**](KmsAuthMetadata.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_auth_methods_metadata import ClusterAuthMethodsMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAuthMethodsMetadata from a JSON string
cluster_auth_methods_metadata_instance = ClusterAuthMethodsMetadata.from_json(json)
# print the JSON string representation of the object
print(ClusterAuthMethodsMetadata.to_json())

# convert the object into a dict
cluster_auth_methods_metadata_dict = cluster_auth_methods_metadata_instance.to_dict()
# create an instance of ClusterAuthMethodsMetadata from a dict
cluster_auth_methods_metadata_from_dict = ClusterAuthMethodsMetadata.from_dict(cluster_auth_methods_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


