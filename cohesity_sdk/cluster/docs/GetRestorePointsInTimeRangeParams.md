# GetRestorePointsInTimeRangeParams

Specifies the request parameters to restore points for time range API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time_usecs** | **int** | Specifies the end time specified as a Unix epoch Timestamp in microseconds. | 
**environment** | **str** | Specifies the protection source environment type. | [optional] 
**protection_group_ids** | **List[str]** | Specifies the jobs for which to get the full snapshot information | 
**source_id** | **int** | Specifies the id of the Protection Source which is to be restored. | [optional] 
**start_time_usecs** | **int** | Specifies the start time specified as a Unix epoch Timestamp in microseconds. | 

## Example

```python
from cohesity_sdk.cluster.models.get_restore_points_in_time_range_params import GetRestorePointsInTimeRangeParams

# TODO update the JSON string below
json = "{}"
# create an instance of GetRestorePointsInTimeRangeParams from a JSON string
get_restore_points_in_time_range_params_instance = GetRestorePointsInTimeRangeParams.from_json(json)
# print the JSON string representation of the object
print(GetRestorePointsInTimeRangeParams.to_json())

# convert the object into a dict
get_restore_points_in_time_range_params_dict = get_restore_points_in_time_range_params_instance.to_dict()
# create an instance of GetRestorePointsInTimeRangeParams from a dict
get_restore_points_in_time_range_params_from_dict = GetRestorePointsInTimeRangeParams.from_dict(get_restore_points_in_time_range_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


