# BmrSchedule

Specifies settings that defines how frequent bmr backup will be performed for a Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_schedule** | [**DaySchedule**](DaySchedule.md) |  | [optional] 
**month_schedule** | [**MonthSchedule**](MonthSchedule.md) |  | [optional] 
**unit** | **str** | Specifies how often to start new runs of a Protection Group. &lt;br&gt;&#39;Weeks&#39; specifies that new Protection Group runs start weekly on certain days specified using &#39;dayOfWeek&#39; field. &lt;br&gt;&#39;Months&#39; specifies that new Protection Group runs start monthly on certain day of specific week. | 
**week_schedule** | [**WeekSchedule**](WeekSchedule.md) |  | [optional] 
**year_schedule** | [**YearSchedule**](YearSchedule.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.bmr_schedule import BmrSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of BmrSchedule from a JSON string
bmr_schedule_instance = BmrSchedule.from_json(json)
# print the JSON string representation of the object
print(BmrSchedule.to_json())

# convert the object into a dict
bmr_schedule_dict = bmr_schedule_instance.to_dict()
# create an instance of BmrSchedule from a dict
bmr_schedule_from_dict = BmrSchedule.from_dict(bmr_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


