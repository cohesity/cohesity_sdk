# CloudSpinRunSummary

Specifies summary information about cloud spin run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_spin_target_results** | [**List[CloudSpinTargetResult]**](CloudSpinTargetResult.md) | Cloud Spin results for each Cloud Spin target. | [optional] 

## Example

```python
from cohesity_sdk.models.cloud_spin_run_summary import CloudSpinRunSummary

# TODO update the JSON string below
json = "{}"
# create an instance of CloudSpinRunSummary from a JSON string
cloud_spin_run_summary_instance = CloudSpinRunSummary.from_json(json)
# print the JSON string representation of the object
print(CloudSpinRunSummary.to_json())

# convert the object into a dict
cloud_spin_run_summary_dict = cloud_spin_run_summary_instance.to_dict()
# create an instance of CloudSpinRunSummary from a dict
cloud_spin_run_summary_from_dict = CloudSpinRunSummary.from_dict(cloud_spin_run_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


