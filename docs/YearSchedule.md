# YearSchedule

Specifies settings that define a schedule for a Protection Group to run on specific year and specific day of that year.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_of_year** | **str** | Specifies the day of the Year (such as &#39;First&#39; or &#39;Last&#39;) in a Yearly Schedule. &lt;br&gt;This field is used to define the day in the year to start the Protection Group Run. &lt;br&gt; Example: if &#39;dayOfYear&#39; is set to &#39;First&#39;, a backup is performed on the first day of every year. &lt;br&gt; Example: if &#39;dayOfYear&#39; is set to &#39;Last&#39;, a backup is performed on the last day of every year. | 

## Example

```python
from cohesity_sdk.models.year_schedule import YearSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of YearSchedule from a JSON string
year_schedule_instance = YearSchedule.from_json(json)
# print the JSON string representation of the object
print(YearSchedule.to_json())

# convert the object into a dict
year_schedule_dict = year_schedule_instance.to_dict()
# create an instance of YearSchedule from a dict
year_schedule_from_dict = YearSchedule.from_dict(year_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


