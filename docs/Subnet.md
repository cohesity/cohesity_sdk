# Subnet

Defines a Subnet (Subnetwork). The netmask can be specified by setting netmaskBits or netmaskIp4. The netmask can only be set using netmaskIp4 if the IP address is an IPv4 address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** | Component that has reserved the subnet. | [optional] 
**description** | **str** | Description of the subnet. | [optional] 
**gateway** | **str** | Gateway for the subnet. | [optional] 
**id** | **int** | ID of the subnet. | [optional] 
**ip** | **str** | Specifies either an IPv6 address or an IPv4 address. | [optional] 
**netmask_bits** | **int** | Specifies the netmask using bits. | [optional] 
**netmask_ip4** | **str** | Specifies the netmask using an IP4 address. The netmask can only be set using netmaskIp4 if the IP address is an IPv4 address. | [optional] 
**nfs_access** | **str** | Specifies whether clients from this subnet can mount using NFS protocol. Protocol access level. &#39;kDisabled&#39; indicates Protocol access level &#39;Disabled&#39; &#39;kReadOnly&#39; indicates Protocol access level &#39;ReadOnly&#39; &#39;kReadWrite&#39; indicates Protocol access level &#39;ReadWrite&#39; | [optional] 
**nfs_squash** | **str** | Specifies which nfsSquash Mounted. &#39;kNone&#39; mounts none. &#39;kRootSquash&#39; mounts nfsRootSquash. Whether clients from this subnet can mount as root on NFS. &#39;kAllSquash&#39; mounts nfsAllSquash. Whether all clients from this subnet can map view with view_all_squash_uid/view_all_squash_gid configured in the view. | [optional] 
**s3_access** | **str** | Specifies whether clients from this subnet can access using S3 protocol. Protocol access level. &#39;kDisabled&#39; indicates Protocol access level &#39;Disabled&#39; &#39;kReadOnly&#39; indicates Protocol access level &#39;ReadOnly&#39; &#39;kReadWrite&#39; indicates Protocol access level &#39;ReadWrite&#39; | [optional] 
**smb_access** | **str** | Specifies whether clients from this subnet can mount using SMB protocol. Protocol access level. &#39;kDisabled&#39; indicates Protocol access level &#39;Disabled&#39; &#39;kReadOnly&#39; indicates Protocol access level &#39;ReadOnly&#39; &#39;kReadWrite&#39; indicates Protocol access level &#39;ReadWrite&#39; | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.subnet import Subnet

# TODO update the JSON string below
json = "{}"
# create an instance of Subnet from a JSON string
subnet_instance = Subnet.from_json(json)
# print the JSON string representation of the object
print(Subnet.to_json())

# convert the object into a dict
subnet_dict = subnet_instance.to_dict()
# create an instance of Subnet from a dict
subnet_from_dict = Subnet.from_dict(subnet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


