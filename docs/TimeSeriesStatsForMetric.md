# TimeSeriesStatsForMetric

Specifies the time series stats for a metric.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_points** | [**List[DataPoint]**](DataPoint.md) | Specifies a list of data points. | [optional] 
**metric_name** | **str** | Specifies the metric name. | [optional] 
**type** | **str** | Specifies the type of the data points. | [optional] 

## Example

```python
from cohesity_sdk.models.time_series_stats_for_metric import TimeSeriesStatsForMetric

# TODO update the JSON string below
json = "{}"
# create an instance of TimeSeriesStatsForMetric from a JSON string
time_series_stats_for_metric_instance = TimeSeriesStatsForMetric.from_json(json)
# print the JSON string representation of the object
print(TimeSeriesStatsForMetric.to_json())

# convert the object into a dict
time_series_stats_for_metric_dict = time_series_stats_for_metric_instance.to_dict()
# create an instance of TimeSeriesStatsForMetric from a dict
time_series_stats_for_metric_from_dict = TimeSeriesStatsForMetric.from_dict(time_series_stats_for_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


