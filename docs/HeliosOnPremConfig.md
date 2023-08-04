# HeliosOnPremConfig

Params for Helios OnPrem VM Configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Name of the new Helios OnPrem VM. | 
**kubernetes_subnet_cidr** | **str, none_type** | Subnet to use for setting up the Kubernetes cluster&#39;s internal network on which Cohesity Helios will run. | 
**cluster_id** | **int, none_type** | Specifies the ID of the Cluster. | [optional] [readonly] 
**nodes** | [**[HeliosOnPremVMNode]**](HeliosOnPremVMNode.md) | Specifies the Nodes present in this Cluster. | [optional] 
**network_config** | [**ClusterCreateNetworkConfig**](ClusterCreateNetworkConfig.md) |  | [optional] 
**proxy_server_config** | [**ClusterProxyServerConfig**](ClusterProxyServerConfig.md) |  | [optional] 
**ssh_config** | [**HeliosOnPremSSHConfig**](HeliosOnPremSSHConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


