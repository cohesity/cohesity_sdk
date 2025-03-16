# CapacityTrendDatapointStats

Stats contained inside a data point of the capacity trend analysis chart.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_bytes** | **int** | Specifies the size of data corresponding to above tag. | [optional] 
**tag_info** | [**DataTieringTag**](DataTieringTag.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.capacity_trend_datapoint_stats import CapacityTrendDatapointStats

# TODO update the JSON string below
json = "{}"
# create an instance of CapacityTrendDatapointStats from a JSON string
capacity_trend_datapoint_stats_instance = CapacityTrendDatapointStats.from_json(json)
# print the JSON string representation of the object
print(CapacityTrendDatapointStats.to_json())

# convert the object into a dict
capacity_trend_datapoint_stats_dict = capacity_trend_datapoint_stats_instance.to_dict()
# create an instance of CapacityTrendDatapointStats from a dict
capacity_trend_datapoint_stats_from_dict = CapacityTrendDatapointStats.from_dict(capacity_trend_datapoint_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


