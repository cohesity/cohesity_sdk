# ReplicationClusterStats

Specifies the Replication Cluster Stats.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes** | **int** | Specifies the total replicated bytes to the cluster. | 
**id** | **int** | Specifies the cluster Id. | 

## Example

```python
from cohesity_sdk.cluster.models.replication_cluster_stats import ReplicationClusterStats

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationClusterStats from a JSON string
replication_cluster_stats_instance = ReplicationClusterStats.from_json(json)
# print the JSON string representation of the object
print(ReplicationClusterStats.to_json())

# convert the object into a dict
replication_cluster_stats_dict = replication_cluster_stats_instance.to_dict()
# create an instance of ReplicationClusterStats from a dict
replication_cluster_stats_from_dict = ReplicationClusterStats.from_dict(replication_cluster_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


