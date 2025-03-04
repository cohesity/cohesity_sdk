# DeviceTreeLeafNode

Specifies the parameters of a leaf node in device tree.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_name** | **str** | Specifies the disk name. | [optional] 
**length_bytes** | **int** | Specifies The length of data in bytes for the LVM volume (for which this device tree is being built). It does not include size of the LVM meta data. | [optional] 
**offset_bytes** | **int** | Specifies the offset in bytes where data for the LVM volume (for which this device tree is being build) starts relative to the start of the partition. | [optional] 
**partition_number** | **int** | Specifies the paritition number. | [optional] 

## Example

```python
from cohesity_sdk.models.device_tree_leaf_node import DeviceTreeLeafNode

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceTreeLeafNode from a JSON string
device_tree_leaf_node_instance = DeviceTreeLeafNode.from_json(json)
# print the JSON string representation of the object
print(DeviceTreeLeafNode.to_json())

# convert the object into a dict
device_tree_leaf_node_dict = device_tree_leaf_node_instance.to_dict()
# create an instance of DeviceTreeLeafNode from a dict
device_tree_leaf_node_from_dict = DeviceTreeLeafNode.from_dict(device_tree_leaf_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


