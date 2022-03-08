# GetMcmObjectsActivityReqParams

Specifies the params to filter object activity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_identifiers** | [**[McmObjectIdentifier], none_type**](McmObjectIdentifier.md) | Specifies the list of object identifiers to filter the activity. | [optional] 
**environments** | **[str], none_type** | Specifies the list of environments. | [optional] 
**statuses** | **[str], none_type** | Specifies the list of statuses to filter activity events. | [optional] 
**from_time_usecs** | **int, none_type** | Specifies the time in Unix timestamp epoch in microsecond which filters all the activity started after this value. | [optional] 
**to_time_usecs** | **int, none_type** | Specifies the time in Unix timestamp epoch in microsecond which filters all the activity started before this value. | [optional] 
**activity_types** | **[str], none_type** | Specifies the activity types. | [optional] 
**backup_run_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the additional filters in case activity type is set to &#39;BackupRun&#39;. | [optional] 
**archival_run_params** | [**ArchivalRunFilterParams**](ArchivalRunFilterParams.md) |  | [optional] 
**restore_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the additional filters in case activity type is set to &#39;Restore&#39;. | [optional] 
**exclude_data** | **bool, none_type** | Specifies whether to exclude activity information from the response. If not specified or false, activity information will be included. | [optional] 
**exclude_stats** | **bool, none_type** | Specifies whether to exclude stats information from the response. If not specified or false, stats information will be included. | [optional] 
**stats_params** | [**ActivityStatsParams**](ActivityStatsParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


