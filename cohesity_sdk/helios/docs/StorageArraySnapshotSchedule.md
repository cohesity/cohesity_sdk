# StorageArraySnapshotSchedule

Specifies settings that defines how frequent Storage Snapshot Management backup will be performed for a Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_schedule** | [**DaySchedule**](DaySchedule.md) |  | [optional] 
**hour_schedule** | [**HourSchedule**](HourSchedule.md) |  | [optional] 
**minute_schedule** | [**MinuteSchedule**](MinuteSchedule.md) |  | [optional] 
**month_schedule** | [**MonthSchedule**](MonthSchedule.md) |  | [optional] 
**unit** | **str** | Specifies how often to start new Protection Group Runs of a Protection Group. &lt;br&gt;&#39;Minutes&#39; specifies that Protection Group run starts periodically after certain number of minutes specified in &#39;frequency&#39; field. &lt;br&gt;&#39;Hours&#39; specifies that Protection Group run starts periodically after certain number of hours specified in &#39;frequency&#39; field. | 
**week_schedule** | [**WeekSchedule**](WeekSchedule.md) |  | [optional] 
**year_schedule** | [**YearSchedule**](YearSchedule.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.storage_array_snapshot_schedule import StorageArraySnapshotSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of StorageArraySnapshotSchedule from a JSON string
storage_array_snapshot_schedule_instance = StorageArraySnapshotSchedule.from_json(json)
# print the JSON string representation of the object
print(StorageArraySnapshotSchedule.to_json())

# convert the object into a dict
storage_array_snapshot_schedule_dict = storage_array_snapshot_schedule_instance.to_dict()
# create an instance of StorageArraySnapshotSchedule from a dict
storage_array_snapshot_schedule_from_dict = StorageArraySnapshotSchedule.from_dict(storage_array_snapshot_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


