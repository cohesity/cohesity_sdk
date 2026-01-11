# ClusterCreateNetworkConfig

Specifies all of the parameters needed for network configuration of the new Cluster.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_names** | **[str], none_type** | Specifies the list of Domain Names new cluster should be configured with. | 
**ntp_servers** | **[str], none_type** | Specifies the list of NTP Servers new cluster should be configured with. | 
**use_dhcp** | **bool, none_type** | Specifies whether or not to use DHCP to configure the network of the Cluster. | 
**dhcp_network_config** | [**ClusterDhcpNetworkConfig**](ClusterDhcpNetworkConfig.md) |  | [optional] 
**host_names** | **[str], none_type** | Specifies list of FQDN hostname of the cluster. | [optional] [readonly] 
**ip_preference** | **str, none_type** | Specifies IP preference of the cluster to be Ipv4/Ipv6. It is Ipv4 by default. | [optional] 
**manual_network_config** | [**ClusterManualNetworkConfig**](ClusterManualNetworkConfig.md) |  | [optional] 
**secondary_dhcp_network_config** | [**ClusterDhcpNetworkConfig**](ClusterDhcpNetworkConfig.md) |  | [optional] 
**secondary_manual_network_config** | [**ClusterManualNetworkConfig**](ClusterManualNetworkConfig.md) |  | [optional] 
**vip_host_name** | **str, none_type** | Specifies the FQDN hostname of the cluster. Note: This field will be deprecated in future. Use hostNames field instead. | [optional] 
**vips** | **[str]** | Virtual IPs to add to the cluster. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


