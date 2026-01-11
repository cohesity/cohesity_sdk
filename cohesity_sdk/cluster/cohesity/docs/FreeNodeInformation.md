# FreeNodeInformation

Specifies the Metadata of a free Node on the network

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_connect** | **bool, none_type** | Deprecated - This field is deprecated, use connectedTo field. | [optional] 
**chassis_model** | **str, none_type** | Specifies the model number of the Chassis the Node is installed in. | [optional] 
**chassis_serial** | **str, none_type** | Specifies the serial number of the Chassis the Node is installed in. | [optional] 
**connected_to** | **bool, none_type** | Specifies if this is the node from where this API response was received. | [optional] 
**hostname** | **str, none_type** | Specifies the host name of the node. | [optional] 
**id** | **int, none_type** | Specifies the ID of the node. | [optional] 
**ipmi_ip** | **str, none_type** | Specifies the IPMI IP of the Node. | [optional] 
**ips** | **[str], none_type** | List of discovered ipv4/ipv6 addresses of the node. Ip field returns ips as comma separated single string which is incorrect. | [optional] 
**node_model** | **str, none_type** | Specifies the node model. | [optional] 
**node_serial** | **str, none_type** | Specifies the serial number of the Node. | [optional] 
**node_ui_slot** | **str, none_type** | Specifies the position for the UI to display the Node in the Cluster creation page. | [optional] 
**num_slots_in_chassis** | **int, none_type** | Specifies the number of Node slots present in the Chassis where this Node is installed. | [optional] 
**primary_ipv4_address** | **str, none_type** | IPv4 addresses in primary interface&#39;s LAN. | [optional] 
**primary_ipv6_address** | **str, none_type** | IPv6 addresses in primary interface&#39;s LAN. | [optional] 
**product_model** | **str, none_type** | Specifies the product model of the node. | [optional] 
**slot_number** | **str, none_type** | Specifies the number of the slot the Node is installed in. | [optional] 
**software_version** | **str, none_type** | Specifies the version of the software installed on the Node. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


