# NodeIpmiInfoEntry

Specifies the ipmi info for each node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_ip** | **str** | Specifies the ip address of the node. | [optional] 
**node_ipmi_gateway** | **str** | Specifies the gateway for the given node ipmi. | [optional] 
**node_ipmi_ip** | **str** | Specifies the ipmi ip address of the node. | [optional] 
**node_ipmi_subnet_mask** | **str** | Specifies the subnet mask for the given node ipmi. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.node_ipmi_info_entry import NodeIpmiInfoEntry

# TODO update the JSON string below
json = "{}"
# create an instance of NodeIpmiInfoEntry from a JSON string
node_ipmi_info_entry_instance = NodeIpmiInfoEntry.from_json(json)
# print the JSON string representation of the object
print(NodeIpmiInfoEntry.to_json())

# convert the object into a dict
node_ipmi_info_entry_dict = node_ipmi_info_entry_instance.to_dict()
# create an instance of NodeIpmiInfoEntry from a dict
node_ipmi_info_entry_from_dict = NodeIpmiInfoEntry.from_dict(node_ipmi_info_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


