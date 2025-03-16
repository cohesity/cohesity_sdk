# HeliosWeekSchedule

Specifies settings that define a schedule for a Protection Group runs to start on certain days of week.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_of_week** | **List[str]** | Specifies a list of days of the week when to start Protection Group Runs. &lt;br&gt; Example: To run a Protection Group on every Monday and Tuesday, set the schedule with following values: &lt;br&gt;  unit: &#39;Weeks&#39; &lt;br&gt;  dayOfWeek: [&#39;Monday&#39;,&#39;Tuesday&#39;] | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_week_schedule import HeliosWeekSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosWeekSchedule from a JSON string
helios_week_schedule_instance = HeliosWeekSchedule.from_json(json)
# print the JSON string representation of the object
print(HeliosWeekSchedule.to_json())

# convert the object into a dict
helios_week_schedule_dict = helios_week_schedule_instance.to_dict()
# create an instance of HeliosWeekSchedule from a dict
helios_week_schedule_from_dict = HeliosWeekSchedule.from_dict(helios_week_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


