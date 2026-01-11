# FortknoxOnpremPrimaryCluster

Specifies params for a Fortknox Onprem Primary Cluster.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int, none_type** | Specifies the id of the cluster. | [optional] 
**cluster_incarnation_id** | **int, none_type** | Specifies the incarnation id of the cluster. | [optional] 
**cluster_name** | **str, none_type** | Specifies the name of the cluster. | [optional] [readonly] 
**all_endpoints_reachable** | **bool, none_type** | Specifies if all endpoints on the Cluster are reachable. | [optional]  if omitted the server will use the default value of False
**bandwidth_limit** | [**BandwidthThrottling**](BandwidthThrottling.md) |  | [optional] 
**compression_enabled** | **bool, none_type** | Specifies whether to compress the outbound data when transferring the replication data over the network to the Vault Cluster. | [optional]  if omitted the server will use the default value of True
**storage_domain_configs** | [**[StorageDomainConfig]**](StorageDomainConfig.md) | Specifies a list of Storage Domain configurations. | [optional] 
**network_interface** | **str, none_type** | Specifies the name of the network interfaces to use for communicating with the Remote Cluster. | [optional] 
**node_ips** | **[str, none_type], none_type** | List of IPs of nodes in the cluster. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


