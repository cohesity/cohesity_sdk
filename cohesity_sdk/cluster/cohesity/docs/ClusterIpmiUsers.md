# ClusterIpmiUsers

Specifies the  cluster level IPMI user name and the list of node level IPMI user names..

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_ipmi_username** | **str, none_type** | IPMI user name at the cluster level for the cluster. | [optional] 
**node_ipmi_users** | [**[NodeIpmiUser], none_type**](NodeIpmiUser.md) | Specifies the ipmi user info for all the nodes in the cluster. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


