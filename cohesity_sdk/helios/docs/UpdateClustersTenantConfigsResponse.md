# UpdateClustersTenantConfigsResponse

Updated configurations related to tenants for all clusters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters** | [**List[UpdateClustersTenantConfigsResponseClustersInner]**](UpdateClustersTenantConfigsResponseClustersInner.md) | The list of clusters updated, with errors if any. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.update_clusters_tenant_configs_response import UpdateClustersTenantConfigsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateClustersTenantConfigsResponse from a JSON string
update_clusters_tenant_configs_response_instance = UpdateClustersTenantConfigsResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateClustersTenantConfigsResponse.to_json())

# convert the object into a dict
update_clusters_tenant_configs_response_dict = update_clusters_tenant_configs_response_instance.to_dict()
# create an instance of UpdateClustersTenantConfigsResponse from a dict
update_clusters_tenant_configs_response_from_dict = UpdateClustersTenantConfigsResponse.from_dict(update_clusters_tenant_configs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


