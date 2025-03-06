# BackupRunStatsInfo

Specifies the stats of a local backup run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_generic_stats** | [**BackupGenericStats**](BackupGenericStats.md) |  | [optional] 
**nas_stats** | [**BackupNasStats**](BackupNasStats.md) |  | [optional] 
**objects** | [**List[ObjectStatsInfo]**](ObjectStatsInfo.md) | Specifies stats for objects. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.backup_run_stats_info import BackupRunStatsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BackupRunStatsInfo from a JSON string
backup_run_stats_info_instance = BackupRunStatsInfo.from_json(json)
# print the JSON string representation of the object
print(BackupRunStatsInfo.to_json())

# convert the object into a dict
backup_run_stats_info_dict = backup_run_stats_info_instance.to_dict()
# create an instance of BackupRunStatsInfo from a dict
backup_run_stats_info_from_dict = BackupRunStatsInfo.from_dict(backup_run_stats_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


