# NodeServicesStates

Lists node services states

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str, none_type** | Specifies an optional message describing details of the cluster services states. | [optional] 
**node_id** | **int, none_type** | Specifies the id of the node. | [optional] 
**node_ips** | **[str], none_type** | If the node is not part of any cluster, it returns list of local IPs; otherwise it returns the local IP that matches the cluster subnet. | [optional] 
**node_sw_version** | **str, none_type** | Node Software Version | [optional] 
**part_of_cluster** | **bool, none_type** | Specifies weather node is part of a cluster  | [optional] 
**services_state** | [**[ServiceState], none_type**](ServiceState.md) | Contains node services states | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


