# GetMcmObjectsActivityReqParams

Specifies the params to filter object activity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_types** | **List[str]** | Specifies the activity types. | [optional] 
**archival_run_params** | [**ArchivalRunFilterParams**](ArchivalRunFilterParams.md) |  | [optional] 
**backup_run_params** | [**BackupRunFilterParams**](BackupRunFilterParams.md) | Specifies the additional filters in case activity type is set to &#39;BackupRun&#39;. | [optional] 
**environments** | **List[str]** | Specifies the list of environments. | [optional] 
**exclude_data** | **bool** | Specifies whether to exclude activity information from the response. If not specified or false, activity information will be included. | [optional] 
**exclude_stats** | **bool** | Specifies whether to exclude stats information from the response. If not specified or false, stats information will be included. | [optional] 
**from_time_usecs** | **int** | Specifies the time in Unix timestamp epoch in microsecond which filters all the activity started after this value. | [optional] 
**is_sla_violated** | **bool** | Specifies whether to only return activities which violated SLA. Default is false. | [optional] 
**message_codes** | **List[str]** | Specifies the error codes to filter backup runs. | [optional] 
**object_identifiers** | [**List[McmObjectIdentifier]**](McmObjectIdentifier.md) | Specifies the list of object identifiers to filter the activity. | [optional] 
**restore_params** | [**RestoreFilterParams**](RestoreFilterParams.md) | Specifies the additional filters in case activity type is set to &#39;Restore&#39;. | [optional] 
**stats_params** | [**ActivityStatsParams**](ActivityStatsParams.md) |  | [optional] 
**statuses** | **List[str]** | Specifies the list of statuses to filter activity events. | [optional] 
**to_time_usecs** | **int** | Specifies the time in Unix timestamp epoch in microsecond which filters all the activity started before this value. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.get_mcm_objects_activity_req_params import GetMcmObjectsActivityReqParams

# TODO update the JSON string below
json = "{}"
# create an instance of GetMcmObjectsActivityReqParams from a JSON string
get_mcm_objects_activity_req_params_instance = GetMcmObjectsActivityReqParams.from_json(json)
# print the JSON string representation of the object
print(GetMcmObjectsActivityReqParams.to_json())

# convert the object into a dict
get_mcm_objects_activity_req_params_dict = get_mcm_objects_activity_req_params_instance.to_dict()
# create an instance of GetMcmObjectsActivityReqParams from a dict
get_mcm_objects_activity_req_params_from_dict = GetMcmObjectsActivityReqParams.from_dict(get_mcm_objects_activity_req_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


