# ClustersTenantConfigs

All configurations related to tenants for all clusters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters** | [**List[ClusterTenantConfig]**](ClusterTenantConfig.md) | The list of clusters. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.clusters_tenant_configs import ClustersTenantConfigs

# TODO update the JSON string below
json = "{}"
# create an instance of ClustersTenantConfigs from a JSON string
clusters_tenant_configs_instance = ClustersTenantConfigs.from_json(json)
# print the JSON string representation of the object
print(ClustersTenantConfigs.to_json())

# convert the object into a dict
clusters_tenant_configs_dict = clusters_tenant_configs_instance.to_dict()
# create an instance of ClustersTenantConfigs from a dict
clusters_tenant_configs_from_dict = ClustersTenantConfigs.from_dict(clusters_tenant_configs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


