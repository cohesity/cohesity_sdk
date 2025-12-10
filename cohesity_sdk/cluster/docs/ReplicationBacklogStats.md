# ReplicationBacklogStats

Specifies the Replication Backlog Stats.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backlog** | [**ReplicationBacklogStatsBacklog**](ReplicationBacklogStatsBacklog.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.replication_backlog_stats import ReplicationBacklogStats

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationBacklogStats from a JSON string
replication_backlog_stats_instance = ReplicationBacklogStats.from_json(json)
# print the JSON string representation of the object
print(ReplicationBacklogStats.to_json())

# convert the object into a dict
replication_backlog_stats_dict = replication_backlog_stats_instance.to_dict()
# create an instance of ReplicationBacklogStats from a dict
replication_backlog_stats_from_dict = ReplicationBacklogStats.from_dict(replication_backlog_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


