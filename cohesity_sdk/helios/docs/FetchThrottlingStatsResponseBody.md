# FetchThrottlingStatsResponseBody

Specifies the throttling stats across various workloads and api types.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregated_stats** | [**List[ThrottlingStats]**](ThrottlingStats.md) | Specifies the time-series throttling stats for a single or multiple workloads in a source. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.fetch_throttling_stats_response_body import FetchThrottlingStatsResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of FetchThrottlingStatsResponseBody from a JSON string
fetch_throttling_stats_response_body_instance = FetchThrottlingStatsResponseBody.from_json(json)
# print the JSON string representation of the object
print(FetchThrottlingStatsResponseBody.to_json())

# convert the object into a dict
fetch_throttling_stats_response_body_dict = fetch_throttling_stats_response_body_instance.to_dict()
# create an instance of FetchThrottlingStatsResponseBody from a dict
fetch_throttling_stats_response_body_from_dict = FetchThrottlingStatsResponseBody.from_dict(fetch_throttling_stats_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


