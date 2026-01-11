# Schedule

Specifies a schedule for actions to be taken.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**periodic_time_windows** | [**[TimeWindow]**](TimeWindow.md) |  Specifies the time range within the days of the week. | [optional] 
**schedule_type** | **str, none_type** | Specifies the type of schedule for this ScheduleProto. | [optional] 
**time_ranges** | [**[TimeRangeUsecs]**](TimeRangeUsecs.md) |  Specifies the time ranges in usecs. | [optional] 
**timezone** | **str** | Specifies the timezone of the user of this ScheduleProto. The timezones have unique names of the form &#39;Area/Location&#39;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


