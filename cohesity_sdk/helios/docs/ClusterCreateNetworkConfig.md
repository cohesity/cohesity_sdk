# ClusterCreateNetworkConfig

Specifies all of the parameters needed for network configuration of the new Cluster.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ntp_servers** | **[str], none_type** | Specifies the list of NTP Servers new cluster should be configured with. | 
**domain_names** | **[str], none_type** | Specifies the list of Domain Names new cluster should be configured with. | 
**use_dhcp** | **bool, none_type** | Specifies whether or not to use DHCP to configure the network of the Cluster. | 
**vip_host_name** | **str, none_type** | Specifies the FQDN hostname of the cluster. | [optional] 
**ip_preference** | **str, none_type** | Specifies IP preference of the cluster to be Ipv4/Ipv6. It is Ipv4 by default. | [optional] 
**dhcp_network_config** | [**ClusterDhcpNetworkConfig**](ClusterDhcpNetworkConfig.md) |  | [optional] 
**manual_network_config** | [**ClusterManualNetworkConfig**](ClusterManualNetworkConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


