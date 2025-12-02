# ClusterCreateNetworkConfig

Specifies all of the parameters needed for network configuration of the new Cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dhcp_network_config** | [**ClusterDhcpNetworkConfig**](ClusterDhcpNetworkConfig.md) |  | [optional] 
**domain_names** | **List[str]** | Specifies the list of Domain Names new cluster should be configured with. | 
**host_names** | **List[str]** | Specifies list of FQDN hostname of the cluster. | [optional] [readonly] 
**ip_preference** | **str** | Specifies IP preference of the cluster to be Ipv4/Ipv6. It is Ipv4 by default. | [optional] 
**manual_network_config** | [**ClusterManualNetworkConfig**](ClusterManualNetworkConfig.md) |  | [optional] 
**ntp_servers** | **List[str]** | Specifies the list of NTP Servers new cluster should be configured with. | 
**secondary_dhcp_network_config** | [**ClusterDhcpNetworkConfig**](ClusterDhcpNetworkConfig.md) |  | [optional] 
**secondary_manual_network_config** | [**ClusterManualNetworkConfig**](ClusterManualNetworkConfig.md) |  | [optional] 
**use_dhcp** | **bool** | Specifies whether or not to use DHCP to configure the network of the Cluster. | 
**vip_host_name** | **str** | Specifies the FQDN hostname of the cluster. Note: This field will be deprecated in future. Use hostNames field instead. | [optional] 
**vips** | **List[str]** | Virtual IPs to add to the cluster. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_create_network_config import ClusterCreateNetworkConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCreateNetworkConfig from a JSON string
cluster_create_network_config_instance = ClusterCreateNetworkConfig.from_json(json)
# print the JSON string representation of the object
print(ClusterCreateNetworkConfig.to_json())

# convert the object into a dict
cluster_create_network_config_dict = cluster_create_network_config_instance.to_dict()
# create an instance of ClusterCreateNetworkConfig from a dict
cluster_create_network_config_from_dict = ClusterCreateNetworkConfig.from_dict(cluster_create_network_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


