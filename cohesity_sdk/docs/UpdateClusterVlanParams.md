# UpdateClusterVlanParams

Parameters to update vlan on the cluster.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_tenant_access** | **bool, none_type** | Allow vlan to be used by all tenants without explicit assignment. Set to true only when the vlan is not assigned to any tenant. | [optional]  if omitted the server will use the default value of False
**app_ips** | **[str], none_type** | Vlan IP addresses for apps. | [optional] 
**description** | **str, none_type** | Description of the vlan. | [optional] 
**ecmp_enabled** | **bool, none_type** | Set to true to enable ECMP in the vlan. | [optional]  if omitted the server will use the default value of False
**ip_addresses_type** | **str, none_type** | Type of IP addresses. The default value is Ipv4. | [optional] 
**gateway** | **str, none_type** | Subnet gateway of the vlan. This can be Ipv4 or Ipv6 gateway based on the IP addresses type. | [optional] 
**subnet** | **str, none_type** | IPv6 or IPv6 subnet in CIDR format i.e ip-address/prefix. Examples: IPv4 subnet&#39;192.168.0.101/24&#39;, &#39;10.10.1.32/27&#39;. IPv6 subnet &#39;3005:1231:2006:0025::0/96&#39;, 3005:1231:2006:0025::0/128 | [optional] 
**tenant_id** | **str, none_type** | Tenant id to assign vlan to a tenant. | [optional] 
**vlan_name** | **str, none_type** | Name of the Vlan. | [optional] 
**mtu** | **int, none_type** | MTU of the vlan. | [optional] 
**ips** | **[str], none_type** | Vlan IP addresses, only one of ips or ipRanges parameters should be given. | [optional] 
**ip_ranges** | [**[IpRange], none_type**](IpRange.md) | Vlan IP address ranges, only one of ips or ipRanges parameters should be given. | [optional] 
**fqdn** | **str, none_type** | FQDN of the vlan. | [optional] 
**ip_pools** | [**[IpPool], none_type**](IpPool.md) | IP pools from the vlan ip addresses, the IPs in a pool goes together. One IP from each pool forms a VIP group. | [optional] 
**dns_delegation_zones** | [**[DnsDelegationZone], none_type**](DnsDelegationZone.md) | DNS delegation zones of the vlan. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


