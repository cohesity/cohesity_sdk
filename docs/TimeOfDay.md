# TimeOfDay

Specifies the time of day. Used for scheduling purposes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hour** | **int** | Specifies the hour of the day (0-23). | 
**minute** | **int** | Specifies the minute of the hour (0-59). | 
**time_zone** | **str** | Specifies the time zone of the user. If not specified, default value is assumed as America/Los_Angeles. | [optional] [default to 'America/Los_Angeles']

## Example

```python
from cohesity_sdk.models.time_of_day import TimeOfDay

# TODO update the JSON string below
json = "{}"
# create an instance of TimeOfDay from a JSON string
time_of_day_instance = TimeOfDay.from_json(json)
# print the JSON string representation of the object
print(TimeOfDay.to_json())

# convert the object into a dict
time_of_day_dict = time_of_day_instance.to_dict()
# create an instance of TimeOfDay from a dict
time_of_day_from_dict = TimeOfDay.from_dict(time_of_day_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


