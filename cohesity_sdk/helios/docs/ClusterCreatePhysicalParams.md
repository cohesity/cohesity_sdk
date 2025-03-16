# ClusterCreatePhysicalParams

Params for Physical Edition Cluster Creation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**List[ClusterCreateNodeParams]**](ClusterCreateNodeParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.cluster_create_physical_params import ClusterCreatePhysicalParams

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCreatePhysicalParams from a JSON string
cluster_create_physical_params_instance = ClusterCreatePhysicalParams.from_json(json)
# print the JSON string representation of the object
print(ClusterCreatePhysicalParams.to_json())

# convert the object into a dict
cluster_create_physical_params_dict = cluster_create_physical_params_instance.to_dict()
# create an instance of ClusterCreatePhysicalParams from a dict
cluster_create_physical_params_from_dict = ClusterCreatePhysicalParams.from_dict(cluster_create_physical_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


