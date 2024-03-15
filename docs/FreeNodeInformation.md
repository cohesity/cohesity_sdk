# FreeNodeInformation

Specifies the Metadata of a free Node on the network

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_connect** | **bool, none_type** | Specifies if Node can be connected. | [optional] 
**chassis_serial** | **str, none_type** | Specifies the serial number of the Chassis the Node is installed in. | [optional] 
**id** | **int, none_type** | Specifies the ID of the node. | [optional] 
**ipmi_ip** | **str, none_type** | Specifies the IPMI IP of the Node. | [optional] 
**ips** | **[str], none_type** | List of discovered ipv4/ipv6 addresses of the node. Ip field returns ips as comma separated single string which is incorrect. | [optional] 
**node_serial** | **str, none_type** | Specifies the serial number of the Node. | [optional] 
**node_ui_slot** | **str, none_type** | Specifies the position for the UI to display the Node in the Cluster creation page. | [optional] 
**num_slots_in_chassis** | **int, none_type** | Specifies the number of Node slots present in the Chassis where this Node is installed. | [optional] 
**product_model** | **str, none_type** | Specifies the product model of the node. | [optional] 
**slot_number** | **str, none_type** | Specifies the number of the slot the Node is installed in. | [optional] 
**software_version** | **str, none_type** | Specifies the version of the software installed on the Node. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


