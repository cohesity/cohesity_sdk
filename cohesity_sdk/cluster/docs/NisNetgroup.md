# NisNetgroup

Specifies an NIS netgroup.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str, none_type** | Specifies the domain name for the netgroup. | 
**name** | **str, none_type** | Specifies the netgroup name. | 
**nfs_access** | **str, none_type** | Specifies NFS protocol acess level for clients from the netgroup. | [optional] 
**nfs_squash** | **str, none_type** | Specifies which nfsSquash Mounted. &#39;kNone&#39; mounts none. &#39;kRootSquash&#39; mounts nfsRootSquash. Whether clients from this subnet can mount as root on NFS. &#39;kAllSquash&#39; mounts nfsAllSquash. Whether all clients from this subnet can map view with view_all_squash_uid/view_all_squash_gid configured in the view. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


