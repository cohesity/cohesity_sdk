# ReplicationCluster

Specifies the information about replication cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Specifies the cluster id. | [optional] 
**cluster_incarnation_id** | **int** | Specifies the cluster incarnation id. | [optional] 
**cluster_name** | **str** | Specifies the cluster name. | [optional] 
**purpose_replication** | **bool** | Specifies if the remote cluster is added for replication. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.replication_cluster import ReplicationCluster

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationCluster from a JSON string
replication_cluster_instance = ReplicationCluster.from_json(json)
# print the JSON string representation of the object
print(ReplicationCluster.to_json())

# convert the object into a dict
replication_cluster_dict = replication_cluster_instance.to_dict()
# create an instance of ReplicationCluster from a dict
replication_cluster_from_dict = ReplicationCluster.from_dict(replication_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


