# StatsTaskInfo

Specifies the details about a Stats Task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_generic_stats** | [**BackupGenericStats**](BackupGenericStats.md) |  | [optional] 
**nas_stats** | [**BackupNasStats**](BackupNasStats.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.stats_task_info import StatsTaskInfo

# TODO update the JSON string below
json = "{}"
# create an instance of StatsTaskInfo from a JSON string
stats_task_info_instance = StatsTaskInfo.from_json(json)
# print the JSON string representation of the object
print(StatsTaskInfo.to_json())

# convert the object into a dict
stats_task_info_dict = stats_task_info_instance.to_dict()
# create an instance of StatsTaskInfo from a dict
stats_task_info_from_dict = StatsTaskInfo.from_dict(stats_task_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


