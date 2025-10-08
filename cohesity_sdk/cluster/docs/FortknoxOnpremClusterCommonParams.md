# FortknoxOnpremClusterCommonParams

Specifies the parameters to create or update a Fortknox Onprem Cluster config.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_endpoints_reachable** | **bool, none_type** | Specifies if all endpoints on the Cluster are reachable. | [optional]  if omitted the server will use the default value of False
**compression_enabled** | **bool, none_type** | Specifies whether to compress the outbound data when transferring the replication data over the network to the Vault Cluster. | [optional]  if omitted the server will use the default value of True
**storage_domain_configs** | [**[StorageDomainConfig]**](StorageDomainConfig.md) | Specifies a list of Storage Domain configurations. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


