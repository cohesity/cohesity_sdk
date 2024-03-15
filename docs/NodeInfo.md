# NodeInfo

Specifies general information of a node.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chassis_model** | **str** | Chassis model. | [optional] 
**chassis_serial** | **str** | Chassis serial number programmed by manufacturer. | [optional] 
**cluster_id** | **int** | Specifies the Id of the cluster to which the node belongs. | [optional] 
**cohesity_chassis_serial** | **str** | Chassis serial number programmed by cohesity software. | [optional] 
**cohesity_node_serial** | **str** | Node serial number programmed by cohesity software. | [optional] 
**hostname** | **str** | Host name of the node reported by the kernel. | [optional] 
**incarnation_id** | **int** | Specifies the cluster incarnation Id. | [optional] 
**interface_list** | [**[EndPoint]**](EndPoint.md) | List of interfaces in node. | [optional] 
**ipmi_ip** | **str** | Ipmi IpAddress | [optional] 
**node_id** | **int** | Specifies the Id of the node. | [optional] 
**node_model** | **str** | Node model. | [optional] 
**node_serial** | **str** | Node serial number programmed by manufacturer. | [optional] 
**product_model** | **str** | Product Model | [optional] 
**services_version_info** | [**[ServiceVersionInfo]**](ServiceVersionInfo.md) | Specifies the version information of the cohesity services. | [optional] 
**slot_number** | **str** | Slot number of the node in the chassis. | [optional] 
**software_version** | **str** | Version of the Cohesity software running on the node. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


