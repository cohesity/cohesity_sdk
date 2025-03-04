# FreeNodeInformation

Specifies the Metadata of a free Node on the network

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_connect** | **bool** | Specifies if Node can be connected. | [optional] 
**chassis_serial** | **str** | Specifies the serial number of the Chassis the Node is installed in. | [optional] 
**id** | **int** | Specifies the ID of the node. | [optional] 
**ipmi_ip** | **str** | Specifies the IPMI IP of the Node. | [optional] 
**ips** | **List[str]** | List of discovered ipv4/ipv6 addresses of the node. Ip field returns ips as comma separated single string which is incorrect. | [optional] 
**node_serial** | **str** | Specifies the serial number of the Node. | [optional] 
**node_ui_slot** | **str** | Specifies the position for the UI to display the Node in the Cluster creation page. | [optional] 
**num_slots_in_chassis** | **int** | Specifies the number of Node slots present in the Chassis where this Node is installed. | [optional] 
**product_model** | **str** | Specifies the product model of the node. | [optional] 
**slot_number** | **str** | Specifies the number of the slot the Node is installed in. | [optional] 
**software_version** | **str** | Specifies the version of the software installed on the Node. | [optional] 

## Example

```python
from cohesity_sdk.models.free_node_information import FreeNodeInformation

# TODO update the JSON string below
json = "{}"
# create an instance of FreeNodeInformation from a JSON string
free_node_information_instance = FreeNodeInformation.from_json(json)
# print the JSON string representation of the object
print(FreeNodeInformation.to_json())

# convert the object into a dict
free_node_information_dict = free_node_information_instance.to_dict()
# create an instance of FreeNodeInformation from a dict
free_node_information_from_dict = FreeNodeInformation.from_dict(free_node_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


