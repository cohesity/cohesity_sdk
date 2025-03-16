# ClusterExpandParams

The parameters to expand the cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_cluster_params** | [**CloudClusterExpandParams**](CloudClusterExpandParams.md) |  | [optional] 
**physical_cluster_params** | [**PhysicalClusterExpandParams**](PhysicalClusterExpandParams.md) |  | [optional] 
**type** | **str** | Type of the cluster. &#39;Cloud&#39; indicates cloud edition cluster. &#39;Physical&#39; indicates physical edition cluster. &#39;Virtual&#39; indicates virtual edition cluster. | 

## Example

```python
from cohesity_sdk.cluster.models.cluster_expand_params import ClusterExpandParams

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterExpandParams from a JSON string
cluster_expand_params_instance = ClusterExpandParams.from_json(json)
# print the JSON string representation of the object
print(ClusterExpandParams.to_json())

# convert the object into a dict
cluster_expand_params_dict = cluster_expand_params_instance.to_dict()
# create an instance of ClusterExpandParams from a dict
cluster_expand_params_from_dict = ClusterExpandParams.from_dict(cluster_expand_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


