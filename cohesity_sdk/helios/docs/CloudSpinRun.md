# CloudSpinRun

Specifies information about Cloud Spin run for an object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_spin_target_results** | [**List[CloudSpinTargetResult]**](CloudSpinTargetResult.md) | Cloud Spin result for a target. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.cloud_spin_run import CloudSpinRun

# TODO update the JSON string below
json = "{}"
# create an instance of CloudSpinRun from a JSON string
cloud_spin_run_instance = CloudSpinRun.from_json(json)
# print the JSON string representation of the object
print(CloudSpinRun.to_json())

# convert the object into a dict
cloud_spin_run_dict = cloud_spin_run_instance.to_dict()
# create an instance of CloudSpinRun from a dict
cloud_spin_run_from_dict = CloudSpinRun.from_dict(cloud_spin_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


