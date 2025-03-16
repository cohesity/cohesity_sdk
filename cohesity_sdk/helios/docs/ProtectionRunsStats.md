# ProtectionRunsStats

Specifies the statistics of protection runs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protection_run_status** | **str** | Specifies the status of protection runs. | [optional] 
**protection_runs_count** | **int** | Specifies the number of protection runs. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.protection_runs_stats import ProtectionRunsStats

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectionRunsStats from a JSON string
protection_runs_stats_instance = ProtectionRunsStats.from_json(json)
# print the JSON string representation of the object
print(ProtectionRunsStats.to_json())

# convert the object into a dict
protection_runs_stats_dict = protection_runs_stats_instance.to_dict()
# create an instance of ProtectionRunsStats from a dict
protection_runs_stats_from_dict = ProtectionRunsStats.from_dict(protection_runs_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


