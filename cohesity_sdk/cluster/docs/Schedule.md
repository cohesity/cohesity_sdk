# Schedule

Specifies a schedule for actions to be taken.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**periodic_time_windows** | [**List[TimeWindow]**](TimeWindow.md) |  Specifies the time range within the days of the week. | [optional] 
**schedule_type** | **str** | Specifies the type of schedule for this ScheduleProto. | [optional] 
**time_ranges** | [**List[TimeRangeUsecs]**](TimeRangeUsecs.md) |  Specifies the time ranges in usecs. | [optional] 
**timezone** | **str** | Specifies the timezone of the user of this ScheduleProto. The timezones have unique names of the form &#39;Area/Location&#39;. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.schedule import Schedule

# TODO update the JSON string below
json = "{}"
# create an instance of Schedule from a JSON string
schedule_instance = Schedule.from_json(json)
# print the JSON string representation of the object
print(Schedule.to_json())

# convert the object into a dict
schedule_dict = schedule_instance.to_dict()
# create an instance of Schedule from a dict
schedule_from_dict = Schedule.from_dict(schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


