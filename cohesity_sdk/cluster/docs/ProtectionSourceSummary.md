# ProtectionSourceSummary

ProtectedSourceSummary is the summary of all the Protection Runs for the Protection groups using the Specified Protection Policy. This is only populated for a policy of type kRPO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_protection_group_paused** | **bool** | Specifies the status of the protection group | [optional] 
**last_protection_run** | [**CommonProtectionGroupRunResponseParameters**](CommonProtectionGroupRunResponseParameters.md) |  | [optional] 
**next_protection_run_time_usecs** | **int** | Specifies the time at which the next Protection Run is scheduled for the given Protection Source in Unix epoch Time | [optional] 
**object** | [**Object**](Object.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.protection_source_summary import ProtectionSourceSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectionSourceSummary from a JSON string
protection_source_summary_instance = ProtectionSourceSummary.from_json(json)
# print the JSON string representation of the object
print(ProtectionSourceSummary.to_json())

# convert the object into a dict
protection_source_summary_dict = protection_source_summary_instance.to_dict()
# create an instance of ProtectionSourceSummary from a dict
protection_source_summary_from_dict = ProtectionSourceSummary.from_dict(protection_source_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


