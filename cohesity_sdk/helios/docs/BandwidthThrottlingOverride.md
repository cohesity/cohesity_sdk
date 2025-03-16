# BandwidthThrottlingOverride

Specifies a list of override bandwidth limits and time periods when those limits override the rateLimitBytesPerSec limit.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes_per_second** | **int** | Specifies the value for the specified time period. The value is specified in bytes per second. | [optional] 
**time_periods** | [**TimeOfAWeek**](TimeOfAWeek.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.bandwidth_throttling_override import BandwidthThrottlingOverride

# TODO update the JSON string below
json = "{}"
# create an instance of BandwidthThrottlingOverride from a JSON string
bandwidth_throttling_override_instance = BandwidthThrottlingOverride.from_json(json)
# print the JSON string representation of the object
print(BandwidthThrottlingOverride.to_json())

# convert the object into a dict
bandwidth_throttling_override_dict = bandwidth_throttling_override_instance.to_dict()
# create an instance of BandwidthThrottlingOverride from a dict
bandwidth_throttling_override_from_dict = BandwidthThrottlingOverride.from_dict(bandwidth_throttling_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


