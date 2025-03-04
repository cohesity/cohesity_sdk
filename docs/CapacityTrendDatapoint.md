# CapacityTrendDatapoint

A data point for the capacity trend analysis chart.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_point_stats** | [**List[CapacityTrendDatapointStats]**](CapacityTrendDatapointStats.md) | Specifies an array of tag and its corresponding statistic. | [optional] 
**data_point_timestamp** | **int** | Specifies the timestamp of this data point. | [optional] 
**error_messages** | **List[str]** | Specifies error messages, if any error is encountered while fetching the datapoint stats. | [optional] 

## Example

```python
from cohesity_sdk.models.capacity_trend_datapoint import CapacityTrendDatapoint

# TODO update the JSON string below
json = "{}"
# create an instance of CapacityTrendDatapoint from a JSON string
capacity_trend_datapoint_instance = CapacityTrendDatapoint.from_json(json)
# print the JSON string representation of the object
print(CapacityTrendDatapoint.to_json())

# convert the object into a dict
capacity_trend_datapoint_dict = capacity_trend_datapoint_instance.to_dict()
# create an instance of CapacityTrendDatapoint from a dict
capacity_trend_datapoint_from_dict = CapacityTrendDatapoint.from_dict(capacity_trend_datapoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


