# ClusterSnapshotPolicy

Describes the snapshot policy struct.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_retention_policy** | [**SnapshotRetentionPolicy**](SnapshotRetentionPolicy.md) |  | [optional] 
**snapshot_schedule_policy** | [**SnapshotSchedulePolicy**](SnapshotSchedulePolicy.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_snapshot_policy import ClusterSnapshotPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterSnapshotPolicy from a JSON string
cluster_snapshot_policy_instance = ClusterSnapshotPolicy.from_json(json)
# print the JSON string representation of the object
print(ClusterSnapshotPolicy.to_json())

# convert the object into a dict
cluster_snapshot_policy_dict = cluster_snapshot_policy_instance.to_dict()
# create an instance of ClusterSnapshotPolicy from a dict
cluster_snapshot_policy_from_dict = ClusterSnapshotPolicy.from_dict(cluster_snapshot_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


