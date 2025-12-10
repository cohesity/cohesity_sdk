# FortknoxOnpremVaultCluster

Specifies params for a Fortknox Onprem Vault Cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Specifies the id of the cluster. | [optional] 
**cluster_incarnation_id** | **int** | Specifies the incarnation id of the cluster. | [optional] 
**cluster_name** | **str** | Specifies the name of the cluster. | [optional] [readonly] 
**all_endpoints_reachable** | **bool** | Specifies if all endpoints on the Cluster are reachable. | [optional] [default to False]
**bandwidth_limit** | [**BandwidthThrottling**](BandwidthThrottling.md) |  | [optional] 
**compression_enabled** | **bool** | Specifies whether to compress the outbound data when transferring the replication data over the network to the Vault Cluster. | [optional] [default to True]
**storage_domain_configs** | [**List[StorageDomainConfig]**](StorageDomainConfig.md) | Specifies a list of Storage Domain configurations. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.fortknox_onprem_vault_cluster import FortknoxOnpremVaultCluster

# TODO update the JSON string below
json = "{}"
# create an instance of FortknoxOnpremVaultCluster from a JSON string
fortknox_onprem_vault_cluster_instance = FortknoxOnpremVaultCluster.from_json(json)
# print the JSON string representation of the object
print(FortknoxOnpremVaultCluster.to_json())

# convert the object into a dict
fortknox_onprem_vault_cluster_dict = fortknox_onprem_vault_cluster_instance.to_dict()
# create an instance of FortknoxOnpremVaultCluster from a dict
fortknox_onprem_vault_cluster_from_dict = FortknoxOnpremVaultCluster.from_dict(fortknox_onprem_vault_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


