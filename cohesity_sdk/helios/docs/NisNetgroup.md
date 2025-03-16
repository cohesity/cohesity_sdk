# NisNetgroup

Specifies an NIS netgroup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Specifies the domain name for the netgroup. | 
**name** | **str** | Specifies the netgroup name. | 
**nfs_access** | **str** | Specifies NFS protocol acess level for clients from the netgroup. | [optional] 
**nfs_squash** | **str** | Specifies which nfsSquash Mounted. &#39;kNone&#39; mounts none. &#39;kRootSquash&#39; mounts nfsRootSquash. Whether clients from this subnet can mount as root on NFS. &#39;kAllSquash&#39; mounts nfsAllSquash. Whether all clients from this subnet can map view with view_all_squash_uid/view_all_squash_gid configured in the view. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.nis_netgroup import NisNetgroup

# TODO update the JSON string below
json = "{}"
# create an instance of NisNetgroup from a JSON string
nis_netgroup_instance = NisNetgroup.from_json(json)
# print the JSON string representation of the object
print(NisNetgroup.to_json())

# convert the object into a dict
nis_netgroup_dict = nis_netgroup_instance.to_dict()
# create an instance of NisNetgroup from a dict
nis_netgroup_from_dict = NisNetgroup.from_dict(nis_netgroup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


