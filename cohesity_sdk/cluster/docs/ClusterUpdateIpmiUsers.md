# ClusterUpdateIpmiUsers

Specifies the  cluster level IPMI user name and the list of node level IPMI user names..

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_ipmi_password** | **str, none_type** | IPMI password at the cluster level for the cluster. | [optional] 
**cluster_ipmi_username** | **str, none_type** | IPMI user name at the cluster level for the cluster. | [optional] 
**node_ipmi_passwords** | **[str], none_type** | Specifies the ipmi passwords for all the nodes in the cluster. | [optional] 
**node_ipmi_usernames** | **[str], none_type** | Specifies the ipmi usernames for all the nodes in the cluster. | [optional] 
**node_ips** | **[str], none_type** | Specifies the ip addresses for all the nodes in the cluster. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


