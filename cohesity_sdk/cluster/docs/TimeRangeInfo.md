# TimeRangeInfo

Information about a set of disjoint, possibly annotated time ranges.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** | Error (if any) associated with the time range. | [optional] 
**time_ranges** | [**List[RecoveryTimeRangeInfo]**](RecoveryTimeRangeInfo.md) | The set of time ranges, each of which may be tagged with its job. These ranges will be non-overlapping and sorted by increasing start time. | [optional] 
**user_message** | **str** | User message (if any) associated with the time range. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.time_range_info import TimeRangeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TimeRangeInfo from a JSON string
time_range_info_instance = TimeRangeInfo.from_json(json)
# print the JSON string representation of the object
print(TimeRangeInfo.to_json())

# convert the object into a dict
time_range_info_dict = time_range_info_instance.to_dict()
# create an instance of TimeRangeInfo from a dict
time_range_info_from_dict = TimeRangeInfo.from_dict(time_range_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


