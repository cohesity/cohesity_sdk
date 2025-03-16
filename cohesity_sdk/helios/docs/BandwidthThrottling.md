# BandwidthThrottling

Specifies settings for limiting the data transfer rate between the local and remote Clusters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_limit_bytes_per_sec** | **int** | Specifies the maximum allowed data transfer rate between the local Cluster and remote Clusters. | [optional] 
**bandwidth_limit_overrides** | [**List[BandwidthThrottlingOverride]**](BandwidthThrottlingOverride.md) | Specifies the max rate limit at which we upload the data. | [optional] 
**timezone** | **str** | Specifies a time zone for the specified time period. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.bandwidth_throttling import BandwidthThrottling

# TODO update the JSON string below
json = "{}"
# create an instance of BandwidthThrottling from a JSON string
bandwidth_throttling_instance = BandwidthThrottling.from_json(json)
# print the JSON string representation of the object
print(BandwidthThrottling.to_json())

# convert the object into a dict
bandwidth_throttling_dict = bandwidth_throttling_instance.to_dict()
# create an instance of BandwidthThrottling from a dict
bandwidth_throttling_from_dict = BandwidthThrottling.from_dict(bandwidth_throttling_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


