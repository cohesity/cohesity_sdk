# GetPITRangesProtectedObjectResponseBody

Specifies the points in time available for restore as a set of one or more time ranges. If the number of available ranges exceeds 1000, then the latest 1000 will be returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | Specifies the environment for which restore ranges are returned. | [optional] 
**oracle_restore_range_info** | [**OracleRestoreRangeInfo**](OracleRestoreRangeInfo.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.get_pit_ranges_protected_object_response_body import GetPITRangesProtectedObjectResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetPITRangesProtectedObjectResponseBody from a JSON string
get_pit_ranges_protected_object_response_body_instance = GetPITRangesProtectedObjectResponseBody.from_json(json)
# print the JSON string representation of the object
print(GetPITRangesProtectedObjectResponseBody.to_json())

# convert the object into a dict
get_pit_ranges_protected_object_response_body_dict = get_pit_ranges_protected_object_response_body_instance.to_dict()
# create an instance of GetPITRangesProtectedObjectResponseBody from a dict
get_pit_ranges_protected_object_response_body_from_dict = GetPITRangesProtectedObjectResponseBody.from_dict(get_pit_ranges_protected_object_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


