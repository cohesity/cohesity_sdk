# HeliosDaySchedule

Specifies settings that define a schedule for a Protection Group runs to start after certain number of days.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **int** | Specifies a factor to multiply the unit by, to determine the backup schedule. &lt;br&gt; Example: If &#39;frequency&#39; set to 2 and the unit is &#39;Hours&#39;, then Snapshots are backed up every 2 hours. If selected unit is &#39;Weeks&#39; or &#39;Months&#39; then frequency will only be applied if policy type is DMaas. | 

## Example

```python
from cohesity_sdk.helios.models.helios_day_schedule import HeliosDaySchedule

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosDaySchedule from a JSON string
helios_day_schedule_instance = HeliosDaySchedule.from_json(json)
# print the JSON string representation of the object
print(HeliosDaySchedule.to_json())

# convert the object into a dict
helios_day_schedule_dict = helios_day_schedule_instance.to_dict()
# create an instance of HeliosDaySchedule from a dict
helios_day_schedule_from_dict = HeliosDaySchedule.from_dict(helios_day_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


