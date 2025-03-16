# GetProtectionRunStatsBody

Specifies the stats of a protection run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_run** | [**List[ArchivalTargetStatsInfo]**](ArchivalTargetStatsInfo.md) | Stats for the archival run. | [optional] 
**local_run** | [**BackupRunStatsInfo**](BackupRunStatsInfo.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.get_protection_run_stats_body import GetProtectionRunStatsBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetProtectionRunStatsBody from a JSON string
get_protection_run_stats_body_instance = GetProtectionRunStatsBody.from_json(json)
# print the JSON string representation of the object
print(GetProtectionRunStatsBody.to_json())

# convert the object into a dict
get_protection_run_stats_body_dict = get_protection_run_stats_body_instance.to_dict()
# create an instance of GetProtectionRunStatsBody from a dict
get_protection_run_stats_body_from_dict = GetProtectionRunStatsBody.from_dict(get_protection_run_stats_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


