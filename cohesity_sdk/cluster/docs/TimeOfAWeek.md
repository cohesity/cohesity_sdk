# TimeOfAWeek

Specifies a time period by specifying a single daily time period and one or more days of the week, for example 9 AM - 5 PM on Monday, Wednesday or Friday. If different time periods are required on different days, then multiple instances of this Weekly Time Period must be specified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **List[str]** | Array of Week Days. Specifies a list of days of a week (such as &#39;Sunday&#39;) when the time period should be applied. If not set, the time range applies to all days of the week. Specifies a day in a week such as &#39;Sunday&#39;, &#39;Monday&#39;, etc. | [optional] 
**end_time** | [**TimeOfDay**](TimeOfDay.md) |  | [optional] 
**is_all_day** | **bool** | All Day. Specifies that bandwidth limit is applied for entire day. | [optional] 
**start_time** | [**TimeOfDay**](TimeOfDay.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.time_of_a_week import TimeOfAWeek

# TODO update the JSON string below
json = "{}"
# create an instance of TimeOfAWeek from a JSON string
time_of_a_week_instance = TimeOfAWeek.from_json(json)
# print the JSON string representation of the object
print(TimeOfAWeek.to_json())

# convert the object into a dict
time_of_a_week_dict = time_of_a_week_instance.to_dict()
# create an instance of TimeOfAWeek from a dict
time_of_a_week_from_dict = TimeOfAWeek.from_dict(time_of_a_week_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


