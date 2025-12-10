# GetRestorePointsInTimeRangeResponse

Specifies the model for the response returned by RestorePointsForTimeRange API

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_snapshot_info** | [**List[FullSnapshotInfo]**](FullSnapshotInfo.md) | Specifies the info related to the recovery object. | [optional] 
**time_range_info** | [**TimeRangeInfo**](TimeRangeInfo.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.get_restore_points_in_time_range_response import GetRestorePointsInTimeRangeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRestorePointsInTimeRangeResponse from a JSON string
get_restore_points_in_time_range_response_instance = GetRestorePointsInTimeRangeResponse.from_json(json)
# print the JSON string representation of the object
print(GetRestorePointsInTimeRangeResponse.to_json())

# convert the object into a dict
get_restore_points_in_time_range_response_dict = get_restore_points_in_time_range_response_instance.to_dict()
# create an instance of GetRestorePointsInTimeRangeResponse from a dict
get_restore_points_in_time_range_response_from_dict = GetRestorePointsInTimeRangeResponse.from_dict(get_restore_points_in_time_range_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


