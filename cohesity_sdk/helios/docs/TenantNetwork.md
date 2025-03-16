# TenantNetwork

Networking information about a Tenant on a Cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_hostname** | **str** | The hostname for Cohesity cluster as seen by tenants and as is routable from the tenant&#39;s network. Tenant&#39;s VLAN&#39;s hostname, if available can be used instead but it is mandatory to provide this value if there&#39;s no VLAN hostname to use. Also, when set, this field would take precedence over VLAN hostname. | [optional] 
**cluster_ips** | **List[str]** | Set of IPs as seen from the tenant&#39;s network for the Cohesity cluster. Only one from &#39;clusterHostname&#39; and &#39;clusterIps&#39; is needed. | [optional] 
**connector_enabled** | **bool** | Whether connector (hybrid extender) is enabled. | 

## Example

```python
from cohesity_sdk.helios.models.tenant_network import TenantNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of TenantNetwork from a JSON string
tenant_network_instance = TenantNetwork.from_json(json)
# print the JSON string representation of the object
print(TenantNetwork.to_json())

# convert the object into a dict
tenant_network_dict = tenant_network_instance.to_dict()
# create an instance of TenantNetwork from a dict
tenant_network_from_dict = TenantNetwork.from_dict(tenant_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


