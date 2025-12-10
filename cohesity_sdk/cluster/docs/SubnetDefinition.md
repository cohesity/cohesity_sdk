# SubnetDefinition

Defines a Subnet (Subnetwork). The netmask can be specified by setting netmaskBits or netmaskIp4. The netmask can only be set using netmaskIp4 if the IP address is an IPv4 address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** | Component that has reserved the subnet. | [optional] 
**description** | **str** | Description of the subnet. | [optional] 
**id** | **int** | ID of the subnet. | [optional] 
**ip** | **str** | Specifies either an IPv6 address or an IPv4 address. | [optional] 
**netmask_bits** | **int** | Specifies the netmask using bits. | [optional] 
**netmask_ip4** | **str** | Specifies the netmask using an IP4 address. The netmask can only be set using netmaskIp4 if the IP address is an IPv4 address. | [optional] 
**nfs_access** | **str** | Specifies whether clients from this subnet can mount using NFS protocol. Protocol access level. &#39;kDisabled&#39; indicates Protocol access level &#39;Disabled&#39; &#39;kReadOnly&#39; indicates Protocol access level &#39;ReadOnly&#39; &#39;kReadWrite&#39; indicates Protocol access level &#39;ReadWrite&#39; | [optional] 
**nfs_all_squash** | **bool** | Specifies whether all clients from this subnet can map view with view_all_squash_uid/view_all_squash_gid configured in the view. | [optional] 
**nfs_root_squash** | **bool** | Specifies whether clients from this subnet can mount as root on NFS. | [optional] 
**s3_access** | **object** | Specifies whether clients from this subnet can access using S3 protocol. Protocol access level. &#39;kDisabled&#39; indicates Protocol access level &#39;Disabled&#39; &#39;kReadOnly&#39; indicates Protocol access level &#39;ReadOnly&#39; &#39;kReadWrite&#39; indicates Protocol access level &#39;ReadWrite&#39; | [optional] 
**smb_access** | **str** | Specifies whether clients from this subnet can mount using SMB protocol. Protocol access level. &#39;kDisabled&#39; indicates Protocol access level &#39;Disabled&#39; &#39;kReadOnly&#39; indicates Protocol access level &#39;ReadOnly&#39; &#39;kReadWrite&#39; indicates Protocol access level &#39;ReadWrite&#39; | [optional] 
**tenant_id** | **str** | Specifies the unique id of the tenant. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.subnet_definition import SubnetDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of SubnetDefinition from a JSON string
subnet_definition_instance = SubnetDefinition.from_json(json)
# print the JSON string representation of the object
print(SubnetDefinition.to_json())

# convert the object into a dict
subnet_definition_dict = subnet_definition_instance.to_dict()
# create an instance of SubnetDefinition from a dict
subnet_definition_from_dict = SubnetDefinition.from_dict(subnet_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


