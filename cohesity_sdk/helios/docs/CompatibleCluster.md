# CompatibleCluster

Specifies a cluster compatible for a release.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Specifies cluster id. | [optional] 
**cluster_incarnation_id** | **int** | Specifies cluster incarnation id. | [optional] 
**cluster_name** | **str** | Specifies cluster&#39;s name. | [optional] 
**current_version** | **str** | Specifies the current version of the cluster. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.compatible_cluster import CompatibleCluster

# TODO update the JSON string below
json = "{}"
# create an instance of CompatibleCluster from a JSON string
compatible_cluster_instance = CompatibleCluster.from_json(json)
# print the JSON string representation of the object
print(CompatibleCluster.to_json())

# convert the object into a dict
compatible_cluster_dict = compatible_cluster_instance.to_dict()
# create an instance of CompatibleCluster from a dict
compatible_cluster_from_dict = CompatibleCluster.from_dict(compatible_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


