# DataPoint

Specifies a data point.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**double_value** | **float** | Specifies the data point value in double format. | [optional] 
**int64_value** | **int** | Specifies the data point value in int64 format. | [optional] 
**string_value** | **str** | Specifies the data point value in string format. | [optional] 
**timestamp_msecs** | **int** | Specifies the timestamp of the data point. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.data_point import DataPoint

# TODO update the JSON string below
json = "{}"
# create an instance of DataPoint from a JSON string
data_point_instance = DataPoint.from_json(json)
# print the JSON string representation of the object
print(DataPoint.to_json())

# convert the object into a dict
data_point_dict = data_point_instance.to_dict()
# create an instance of DataPoint from a dict
data_point_from_dict = DataPoint.from_dict(data_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


