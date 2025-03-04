# TargetBandwidthThrottlings

Specifies the bandwidth throttling setting of the External Target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download** | [**BandwidthThrottling**](BandwidthThrottling.md) |  | [optional] 
**upload** | [**BandwidthThrottling**](BandwidthThrottling.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.target_bandwidth_throttlings import TargetBandwidthThrottlings

# TODO update the JSON string below
json = "{}"
# create an instance of TargetBandwidthThrottlings from a JSON string
target_bandwidth_throttlings_instance = TargetBandwidthThrottlings.from_json(json)
# print the JSON string representation of the object
print(TargetBandwidthThrottlings.to_json())

# convert the object into a dict
target_bandwidth_throttlings_dict = target_bandwidth_throttlings_instance.to_dict()
# create an instance of TargetBandwidthThrottlings from a dict
target_bandwidth_throttlings_from_dict = TargetBandwidthThrottlings.from_dict(target_bandwidth_throttlings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


