# UpdateClusterVlanParams

Parameters to update vlan on the cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_tenant_access** | **bool** | Allow vlan to be used by all tenants without explicit assignment. Set to true only when the vlan is not assigned to any tenant. | [optional] [default to False]
**app_ips** | **List[str]** | Vlan IP addresses for apps. | [optional] 
**description** | **str** | Description of the vlan. | [optional] 
**dns_delegation_zones** | [**List[DnsDelegationZone]**](DnsDelegationZone.md) | DNS delegation zones of the vlan. | [optional] 
**ecmp_enabled** | **bool** | Set to true to enable ECMP in the vlan. | [optional] [default to False]
**fqdn** | **str** | FQDN of the vlan. | [optional] 
**gateway** | **str** | Subnet gateway of the vlan. This can be Ipv4 or Ipv6 gateway based on the IP addresses type. | [optional] 
**ip_addresses_type** | **str** | Type of IP addresses. The default value is Ipv4. | [optional] 
**ip_pools** | [**List[IpPool]**](IpPool.md) | IP pools from the vlan ip addresses, the IPs in a pool goes together. One IP from each pool forms a VIP group. | [optional] 
**ip_ranges** | [**List[IpRange]**](IpRange.md) | Vlan IP address ranges, only one of ips or ipRanges parameters should be given. | [optional] 
**ips** | **List[str]** | Vlan IP addresses, only one of ips or ipRanges parameters should be given. | [optional] 
**mtu** | **int** | MTU of the vlan. | [optional] 
**subnet** | **str** | IPv6 or IPv6 subnet in CIDR format i.e ip-address/prefix. Examples: IPv4 subnet&#39;192.168.0.101/24&#39;, &#39;10.10.1.32/27&#39;. IPv6 subnet &#39;3005:1231:2006:0025::0/96&#39;, 3005:1231:2006:0025::0/128 | [optional] 
**tenant_id** | **str** | Tenant id to assign vlan to a tenant. | [optional] 
**vlan_name** | **str** | Name of the Vlan. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.update_cluster_vlan_params import UpdateClusterVlanParams

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateClusterVlanParams from a JSON string
update_cluster_vlan_params_instance = UpdateClusterVlanParams.from_json(json)
# print the JSON string representation of the object
print(UpdateClusterVlanParams.to_json())

# convert the object into a dict
update_cluster_vlan_params_dict = update_cluster_vlan_params_instance.to_dict()
# create an instance of UpdateClusterVlanParams from a dict
update_cluster_vlan_params_from_dict = UpdateClusterVlanParams.from_dict(update_cluster_vlan_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


