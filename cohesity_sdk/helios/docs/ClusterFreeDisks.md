# ClusterFreeDisks

Sepcifies the free disks of cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_free_disks** | [**List[NodeFreeDisks]**](NodeFreeDisks.md) | Specifies list of free disks of cluster. | 

## Example

```python
from cohesity_sdk.helios.models.cluster_free_disks import ClusterFreeDisks

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterFreeDisks from a JSON string
cluster_free_disks_instance = ClusterFreeDisks.from_json(json)
# print the JSON string representation of the object
print(ClusterFreeDisks.to_json())

# convert the object into a dict
cluster_free_disks_dict = cluster_free_disks_instance.to_dict()
# create an instance of ClusterFreeDisks from a dict
cluster_free_disks_from_dict = ClusterFreeDisks.from_dict(cluster_free_disks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


