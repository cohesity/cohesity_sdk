# ClusterCreateVirtualParams

Params for Virtual Edition Cluster Creation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**List[ClusterCreateNodeParams]**](ClusterCreateNodeParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_create_virtual_params import ClusterCreateVirtualParams

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCreateVirtualParams from a JSON string
cluster_create_virtual_params_instance = ClusterCreateVirtualParams.from_json(json)
# print the JSON string representation of the object
print(ClusterCreateVirtualParams.to_json())

# convert the object into a dict
cluster_create_virtual_params_dict = cluster_create_virtual_params_instance.to_dict()
# create an instance of ClusterCreateVirtualParams from a dict
cluster_create_virtual_params_from_dict = ClusterCreateVirtualParams.from_dict(cluster_create_virtual_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


