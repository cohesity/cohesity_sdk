# ReplicationRunSummary

Specifies summary information about replication run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replication_target_results** | [**List[ReplicationTargetResult]**](ReplicationTargetResult.md) | Replication results for each replication target. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.replication_run_summary import ReplicationRunSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationRunSummary from a JSON string
replication_run_summary_instance = ReplicationRunSummary.from_json(json)
# print the JSON string representation of the object
print(ReplicationRunSummary.to_json())

# convert the object into a dict
replication_run_summary_dict = replication_run_summary_instance.to_dict()
# create an instance of ReplicationRunSummary from a dict
replication_run_summary_from_dict = ReplicationRunSummary.from_dict(replication_run_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


