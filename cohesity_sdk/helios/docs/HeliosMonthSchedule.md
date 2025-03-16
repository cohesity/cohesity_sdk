# HeliosMonthSchedule

Specifies settings that define a schedule for a Protection Group runs to on specific week and specific days of that week.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_of_week** | **List[str]** | Specifies a list of days of the week when to start Protection Group Runs. &lt;br&gt; Example: To run a Protection Group on every Monday and Tuesday, set the schedule with following values: &lt;br&gt;  unit: &#39;Weeks&#39; &lt;br&gt;  dayOfWeek: [&#39;Monday&#39;,&#39;Tuesday&#39;] | [optional] 
**week_of_month** | **str** | Specifies the week of the month (such as &#39;Third&#39;) in a Monthly Schedule specified by unit field as &#39;Months&#39;. &lt;br&gt;This field is used in combination with &#39;dayOfWeek&#39; to define the day in the month to start the Protection Group Run. &lt;br&gt; Example: if &#39;weekOfMonth&#39; is set to &#39;Third&#39; and day is set to &#39;Monday&#39;, a backup is performed on the third Monday of every month. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_month_schedule import HeliosMonthSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosMonthSchedule from a JSON string
helios_month_schedule_instance = HeliosMonthSchedule.from_json(json)
# print the JSON string representation of the object
print(HeliosMonthSchedule.to_json())

# convert the object into a dict
helios_month_schedule_dict = helios_month_schedule_instance.to_dict()
# create an instance of HeliosMonthSchedule from a dict
helios_month_schedule_from_dict = HeliosMonthSchedule.from_dict(helios_month_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


