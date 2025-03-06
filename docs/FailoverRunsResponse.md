# FailoverRunsResponse

Specifies the response upon creating a special run during failover workflow.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failover_planned_runs** | [**List[PlannedRunPollStatus]**](PlannedRunPollStatus.md) | Specifies the list of planned runs created during various planeed failover workflows. Each planned run is uniqely identified by falioverId and runId. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.failover_runs_response import FailoverRunsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FailoverRunsResponse from a JSON string
failover_runs_response_instance = FailoverRunsResponse.from_json(json)
# print the JSON string representation of the object
print(FailoverRunsResponse.to_json())

# convert the object into a dict
failover_runs_response_dict = failover_runs_response_instance.to_dict()
# create an instance of FailoverRunsResponse from a dict
failover_runs_response_from_dict = FailoverRunsResponse.from_dict(failover_runs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


