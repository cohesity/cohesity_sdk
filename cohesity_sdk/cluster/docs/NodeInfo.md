# NodeInfo

Specifies general information of a node.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chassis_model** | **str** | Chassis model. | 
**chassis_serial** | **str** | Chassis serial number programmed by manufacturer. | 
**cluster_id** | **int** | Specifies the Id of the cluster to which the node belongs. | 
**cohesity_chassis_serial** | **str** | Chassis serial number programmed by cohesity software. | 
**cohesity_node_serial** | **str** | Node serial number programmed by cohesity software. | 
**cpu** | **int** | Number of CPUs | 
**hostname** | **str** | Host name of the node reported by the kernel. | 
**incarnation_id** | **int** | Specifies the cluster incarnation Id. | 
**ipmi_ip** | **str** | Ipmi IpAddress | 
**is_node_reachable** | **bool** | Specifies whether the node is reachable or not | 
**node_id** | **int** | Specifies the Id of the node. | 
**node_model** | **str** | Node model. | 
**node_serial** | **str** | Node serial number programmed by manufacturer. | 
**product_model** | **str** | Product Model | 
**services_version_info** | [**[ServiceVersionInfo]**](ServiceVersionInfo.md) | Specifies the version information of the cohesity services. | 
**slot_number** | **str** | Slot number of the node in the chassis. | 
**software_version** | **str** | Version of the Cohesity software running on the node. | 
**system_memory_bytes** | **int** | System Memory in bytes | 
**interface_list** | [**[EndPoint]**](EndPoint.md) | List of interfaces in node. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


