# NodeNetworkInterfaces

Interfaces on a node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chassis_serial_number** | **str** | Chassis serial number. | [optional] 
**interfaces** | [**List[Interface]**](Interface.md) | List of interfaces on the node. | [optional] 
**node_id** | **int** | Id of the node. | [optional] 
**slot** | **int** | Slot number of the node. | [optional] 

## Example

```python
from cohesity_sdk.models.node_network_interfaces import NodeNetworkInterfaces

# TODO update the JSON string below
json = "{}"
# create an instance of NodeNetworkInterfaces from a JSON string
node_network_interfaces_instance = NodeNetworkInterfaces.from_json(json)
# print the JSON string representation of the object
print(NodeNetworkInterfaces.to_json())

# convert the object into a dict
node_network_interfaces_dict = node_network_interfaces_instance.to_dict()
# create an instance of NodeNetworkInterfaces from a dict
node_network_interfaces_from_dict = NodeNetworkInterfaces.from_dict(node_network_interfaces_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


