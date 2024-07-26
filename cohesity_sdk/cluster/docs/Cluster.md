# Cluster

Specifies the cluster details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_audit_log_config** | [**ClusterAuditLogConfig**](ClusterAuditLogConfig.md) |  | [optional] 
**cluster_size** | **str, none_type** | Specifies the size of the cloud platforms. | [optional] [readonly] 
**description** | **str, none_type** | Description of the cluster. | [optional] 
**enable_encryption** | **bool, none_type** | Specifies whether or not encryption is enabled. If encryption is enabled, all data on the Cluster will be encrypted. | [optional] [readonly] 
**file_services_audit_log_config** | [**AuditLogConfig**](AuditLogConfig.md) |  | [optional] 
**id** | **int, none_type** | Specifies the cluster id of the new cluster. | [optional] [readonly] 
**incarnation_id** | **int, none_type** | Specifies the incarnation id of the new cluster. | [optional] [readonly] 
**local_tenant_id** | **str, none_type** | Specifies the local tenant id. Only applicable on Helios. | [optional] [readonly] 
**name** | **str, none_type** | Name of the new cluster. | [optional] 
**network_config** | [**ClusterCreateNetworkConfig**](ClusterCreateNetworkConfig.md) |  | [optional] 
**proxy_server_config** | [**ClusterProxyServerConfig**](ClusterProxyServerConfig.md) |  | [optional] 
**region_id** | **str, none_type** | Specifies the region id on which this cluster is present. Only applicable on Helios for DMaaS clusters. | [optional] [readonly] 
**rigel_cluster_params** | [**RigelClusterConfigParams**](RigelClusterConfigParams.md) |  | [optional] 
**sw_version** | **str, none_type** | Software version of the new cluster. | [optional] [readonly] 
**tenant_id** | **str, none_type** | Specifies the globally unique tenant id. Only applicable on Helios. | [optional] [readonly] 
**type** | **str, none_type** | Specifies the type of the new cluster. | [optional] [readonly] 
**views_global_settings** | [**ViewsGlobalSettings**](ViewsGlobalSettings.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


