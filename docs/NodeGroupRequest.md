# NodeGroupRequest

Specifies the request to create a Node Group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the name of the Node Group. | 
**node_ids** | **[int], none_type** | List of Node Ids that are part of this node group. | [optional] 
**id** | **int, none_type** | Id of the node group. | [optional] 
**type** | **int, none_type** | Type of the node group. | [optional] 
**bgp_instance** | [**BgpInstance**](BgpInstance.md) |  | [optional] 
**subnet_info** | [**SubnetInfo**](SubnetInfo.md) |  | [optional] 
**dns_servers_info** | [**DnsServersInfo**](DnsServersInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


