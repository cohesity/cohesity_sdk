# FortknoxOnpremClusterCommonParams

Specifies the parameters to create or update a Fortknox Onprem Cluster config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_endpoints_reachable** | **bool** | Specifies if all endpoints on the Cluster are reachable. | [optional] [default to False]
**bandwidth_limit** | [**BandwidthThrottling**](BandwidthThrottling.md) |  | [optional] 
**compression_enabled** | **bool** | Specifies whether to compress the outbound data when transferring the replication data over the network to the Vault Cluster. | [optional] [default to True]
**storage_domain_configs** | [**List[StorageDomainConfig]**](StorageDomainConfig.md) | Specifies a list of Storage Domain configurations. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.fortknox_onprem_cluster_common_params import FortknoxOnpremClusterCommonParams

# TODO update the JSON string below
json = "{}"
# create an instance of FortknoxOnpremClusterCommonParams from a JSON string
fortknox_onprem_cluster_common_params_instance = FortknoxOnpremClusterCommonParams.from_json(json)
# print the JSON string representation of the object
print(FortknoxOnpremClusterCommonParams.to_json())

# convert the object into a dict
fortknox_onprem_cluster_common_params_dict = fortknox_onprem_cluster_common_params_instance.to_dict()
# create an instance of FortknoxOnpremClusterCommonParams from a dict
fortknox_onprem_cluster_common_params_from_dict = FortknoxOnpremClusterCommonParams.from_dict(fortknox_onprem_cluster_common_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


