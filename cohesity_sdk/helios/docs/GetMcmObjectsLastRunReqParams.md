# GetMcmObjectsLastRunReqParams

Specifies the params to filter object last run activities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_types** | **List[str]** | Specifies the activity types. | [optional] 
**archival_run_params** | [**ArchivalRunFilterParams**](ArchivalRunFilterParams.md) |  | [optional] 
**backup_run_params** | [**BackupRunFilterParams**](BackupRunFilterParams.md) | Specifies the additional filters in case activity type is set to &#39;BackupRun&#39;. | [optional] 
**environments** | **List[str]** | Specifies the list of environments. | [optional] 
**exclude_data** | **bool** | Specifies whether to exclude activity information from the response. If not specified or false, activity information will be included. | [optional] 
**exclude_stats** | **bool** | Specifies whether to exclude stats information from the response. If not specified or false, stats information will be included. | [optional] 
**include_details** | **bool** | Specifies whether the response should return activity details. If this is true, all activity info will be returned. Otherwise only object id, activity id, status and sla info will be returned. If not specified, default is false. | [optional] 
**is_protected** | **bool** | Specifies whether to return runs for only protected objects. By default it&#39;s false. | [optional] 
**is_sla_violated** | **bool** | Specifies whether the last run violated sla. | [optional] 
**object_identifiers** | [**List[McmObjectIdentifier]**](McmObjectIdentifier.md) | Specifies the list of object identifiers, only last runs for these objects will be returned. | [optional] 
**source_identifier** | [**McmObjectIdentifier**](McmObjectIdentifier.md) |  | [optional] 
**stats_params** | [**ActivityStatsParams**](ActivityStatsParams.md) |  | [optional] 
**statuses** | **List[str]** | Specifies the list of statuses to filter activity events. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.get_mcm_objects_last_run_req_params import GetMcmObjectsLastRunReqParams

# TODO update the JSON string below
json = "{}"
# create an instance of GetMcmObjectsLastRunReqParams from a JSON string
get_mcm_objects_last_run_req_params_instance = GetMcmObjectsLastRunReqParams.from_json(json)
# print the JSON string representation of the object
print(GetMcmObjectsLastRunReqParams.to_json())

# convert the object into a dict
get_mcm_objects_last_run_req_params_dict = get_mcm_objects_last_run_req_params_instance.to_dict()
# create an instance of GetMcmObjectsLastRunReqParams from a dict
get_mcm_objects_last_run_req_params_from_dict = GetMcmObjectsLastRunReqParams.from_dict(get_mcm_objects_last_run_req_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


