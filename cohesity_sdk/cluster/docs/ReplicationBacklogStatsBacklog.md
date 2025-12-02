# ReplicationBacklogStatsBacklog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted** | [**ReplicationBacklogStateStats**](ReplicationBacklogStateStats.md) |  | [optional] 
**running** | [**ReplicationBacklogStateStats**](ReplicationBacklogStateStats.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.replication_backlog_stats_backlog import ReplicationBacklogStatsBacklog

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationBacklogStatsBacklog from a JSON string
replication_backlog_stats_backlog_instance = ReplicationBacklogStatsBacklog.from_json(json)
# print the JSON string representation of the object
print(ReplicationBacklogStatsBacklog.to_json())

# convert the object into a dict
replication_backlog_stats_backlog_dict = replication_backlog_stats_backlog_instance.to_dict()
# create an instance of ReplicationBacklogStatsBacklog from a dict
replication_backlog_stats_backlog_from_dict = ReplicationBacklogStatsBacklog.from_dict(replication_backlog_stats_backlog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


