# ReplicationParams

Specifies the replication config for a Remote Cluster.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_endpoints_reachable** | **bool, none_type** | Specifies if all endpoints on Remote Cluster are reachable. | [optional]  if omitted the server will use the default value of False
**bandwidth_limit** | [**BandwidthThrottling**](BandwidthThrottling.md) |  | [optional] 
**compression_enabled** | **bool, none_type** | Specifies whether to compress the outbound data when transferring the replication data over the network to the Remote Cluster. | [optional]  if omitted the server will use the default value of True
**encryption_key** | **str, none_type** | Specifies the encryption key used for encrypting the replication data from a local Cluster to a Remote Cluster. If a key is not specified, replication traffic encryption is disabled. When Snapshots are replicated from a local Cluster to a Remote Cluster, the encryption key specified on the local Cluster must be the same as the key specified on the Remote Cluster. | [optional] 
**storage_domain_pairs** | [**[StorageDomainPair]**](StorageDomainPair.md) | Specifies a list of Storage Domain pairs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


