# LastProtectionRunSummary

Specifies the protection summary of the latest run using this policy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_cancelled_protection_runs** | **int** | Specifies the number of cancelled Protection Runs the given Protection Policy has in the Last Run. | [optional] 
**number_of_failed_protection_runs** | **int** | Specifies the number of failed Protection Runs the given Protection Policy has in the Last Run. | [optional] 
**number_of_protected_sources** | **int** | Specifies the number of Protection Sources protected by the given Protection Policy. | [optional] 
**number_of_running_protection_runs** | **int** | Specifies the number of running Protection Runs using the current Protection Policy. | [optional] 
**number_of_sla_violations** | **int** | Specifies the number of SLA violations the given Protection Policy has in the Last Run. | [optional] 
**number_of_successful_protection_runs** | **int** | Specifies the number of successful Protection Runs the given Protection Policy has in the Last Run. | [optional] 
**total_logical_backup_size_in_bytes** | **int** | Specifies the aggregated total logical backup performed in all the Latest Protection Runs made for all the Protection Groups which have the given Protection Policy Specified. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.last_protection_run_summary import LastProtectionRunSummary

# TODO update the JSON string below
json = "{}"
# create an instance of LastProtectionRunSummary from a JSON string
last_protection_run_summary_instance = LastProtectionRunSummary.from_json(json)
# print the JSON string representation of the object
print(LastProtectionRunSummary.to_json())

# convert the object into a dict
last_protection_run_summary_dict = last_protection_run_summary_instance.to_dict()
# create an instance of LastProtectionRunSummary from a dict
last_protection_run_summary_from_dict = LastProtectionRunSummary.from_dict(last_protection_run_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


