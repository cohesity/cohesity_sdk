# GetMcmObjectsLastRunReqParams

Specifies the params to filter object last run activities.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_identifiers** | [**[McmObjectIdentifier], none_type**](McmObjectIdentifier.md) | Specifies the list of object identifiers, only last runs for these objects will be returned. | [optional] 
**environments** | **[str], none_type** | Specifies the list of environments. | [optional] 
**statuses** | **[str], none_type** | Specifies the list of statuses to filter activity events. | [optional] 
**is_sla_violated** | **bool, none_type** | Specifies whether the last run violated sla. | [optional] 
**source_identifier** | [**McmObjectIdentifier**](McmObjectIdentifier.md) |  | [optional] 
**activity_types** | **[str], none_type** | Specifies the activity types. | [optional] 
**backup_run_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the additional filters in case activity type is set to &#39;BackupRun&#39;. | [optional] 
**archival_run_params** | [**ArchivalRunFilterParams**](ArchivalRunFilterParams.md) |  | [optional] 
**include_details** | **bool, none_type** | Specifies whether the response should return activity details. If this is true, all activity info will be returned. Otherwise only object id, activity id, status and sla info will be returned. If not specified, default is false. | [optional] 
**is_protected** | **bool, none_type** | Specifies whether to return runs for only protected objects. By default it&#39;s false. | [optional] 
**exclude_data** | **bool, none_type** | Specifies whether to exclude activity information from the response. If not specified or false, activity information will be included. | [optional] 
**exclude_stats** | **bool, none_type** | Specifies whether to exclude stats information from the response. If not specified or false, stats information will be included. | [optional] 
**stats_params** | [**ActivityStatsParams**](ActivityStatsParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


