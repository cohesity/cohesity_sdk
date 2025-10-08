# FetchDirectoriesParams

Specifies the parameters required to fetch the subfolders and files of a directory.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dir_path** | **str** | DirPath is the full path of the directory whose contents need to be listed. | 
**attempt_num** | **int, none_type** | AttemptNum is the attempt number of the run that successfully created the snapshot. | [optional] 
**browse_indexed_data** | **bool, none_type** | Specifies whether to use indexed data for browse. | [optional] 
**cookie** | **str, none_type** | Cookie is used for paginating results. If the response returned partial results, it will also return a cookie that can be used to resume the listing. The value returned in response should be passed in the next call. The first call should not have this value set. Note that this value is only a suggestion and server is free to do a short read (return fewer entries along with a cookie). Please note that this should be used when browsing indexed data and does not apply otherwise. | [optional] 
**environment** | **str, none_type** | Specifies the environment. | [optional] 
**include_stat_file_entries** | **bool, none_type** | Specifies whether file stat data is returned. | [optional]  if omitted the server will use the default value of False
**max_entries** | **int, none_type** | MaxEntries is the maximum number of entries to return in this call. If there are more entries, server will return a cookie in the response that can be used to continue enumeration from the last call. The default value is 1000 i.e. If no value is specified, 1000 entries are returned. | [optional] 
**point_in_time_usecs** | **int, none_type** | PointInTimeUsecs is the time to read directory from previously available snapshot before this time. | [optional] 
**snapshot_id** | **str, none_type** | Specifies the snapshot that we are checking for the directories | [optional] 
**storage_domain_id** | **int, none_type** | Id of the Storage Domain if a View is being browsed. | [optional] 
**view_name** | **str, none_type** | Name of the View if a View is being browsed. | [optional] 
**volume_info_cookie** | **int, none_type** | VolumeInfoCookie is the cookie to be passed in calls to reading a directory for this volume. | [optional] 
**volume_name** | **str, none_type** | VolumeName is the name of the volume that needs to be browsed. This should match the name returned in VolumeInfo. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


