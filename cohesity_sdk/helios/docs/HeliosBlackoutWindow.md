# HeliosBlackoutWindow

List of Blackout Windows. If specified, this field defines blackout periods when backups are not triggered..

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_id** | **str** | Specifies the unique identifier for the blackout getting added. This field should only be set if policy is getting updated. | [optional] 
**day** | **str** | Specifies a day in the week when no new Protection Group Runs should be started such as &#39;Sunday&#39;. Specifies a day in a week such as &#39;Sunday&#39;, &#39;Monday&#39;, etc. | 
**end_time** | [**TimeOfDay**](TimeOfDay.md) |  | 
**start_time** | [**TimeOfDay**](TimeOfDay.md) |  | 

## Example

```python
from cohesity_sdk.helios.models.helios_blackout_window import HeliosBlackoutWindow

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosBlackoutWindow from a JSON string
helios_blackout_window_instance = HeliosBlackoutWindow.from_json(json)
# print the JSON string representation of the object
print(HeliosBlackoutWindow.to_json())

# convert the object into a dict
helios_blackout_window_dict = helios_blackout_window_instance.to_dict()
# create an instance of HeliosBlackoutWindow from a dict
helios_blackout_window_from_dict = HeliosBlackoutWindow.from_dict(helios_blackout_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


