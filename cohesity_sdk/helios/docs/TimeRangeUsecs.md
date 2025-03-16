# TimeRangeUsecs

Specifies a valid time range in micro seconds.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time_usecs** | **int** | Specifies the end time of this time range. | 
**start_time_usecs** | **int** | Specifies the start time of this time range. | 

## Example

```python
from cohesity_sdk.helios.models.time_range_usecs import TimeRangeUsecs

# TODO update the JSON string below
json = "{}"
# create an instance of TimeRangeUsecs from a JSON string
time_range_usecs_instance = TimeRangeUsecs.from_json(json)
# print the JSON string representation of the object
print(TimeRangeUsecs.to_json())

# convert the object into a dict
time_range_usecs_dict = time_range_usecs_instance.to_dict()
# create an instance of TimeRangeUsecs from a dict
time_range_usecs_from_dict = TimeRangeUsecs.from_dict(time_range_usecs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


