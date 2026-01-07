# ClusterDeleteIpmiUsers

Specifies the cluster level IPMI user name and the list of node level IPMI user names for which ipmi credentials in cluster config needs to be deleted.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_ipmi_username** | **str, none_type** | Specifies the cluster level IPMI username to be deleted from cluster config. | [optional] 
**node_ipmi_usernames** | **[str], none_type** | Specifies the ipmi usernames for the nodes for which ipmi credentials in cluster config needs to be deleted. | [optional] 
**node_ips** | **[str], none_type** | Specifies the ip addresses for nodes in the cluster for which ipmi credentials in cluster config needs to be deleted. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


