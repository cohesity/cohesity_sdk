# RecoverClusterScopedResourcesParams

Specifies the parameters from where the cluster scoped resources would be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_id** | **str** | Specifies the snapshot id of the namespace from where the cluster scoped resources are to be recovered. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_cluster_scoped_resources_params import RecoverClusterScopedResourcesParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverClusterScopedResourcesParams from a JSON string
recover_cluster_scoped_resources_params_instance = RecoverClusterScopedResourcesParams.from_json(json)
# print the JSON string representation of the object
print(RecoverClusterScopedResourcesParams.to_json())

# convert the object into a dict
recover_cluster_scoped_resources_params_dict = recover_cluster_scoped_resources_params_instance.to_dict()
# create an instance of RecoverClusterScopedResourcesParams from a dict
recover_cluster_scoped_resources_params_from_dict = RecoverClusterScopedResourcesParams.from_dict(recover_cluster_scoped_resources_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


