# CapacityTrendAnalysis

Capacity Trend analysis of the requested sources in the given time range.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_point_vec** | [**List[CapacityTrendDatapoint]**](CapacityTrendDatapoint.md) | Vector of data points. Each data point contains statistics on analysis and downtiered data. | [optional] 
**last_updated_time_usecs** | **int** | Last updated time of capacity trend. | [optional] 

## Example

```python
from cohesity_sdk.models.capacity_trend_analysis import CapacityTrendAnalysis

# TODO update the JSON string below
json = "{}"
# create an instance of CapacityTrendAnalysis from a JSON string
capacity_trend_analysis_instance = CapacityTrendAnalysis.from_json(json)
# print the JSON string representation of the object
print(CapacityTrendAnalysis.to_json())

# convert the object into a dict
capacity_trend_analysis_dict = capacity_trend_analysis_instance.to_dict()
# create an instance of CapacityTrendAnalysis from a dict
capacity_trend_analysis_from_dict = CapacityTrendAnalysis.from_dict(capacity_trend_analysis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


