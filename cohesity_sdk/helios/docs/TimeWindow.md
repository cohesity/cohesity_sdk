# TimeWindow

Specifies a a time range within a day.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_of_the_week** | **str** | Specifies the week day. | [optional] 
**end_time** | [**Time**](Time.md) |  | [optional] 
**start_time** | [**Time**](Time.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.time_window import TimeWindow

# TODO update the JSON string below
json = "{}"
# create an instance of TimeWindow from a JSON string
time_window_instance = TimeWindow.from_json(json)
# print the JSON string representation of the object
print(TimeWindow.to_json())

# convert the object into a dict
time_window_dict = time_window_instance.to_dict()
# create an instance of TimeWindow from a dict
time_window_from_dict = TimeWindow.from_dict(time_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


