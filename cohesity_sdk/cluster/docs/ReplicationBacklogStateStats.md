# ReplicationBacklogStateStats

Specifies the Replication Backlog Stats for a given state.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes** | **int** | Total number of bytes backlogged for data replication. | 
**objects** | **int** | Total number of objects backlogged for data replication. | 

## Example

```python
from cohesity_sdk.cluster.models.replication_backlog_state_stats import ReplicationBacklogStateStats

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationBacklogStateStats from a JSON string
replication_backlog_state_stats_instance = ReplicationBacklogStateStats.from_json(json)
# print the JSON string representation of the object
print(ReplicationBacklogStateStats.to_json())

# convert the object into a dict
replication_backlog_state_stats_dict = replication_backlog_state_stats_instance.to_dict()
# create an instance of ReplicationBacklogStateStats from a dict
replication_backlog_state_stats_from_dict = ReplicationBacklogStateStats.from_dict(replication_backlog_state_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


