# DeviceTreeNonLeafNode

Specifies the parameters of a non leaf node in device tree.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children_nodes** | [**List[DeviceTreeNode]**](DeviceTreeNode.md) | Specifies a list of children nodes. | [optional] 
**device_id** | **int** | Specifies the id of device. | [optional] 
**device_length** | **int** | Specifies the length of device. | [optional] 
**type** | **str** | Specifies the children nodes combine type. | [optional] 

## Example

```python
from cohesity_sdk.models.device_tree_non_leaf_node import DeviceTreeNonLeafNode

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceTreeNonLeafNode from a JSON string
device_tree_non_leaf_node_instance = DeviceTreeNonLeafNode.from_json(json)
# print the JSON string representation of the object
print(DeviceTreeNonLeafNode.to_json())

# convert the object into a dict
device_tree_non_leaf_node_dict = device_tree_non_leaf_node_instance.to_dict()
# create an instance of DeviceTreeNonLeafNode from a dict
device_tree_non_leaf_node_from_dict = DeviceTreeNonLeafNode.from_dict(device_tree_non_leaf_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


