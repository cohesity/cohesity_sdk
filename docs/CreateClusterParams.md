# CreateClusterParams

Specifies the parameters required to create cluster.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the name of the new cluster. | 
**type** | **str, none_type** | Specifies the type of the new cluster. | 
**enable_encryption** | **bool, none_type** | Specifies whether or not to enable encryption. If encryption is enabled, all data on the Cluster will be encrypted. This can only be enabled at Cluster creation time and cannot be disabled later. | 
**network_config** | [**ClusterCreateNetworkConfig**](ClusterCreateNetworkConfig.md) |  | 
**proxy_server_config** | [**ClusterProxyServerConfig**](ClusterProxyServerConfig.md) |  | [optional] 
**physical_cluster_params** | [**ClusterCreatePhysicalParams**](ClusterCreatePhysicalParams.md) |  | [optional] 
**virtual_cluster_params** | [**ClusterCreateVirtualParams**](ClusterCreateVirtualParams.md) |  | [optional] 
**cloud_cluster_params** | [**ClusterCreateCloudParams**](ClusterCreateCloudParams.md) |  | [optional] 
**rigel_cluster_params** | [**ClusterCreateRigelParams**](ClusterCreateRigelParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


