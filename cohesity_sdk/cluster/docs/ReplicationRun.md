# ReplicationRun

Specifies information about replication run for an object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replication_target_results** | [**List[ReplicationTargetResult]**](ReplicationTargetResult.md) | Replication result for a target. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.replication_run import ReplicationRun

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationRun from a JSON string
replication_run_instance = ReplicationRun.from_json(json)
# print the JSON string representation of the object
print(ReplicationRun.to_json())

# convert the object into a dict
replication_run_dict = replication_run_instance.to_dict()
# create an instance of ReplicationRun from a dict
replication_run_from_dict = ReplicationRun.from_dict(replication_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


