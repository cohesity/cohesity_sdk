# HourSchedule

Specifies settings that define a schedule for a Protection Group runs to start after certain number of hours.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **int** | Specifies a factor to multiply the unit by, to determine the backup schedule. &lt;br&gt; Example: If &#39;frequency&#39; set to 2 and the unit is &#39;Hours&#39;, then Snapshots are backed up every 2 hours. &lt;br&gt; This field is only applicable if unit is &#39;Minutes&#39;, &#39;Hours&#39; or &#39;Days&#39;. | 

## Example

```python
from cohesity_sdk.helios.models.hour_schedule import HourSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of HourSchedule from a JSON string
hour_schedule_instance = HourSchedule.from_json(json)
# print the JSON string representation of the object
print(HourSchedule.to_json())

# convert the object into a dict
hour_schedule_dict = hour_schedule_instance.to_dict()
# create an instance of HourSchedule from a dict
hour_schedule_from_dict = HourSchedule.from_dict(hour_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


