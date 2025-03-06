# ArchivalRunSummary

Specifies summary information about archival run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_target_results** | [**List[ArchivalTargetResult]**](ArchivalTargetResult.md) | Archival results for each archival target. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.archival_run_summary import ArchivalRunSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ArchivalRunSummary from a JSON string
archival_run_summary_instance = ArchivalRunSummary.from_json(json)
# print the JSON string representation of the object
print(ArchivalRunSummary.to_json())

# convert the object into a dict
archival_run_summary_dict = archival_run_summary_instance.to_dict()
# create an instance of ArchivalRunSummary from a dict
archival_run_summary_from_dict = ArchivalRunSummary.from_dict(archival_run_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


