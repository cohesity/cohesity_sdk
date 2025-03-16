# CommonBandwidthSettings

Specifies the common bandwidth setting of the External Target

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download** | [**BandwidthThrottling**](BandwidthThrottling.md) |  | [optional] 
**upload** | [**BandwidthThrottling**](BandwidthThrottling.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.common_bandwidth_settings import CommonBandwidthSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CommonBandwidthSettings from a JSON string
common_bandwidth_settings_instance = CommonBandwidthSettings.from_json(json)
# print the JSON string representation of the object
print(CommonBandwidthSettings.to_json())

# convert the object into a dict
common_bandwidth_settings_dict = common_bandwidth_settings_instance.to_dict()
# create an instance of CommonBandwidthSettings from a dict
common_bandwidth_settings_from_dict = CommonBandwidthSettings.from_dict(common_bandwidth_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


