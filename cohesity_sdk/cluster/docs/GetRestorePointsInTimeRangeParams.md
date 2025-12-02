# GetRestorePointsInTimeRangeParams

Specifies the request parameters to restore points for time range API.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time_usecs** | **int** | Specifies the end time specified as a Unix epoch Timestamp in microseconds. | 
**protection_group_ids** | **[str]** | Specifies the jobs for which to get the full snapshot information | 
**start_time_usecs** | **int** | Specifies the start time specified as a Unix epoch Timestamp in microseconds. | 
**environment** | **str, none_type** | Specifies the protection source environment type. | [optional] 
**source_id** | **int, none_type** | Specifies the id of the Protection Source which is to be restored. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


