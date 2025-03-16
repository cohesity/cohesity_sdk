# DaySchedule

Specifies settings that define a schedule for a Protection Group runs to start after certain number of days.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **int** | Specifies a factor to multiply the unit by, to determine the backup schedule. &lt;br&gt; Example: If &#39;frequency&#39; set to 2 and the unit is &#39;Hours&#39;, then Snapshots are backed up every 2 hours. &lt;br&gt; This field is only applicable if unit is &#39;Minutes&#39;, &#39;Hours&#39; or &#39;Days&#39;. | 

## Example

```python
from cohesity_sdk.helios.models.day_schedule import DaySchedule

# TODO update the JSON string below
json = "{}"
# create an instance of DaySchedule from a JSON string
day_schedule_instance = DaySchedule.from_json(json)
# print the JSON string representation of the object
print(DaySchedule.to_json())

# convert the object into a dict
day_schedule_dict = day_schedule_instance.to_dict()
# create an instance of DaySchedule from a dict
day_schedule_from_dict = DaySchedule.from_dict(day_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


