# StorageArraySnapshotSchedule

Specifies settings that defines how frequent Storage Snapshot Management backup will be performed for a Protection Group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str, none_type** | Specifies how often to start new Protection Group Runs of a Protection Group. &lt;br&gt;&#39;Minutes&#39; specifies that Protection Group run starts periodically after certain number of minutes specified in &#39;frequency&#39; field. &lt;br&gt;&#39;Hours&#39; specifies that Protection Group run starts periodically after certain number of hours specified in &#39;frequency&#39; field. | 
**minute_schedule** | [**MinuteSchedule**](MinuteSchedule.md) |  | [optional] 
**hour_schedule** | [**HourSchedule**](HourSchedule.md) |  | [optional] 
**day_schedule** | [**DaySchedule**](DaySchedule.md) |  | [optional] 
**week_schedule** | [**WeekSchedule**](WeekSchedule.md) |  | [optional] 
**month_schedule** | [**MonthSchedule**](MonthSchedule.md) |  | [optional] 
**year_schedule** | [**YearSchedule**](YearSchedule.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


