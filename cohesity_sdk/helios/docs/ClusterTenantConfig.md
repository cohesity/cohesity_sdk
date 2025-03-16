# ClusterTenantConfig

All configurations related to tenants for a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_identifier** | **str** | List of Clusters Identifiers to filter from. The format is clusterId:clusterIncarnationId. | 
**organizations_enabled** | **bool** | Whether organizations is enabled on the cluster. | 
**organizations_storage_domain_sharing_enabled** | **bool** | Whether storage domain sharing is enabled for organizations on the cluster. | [default to False]

## Example

```python
from cohesity_sdk.helios.models.cluster_tenant_config import ClusterTenantConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterTenantConfig from a JSON string
cluster_tenant_config_instance = ClusterTenantConfig.from_json(json)
# print the JSON string representation of the object
print(ClusterTenantConfig.to_json())

# convert the object into a dict
cluster_tenant_config_dict = cluster_tenant_config_instance.to_dict()
# create an instance of ClusterTenantConfig from a dict
cluster_tenant_config_from_dict = ClusterTenantConfig.from_dict(cluster_tenant_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


