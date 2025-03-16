# NfsConfig

Specifies the NFS config settings for this View.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_nfs_kerberos_authentication** | **bool** | If set, it enables NFS Kerberos Authentication | [optional] 
**enable_nfs_kerberos_integrity** | **bool** | If set, it enables NFS Kerberos Integrity | [optional] 
**enable_nfs_kerberos_privacy** | **bool** | If set, it enables NFS Kerberos Privacy | [optional] 
**enable_nfs_unix_authentication** | **bool** | If set, it enables NFS UNIX Authentication | [optional] 
**enable_nfs_view_discovery** | **bool** | If set, it enables discovery of view for NFS. | [optional] 
**enable_nfs_wcc** | **bool** | If set, it enables NFS weak cache consistency. | [optional] 
**nfs_all_squash** | [**NfsSquash**](NfsSquash.md) | Specifies the NFS all squash config. | [optional] 
**nfs_root_permissions** | [**NfsRootPermissions**](NfsRootPermissions.md) | Specifies the NFS root permission config of the view file system. | [optional] 
**nfs_root_squash** | [**NfsSquash**](NfsSquash.md) | Specifies the NFS root squash config. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.nfs_config import NfsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of NfsConfig from a JSON string
nfs_config_instance = NfsConfig.from_json(json)
# print the JSON string representation of the object
print(NfsConfig.to_json())

# convert the object into a dict
nfs_config_dict = nfs_config_instance.to_dict()
# create an instance of NfsConfig from a dict
nfs_config_from_dict = NfsConfig.from_dict(nfs_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


