# ArchivalBandwidthSettings

Specifies the global bandwidth setting of the Archival External Target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download** | [**BandwidthThrottling**](BandwidthThrottling.md) |  | [optional] 
**upload** | [**BandwidthThrottling**](BandwidthThrottling.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.archival_bandwidth_settings import ArchivalBandwidthSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ArchivalBandwidthSettings from a JSON string
archival_bandwidth_settings_instance = ArchivalBandwidthSettings.from_json(json)
# print the JSON string representation of the object
print(ArchivalBandwidthSettings.to_json())

# convert the object into a dict
archival_bandwidth_settings_dict = archival_bandwidth_settings_instance.to_dict()
# create an instance of ArchivalBandwidthSettings from a dict
archival_bandwidth_settings_from_dict = ArchivalBandwidthSettings.from_dict(archival_bandwidth_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


