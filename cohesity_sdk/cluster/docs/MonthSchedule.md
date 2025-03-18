# MonthSchedule

Specifies settings that define a schedule for a Protection Group runs to on specific week and specific days of that week.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_of_month** | **int** | Specifies the exact date of the month (such as 18) in a Monthly Schedule specified by unit field as &#39;Years&#39;. &lt;br&gt; Example: if &#39;dayOfMonth&#39; is set to &#39;18&#39;, a backup is performed on the 18th of every month. | [optional] 
**day_of_week** | **List[str]** | Specifies a list of days of the week when to start Protection Group Runs. &lt;br&gt; Example: To run a Protection Group on every Monday and Tuesday, set the schedule with following values: &lt;br&gt;  unit: &#39;Weeks&#39; &lt;br&gt;  dayOfWeek: [&#39;Monday&#39;,&#39;Tuesday&#39;] | [optional] 
**week_of_month** | **str** | Specifies the week of the month (such as &#39;Third&#39;) or nth day of month (such as &#39;First&#39; or &#39;Last&#39;) in a Monthly Schedule specified by unit field as &#39;Months&#39;. &lt;br&gt;This field can be used in combination with &#39;dayOfWeek&#39; to define the day in the month to start the Protection Group Run. &lt;br&gt; Example: if &#39;weekOfMonth&#39; is set to &#39;Third&#39; and day is set to &#39;Monday&#39;, a backup is performed on the third Monday of every month. &lt;br&gt; Example: if &#39;weekOfMonth&#39; is set to &#39;Last&#39; and dayOfWeek is not set, a backup is performed on the last day of every month. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.month_schedule import MonthSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of MonthSchedule from a JSON string
month_schedule_instance = MonthSchedule.from_json(json)
# print the JSON string representation of the object
print(MonthSchedule.to_json())

# convert the object into a dict
month_schedule_dict = month_schedule_instance.to_dict()
# create an instance of MonthSchedule from a dict
month_schedule_from_dict = MonthSchedule.from_dict(month_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


