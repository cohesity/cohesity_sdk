# CreateFortknoxOnpremPrimaryClusterParams

Specifies the parameters to create a Fortknox Onprem Primary Cluster config.

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
from cohesity_sdk.cluster.models.create_fortknox_onprem_primary_cluster_params import CreateFortknoxOnpremPrimaryClusterParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFortknoxOnpremPrimaryClusterParams from a JSON string
create_fortknox_onprem_primary_cluster_params_instance = CreateFortknoxOnpremPrimaryClusterParams.from_json(json)
# print the JSON string representation of the object
print(CreateFortknoxOnpremPrimaryClusterParams.to_json())

# convert the object into a dict
create_fortknox_onprem_primary_cluster_params_dict = create_fortknox_onprem_primary_cluster_params_instance.to_dict()
# create an instance of CreateFortknoxOnpremPrimaryClusterParams from a dict
create_fortknox_onprem_primary_cluster_params_from_dict = CreateFortknoxOnpremPrimaryClusterParams.from_dict(create_fortknox_onprem_primary_cluster_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


