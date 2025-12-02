# ProtectionRunsInPolicySummary

Specifies the aggregated summary of the Protection Runs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_archival_runs** | **int** | Specifies the total number of Archival Runs using the current Protection Policy. | [optional] 
**number_of_protection_runs** | **int** | Specifies the total number of Protection Runs by the given Protection Policy. | [optional] 
**number_of_replication_runs** | **int** | Specifies the total number of Replication Runs using the current Protection Policy. | [optional] 
**number_of_successful_archival_runs** | **int** | Specifies the number of total successful Archival Runs using the current Protection Policy. | [optional] 
**number_of_successful_protection_runs** | **int** | Specifies the number of successful Protection Runs using the current Protection Policy. | [optional] 
**number_of_successful_replication_runs** | **int** | Specifies the number of total successful Replication Runs using the current Protection Policy. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.protection_runs_in_policy_summary import ProtectionRunsInPolicySummary

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectionRunsInPolicySummary from a JSON string
protection_runs_in_policy_summary_instance = ProtectionRunsInPolicySummary.from_json(json)
# print the JSON string representation of the object
print(ProtectionRunsInPolicySummary.to_json())

# convert the object into a dict
protection_runs_in_policy_summary_dict = protection_runs_in_policy_summary_instance.to_dict()
# create an instance of ProtectionRunsInPolicySummary from a dict
protection_runs_in_policy_summary_from_dict = ProtectionRunsInPolicySummary.from_dict(protection_runs_in_policy_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


