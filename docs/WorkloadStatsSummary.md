# WorkloadStatsSummary

Specifies the Workload Stats Summary Schema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workloads** | [**List[WorkloadStatsSchema]**](WorkloadStatsSchema.md) | Specifies the Workload types. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.workload_stats_summary import WorkloadStatsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of WorkloadStatsSummary from a JSON string
workload_stats_summary_instance = WorkloadStatsSummary.from_json(json)
# print the JSON string representation of the object
print(WorkloadStatsSummary.to_json())

# convert the object into a dict
workload_stats_summary_dict = workload_stats_summary_instance.to_dict()
# create an instance of WorkloadStatsSummary from a dict
workload_stats_summary_from_dict = WorkloadStatsSummary.from_dict(workload_stats_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


