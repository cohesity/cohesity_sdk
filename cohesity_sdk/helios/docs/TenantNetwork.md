# TenantNetwork

Networking information about a Tenant on a Cluster.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_enabled** | **bool, none_type** | Whether connector (hybrid extender) is enabled. | [optional] 
**cluster_hostname** | **str, none_type** | The hostname for Cohesity cluster as seen by tenants and as is routable   from the tenant&#39;s network. Tenant&#39;s VLAN&#39;s hostname, if available can be   used instead but it is mandatory to provide this value if there&#39;s no VLAN   hostname to use. Also, when set, this field would take precedence over   VLAN hostname. | [optional] 
**cluster_ips** | **[str, none_type], none_type** | Set of IPs as seen from the tenant&#39;s network for the Cohesity cluster.   Only one from &#39;clusterHostname&#39; and &#39;clusterIps&#39; is needed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


