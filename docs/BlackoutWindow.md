# BlackoutWindow

Specifies a time range in a single day when new Protection Group Runs of Protection Groups cannot be started. For example, a Protection Group with a daily schedule could define a blackout period for Sunday.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_id** | **str** | Specifies the unique identifier for the target getting added. This field need to be passed olny when policies are updated. | [optional] 
**day** | **str** | Specifies a day in the week when no new Protection Group Runs should be started such as &#39;Sunday&#39;. Specifies a day in a week such as &#39;Sunday&#39;, &#39;Monday&#39;, etc. | 
**end_time** | [**TimeOfDay**](TimeOfDay.md) |  | 
**start_time** | [**TimeOfDay**](TimeOfDay.md) |  | 

## Example

```python
from cohesity_sdk.models.blackout_window import BlackoutWindow

# TODO update the JSON string below
json = "{}"
# create an instance of BlackoutWindow from a JSON string
blackout_window_instance = BlackoutWindow.from_json(json)
# print the JSON string representation of the object
print(BlackoutWindow.to_json())

# convert the object into a dict
blackout_window_dict = blackout_window_instance.to_dict()
# create an instance of BlackoutWindow from a dict
blackout_window_from_dict = BlackoutWindow.from_dict(blackout_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


