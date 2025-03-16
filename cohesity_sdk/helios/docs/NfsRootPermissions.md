# NfsRootPermissions

Specifies the config of NFS root permission of a view file system.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **int** | Unix GID for the root of the file system. | [optional] 
**mode** | **int** | Unix mode bits for the root of the file system. | [optional] 
**uid** | **int** | Unix UID for the root of the file system. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.nfs_root_permissions import NfsRootPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of NfsRootPermissions from a JSON string
nfs_root_permissions_instance = NfsRootPermissions.from_json(json)
# print the JSON string representation of the object
print(NfsRootPermissions.to_json())

# convert the object into a dict
nfs_root_permissions_dict = nfs_root_permissions_instance.to_dict()
# create an instance of NfsRootPermissions from a dict
nfs_root_permissions_from_dict = NfsRootPermissions.from_dict(nfs_root_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


