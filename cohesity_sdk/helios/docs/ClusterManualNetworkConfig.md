# ClusterManualNetworkConfig

Specifies all of the parameters needed for network configuration of the new Cluster using manual configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_servers** | **List[str]** | Specifies the list of Dns Servers new cluster should be configured with. | 
**gateway** | **str** | Specifies the gateway of the new cluster network. | 
**subnet_ip** | **str** | Specifies the ip subnet ip of the cluster network. | 
**subnet_mask** | **str** | Specifies the ip subnet mask of the cluster network. | 

## Example

```python
from cohesity_sdk.helios.models.cluster_manual_network_config import ClusterManualNetworkConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterManualNetworkConfig from a JSON string
cluster_manual_network_config_instance = ClusterManualNetworkConfig.from_json(json)
# print the JSON string representation of the object
print(ClusterManualNetworkConfig.to_json())

# convert the object into a dict
cluster_manual_network_config_dict = cluster_manual_network_config_instance.to_dict()
# create an instance of ClusterManualNetworkConfig from a dict
cluster_manual_network_config_from_dict = ClusterManualNetworkConfig.from_dict(cluster_manual_network_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


