# UpgradeChecksResults

Specifies upgrade checks results from cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error message if test results could not be fetched. | [optional] 
**finish_time_secs** | **int** | Specifies unix epoch finish time of checks(in seconds). | [optional] 
**node_results** | [**List[UpgradeCheckNodeResult]**](UpgradeCheckNodeResult.md) | The healthcheck result for node. | [optional] 
**request_type** | **str** | Type of the check(preupgrade/postupgrade). | [optional] 
**result_status** | **str** | Final result (running/pass/fail) of run. | [optional] 
**start_time_secs** | **int** | Specifies unix epoch start time of checks(in seconds). | [optional] 
**test_run_instance_id** | **str** | Specifies test run instance of upgrade checks. | [optional] 

## Example

```python
from cohesity_sdk.models.upgrade_checks_results import UpgradeChecksResults

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeChecksResults from a JSON string
upgrade_checks_results_instance = UpgradeChecksResults.from_json(json)
# print the JSON string representation of the object
print(UpgradeChecksResults.to_json())

# convert the object into a dict
upgrade_checks_results_dict = upgrade_checks_results_instance.to_dict()
# create an instance of UpgradeChecksResults from a dict
upgrade_checks_results_from_dict = UpgradeChecksResults.from_dict(upgrade_checks_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


