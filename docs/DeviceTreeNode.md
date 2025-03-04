# DeviceTreeNode

Specifies the tree structure of a logical volume. The leaves are slices of partitions and the other nodes are assemled by combining nodes in some mode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_leaf** | **bool** | Specifies if the node is a leaf node. | [optional] 
**leaf_node_params** | [**DeviceTreeLeafNode**](DeviceTreeLeafNode.md) |  | [optional] 
**non_leaf_node_params** | [**DeviceTreeNonLeafNode**](DeviceTreeNonLeafNode.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.device_tree_node import DeviceTreeNode

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceTreeNode from a JSON string
device_tree_node_instance = DeviceTreeNode.from_json(json)
# print the JSON string representation of the object
print(DeviceTreeNode.to_json())

# convert the object into a dict
device_tree_node_dict = device_tree_node_instance.to_dict()
# create an instance of DeviceTreeNode from a dict
device_tree_node_from_dict = DeviceTreeNode.from_dict(device_tree_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


