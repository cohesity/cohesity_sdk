# OdpRemoteCluster

Specifies an ODP Remote Cluster config.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int, none_type** | Specifies the ODP Remote Cluster id. | 
**cluster_incarnation_id** | **int, none_type** | Specifies the ODP Remote Cluster incarnation id. | 
**cluster_name** | **str, none_type** | Specifies the ODP Remote Cluster name. | 
**cluster_id_stale** | **bool, none_type** | Specifies if the cluster id is stale and needs to be refreshed. | [optional] 
**all_endpoints_reachable** | **bool, none_type** | Specifies if all endpoints on ODP Remote Cluster are reachable. | [optional] 
**storage_domain_pairs** | [**[StorageDomainPair], none_type**](StorageDomainPair.md) | Specifies a list of Storage Domain pairs. | [optional] 
**compression_enabled** | **bool, none_type** | Specifies whether to compress the data transferred to ODP Remote Cluster. | [optional] 
**key_encryption_key** | **str, none_type** | Specifies the key used for encrypting the data transferred to ODP Remote Cluster. | [optional] 
**used_for_replication** | **bool, none_type** | Specifies if the ODP Remote Cluster is used for replication. | [optional] 
**tenant_id** | **str, none_type** | Specifies the tenant id. | [optional] 
**remote_tenant_id** | **str, none_type** | Specifies the tenant id for ODP Remote Cluster. | [optional] 
**interface_group_name** | **str, none_type** | Specifies the interface group name of the ODP Remote Cluster. | [optional] 
**use_bifrost_broker_channel** | **bool, none_type** | Specifies whether to use Bifrost Broker channel for remote connection. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


