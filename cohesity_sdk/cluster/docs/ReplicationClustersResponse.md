# ReplicationClustersResponse

Specifies the Replication Clusters Response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters** | [**List[ReplicationClusterStats]**](ReplicationClusterStats.md) | Specifies a list of Replication Cluster stats. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.replication_clusters_response import ReplicationClustersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationClustersResponse from a JSON string
replication_clusters_response_instance = ReplicationClustersResponse.from_json(json)
# print the JSON string representation of the object
print(ReplicationClustersResponse.to_json())

# convert the object into a dict
replication_clusters_response_dict = replication_clusters_response_instance.to_dict()
# create an instance of ReplicationClustersResponse from a dict
replication_clusters_response_from_dict = ReplicationClustersResponse.from_dict(replication_clusters_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


