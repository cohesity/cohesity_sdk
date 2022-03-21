# GetMcmProtectionGroupsActivityReqParams

Specifies the params to filter Protection Group activity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protection_group_identifiers** | **[str], none_type** | Specifies the list of Protection Group identifiers to filter the activity. | [optional] 
**environments** | **[str], none_type** | Specifies the list of environments. | [optional] 
**statuses** | **[str], none_type** | Specifies the list of statuses to filter activity events. | [optional] 
**run_start_time_usecs** | **int, none_type** | Specifies the time in Unix timestamp epoch in microsecond which filters all the activity started at this time. | [optional] 
**from_time_usecs** | **int, none_type** | Specifies the time in Unix timestamp epoch in microsecond which filters all the activity started after this value. | [optional] 
**to_time_usecs** | **int, none_type** | Specifies the time in Unix timestamp epoch in microsecond which filters all the activity started before this value. | [optional] 
**activity_types** | **[str], none_type** | Specifies the activity types. | [optional] 
**include_object_details** | **bool, none_type** | Specifies whether to include details for objects in response. By default this is false. | [optional] 
**backup_run_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the additional filters in case activity type is set to &#39;BackupRun&#39;. This does not apply to RPaaS. | [optional] 
**archival_run_params** | [**ProtectionGroupArchivalRunFilterParams**](ProtectionGroupArchivalRunFilterParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


