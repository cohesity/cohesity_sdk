# UpdateClustersTenantConfigsResponseClustersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_identifier** | **str** | List of Clusters Identifiers to filter from. The format is clusterId:clusterIncarnationId. | 
**organizations_enabled** | **bool** | Whether organizations is enabled on the cluster. | 
**organizations_storage_domain_sharing_enabled** | **bool** | Whether storage domain sharing is enabled for organizations on the cluster. | [default to False]
**error_message** | **str** | Error message for the cluster. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.update_clusters_tenant_configs_response_clusters_inner import UpdateClustersTenantConfigsResponseClustersInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateClustersTenantConfigsResponseClustersInner from a JSON string
update_clusters_tenant_configs_response_clusters_inner_instance = UpdateClustersTenantConfigsResponseClustersInner.from_json(json)
# print the JSON string representation of the object
print(UpdateClustersTenantConfigsResponseClustersInner.to_json())

# convert the object into a dict
update_clusters_tenant_configs_response_clusters_inner_dict = update_clusters_tenant_configs_response_clusters_inner_instance.to_dict()
# create an instance of UpdateClustersTenantConfigsResponseClustersInner from a dict
update_clusters_tenant_configs_response_clusters_inner_from_dict = UpdateClustersTenantConfigsResponseClustersInner.from_dict(update_clusters_tenant_configs_response_clusters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


