# BgpTimers

BGP protocol timers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hold_time** | **int** | Hold time in seconds. | [optional] 
**keep_alive** | **int** | Keep alive interval in seconds. | [optional] 

## Example

```python
from cohesity_sdk.models.bgp_timers import BgpTimers

# TODO update the JSON string below
json = "{}"
# create an instance of BgpTimers from a JSON string
bgp_timers_instance = BgpTimers.from_json(json)
# print the JSON string representation of the object
print(BgpTimers.to_json())

# convert the object into a dict
bgp_timers_dict = bgp_timers_instance.to_dict()
# create an instance of BgpTimers from a dict
bgp_timers_from_dict = BgpTimers.from_dict(bgp_timers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


