# TimeSeriesStats

Specifies a list of time series stats.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_series_stats** | [**List[TimeSeriesStatsForMetric]**](TimeSeriesStatsForMetric.md) | Specifies the list of time series stats. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.time_series_stats import TimeSeriesStats

# TODO update the JSON string below
json = "{}"
# create an instance of TimeSeriesStats from a JSON string
time_series_stats_instance = TimeSeriesStats.from_json(json)
# print the JSON string representation of the object
print(TimeSeriesStats.to_json())

# convert the object into a dict
time_series_stats_dict = time_series_stats_instance.to_dict()
# create an instance of TimeSeriesStats from a dict
time_series_stats_from_dict = TimeSeriesStats.from_dict(time_series_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


