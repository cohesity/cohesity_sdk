# DeviceTreeNode

Specifies the tree structure of a logical volume. The leaves are slices of partitions and the other nodes are assemled by combining nodes in some mode.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_leaf** | **bool, none_type** | Specifies if the node is a leaf node. | [optional] 
**leaf_node_params** | [**DeviceTreeLeafNode**](DeviceTreeLeafNode.md) |  | [optional] 
**non_leaf_node_params** | [**DeviceTreeNonLeafNode**](DeviceTreeNonLeafNode.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


