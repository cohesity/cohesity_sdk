# NodeGroupRequest

Specifies the request to create a Node Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp_instance** | [**BgpInstance**](BgpInstance.md) |  | [optional] 
**dns_servers_info** | [**DnsServersInfo**](DnsServersInfo.md) |  | [optional] 
**id** | **int** | Id of the node group. | [optional] 
**name** | **str** | Specifies the name of the Node Group. | 
**node_ids** | **List[int]** | List of Node Ids that are part of this node group. | [optional] 
**subnet_info** | [**SubnetInfo**](SubnetInfo.md) |  | [optional] 
**type** | **int** | Type of the node group. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.node_group_request import NodeGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NodeGroupRequest from a JSON string
node_group_request_instance = NodeGroupRequest.from_json(json)
# print the JSON string representation of the object
print(NodeGroupRequest.to_json())

# convert the object into a dict
node_group_request_dict = node_group_request_instance.to_dict()
# create an instance of NodeGroupRequest from a dict
node_group_request_from_dict = NodeGroupRequest.from_dict(node_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


