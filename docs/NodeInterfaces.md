# NodeInterfaces

Specifies the interfaces present on a Node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the node. | [optional] 
**interfaces** | [**List[NetworkInterface]**](NetworkInterface.md) | Specifies the list of network interfaces present on this Node. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.node_interfaces import NodeInterfaces

# TODO update the JSON string below
json = "{}"
# create an instance of NodeInterfaces from a JSON string
node_interfaces_instance = NodeInterfaces.from_json(json)
# print the JSON string representation of the object
print(NodeInterfaces.to_json())

# convert the object into a dict
node_interfaces_dict = node_interfaces_instance.to_dict()
# create an instance of NodeInterfaces from a dict
node_interfaces_from_dict = NodeInterfaces.from_dict(node_interfaces_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


