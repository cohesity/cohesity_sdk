# ClusterUpdateIpmiUsers

Specifies the cluster level IPMI user name and the list of node level IPMI user names for which ipmi credentials in cluster config needs to be updated.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_ipmi_password** | **str, none_type** | Specifies the ipmi password for the cluster level ipmi username to update ipmi user credentials. | [optional] 
**cluster_ipmi_username** | **str, none_type** | Specifies the cluster level IPMI username to update ipmi user credentials. | [optional] 
**node_ipmi_passwords** | **[str], none_type** | Specifies the ipmi passwords corresponding to the ipmi usernames provided. | [optional] 
**node_ipmi_usernames** | **[str], none_type** | Specifies the ipmi usernames for the nodes for which ipmi credentials in cluster config needs to be updated. | [optional] 
**node_ips** | **[str], none_type** | Specifies the ip addresses for nodes in the cluster for which ipmi credentials in cluster config needs to be updated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


