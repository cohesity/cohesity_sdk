# TieringBandwidthSettings

Specifies the global bandwidth setting of the Tiering External Target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download** | [**BandwidthThrottling**](BandwidthThrottling.md) |  | [optional] 
**upload** | [**BandwidthThrottling**](BandwidthThrottling.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.tiering_bandwidth_settings import TieringBandwidthSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TieringBandwidthSettings from a JSON string
tiering_bandwidth_settings_instance = TieringBandwidthSettings.from_json(json)
# print the JSON string representation of the object
print(TieringBandwidthSettings.to_json())

# convert the object into a dict
tiering_bandwidth_settings_dict = tiering_bandwidth_settings_instance.to_dict()
# create an instance of TieringBandwidthSettings from a dict
tiering_bandwidth_settings_from_dict = TieringBandwidthSettings.from_dict(tiering_bandwidth_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


