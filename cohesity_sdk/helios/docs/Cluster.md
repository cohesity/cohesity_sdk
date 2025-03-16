# Cluster

Specifies the cluster details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_audit_log_config** | [**ClusterAuditLogConfig**](ClusterAuditLogConfig.md) |  | [optional] 
**cluster_size** | **str** | Specifies the size of the cloud platforms. | [optional] [readonly] 
**description** | **str** | Description of the cluster. | [optional] 
**enable_encryption** | **bool** | Specifies whether or not encryption is enabled. If encryption is enabled, all data on the Cluster will be encrypted. | [optional] [readonly] 
**file_services_audit_log_config** | [**AuditLogConfig**](AuditLogConfig.md) |  | [optional] 
**id** | **int** | Specifies the cluster id of the new cluster. | [optional] [readonly] 
**incarnation_id** | **int** | Specifies the incarnation id of the new cluster. | [optional] [readonly] 
**local_tenant_id** | **str** | Specifies the local tenant id. Only applicable on Helios. | [optional] [readonly] 
**name** | **str** | Name of the new cluster. | [optional] 
**network_config** | [**ClusterCreateNetworkConfig**](ClusterCreateNetworkConfig.md) |  | [optional] 
**proxy_server_config** | [**ClusterProxyServerConfig**](ClusterProxyServerConfig.md) |  | [optional] 
**region_id** | **str** | Specifies the region id on which this cluster is present. Only applicable on Helios for DMaaS clusters. | [optional] [readonly] 
**rigel_cluster_params** | [**RigelClusterConfigParams**](RigelClusterConfigParams.md) |  | [optional] 
**sw_version** | **str** | Software version of the new cluster. | [optional] [readonly] 
**tenant_id** | **str** | Specifies the globally unique tenant id. Only applicable on Helios. | [optional] [readonly] 
**type** | **str** | Specifies the type of the new cluster. | [optional] [readonly] 
**views_global_settings** | [**ViewsGlobalSettings**](ViewsGlobalSettings.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.cluster import Cluster

# TODO update the JSON string below
json = "{}"
# create an instance of Cluster from a JSON string
cluster_instance = Cluster.from_json(json)
# print the JSON string representation of the object
print(Cluster.to_json())

# convert the object into a dict
cluster_dict = cluster_instance.to_dict()
# create an instance of Cluster from a dict
cluster_from_dict = Cluster.from_dict(cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


