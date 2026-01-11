# ClusterIpmiLanInfo

Specifies the cluster ipmi lan info for the cluster in which current node is present.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_ipmi_gateway** | **str, none_type** | Specifies the gateway for the given cluster ipmi lan. | [optional] 
**cluster_ipmi_subnet_mask** | **str, none_type** | Specifies the subnet mask for the given cluster ipmi lan. | [optional] 
**node_ipmi_entries** | [**[NodeIpmiInfoEntry], none_type**](NodeIpmiInfoEntry.md) | Specifies the list of node ipmi info for all the nodes in the cluster. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


