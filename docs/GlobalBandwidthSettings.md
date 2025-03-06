# GlobalBandwidthSettings

Specifies the bandwidth setting of the External Target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_params** | [**CommonBandwidthSettings**](CommonBandwidthSettings.md) |  | [optional] 
**tiering_params** | [**CommonBandwidthSettings**](CommonBandwidthSettings.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.global_bandwidth_settings import GlobalBandwidthSettings

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalBandwidthSettings from a JSON string
global_bandwidth_settings_instance = GlobalBandwidthSettings.from_json(json)
# print the JSON string representation of the object
print(GlobalBandwidthSettings.to_json())

# convert the object into a dict
global_bandwidth_settings_dict = global_bandwidth_settings_instance.to_dict()
# create an instance of GlobalBandwidthSettings from a dict
global_bandwidth_settings_from_dict = GlobalBandwidthSettings.from_dict(global_bandwidth_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


