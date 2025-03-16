# GetMcmProtectionGroupsActivityReqParams

Specifies the params to filter Protection Group activity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_types** | **List[str]** | Specifies the activity types. | [optional] 
**archival_run_params** | [**ProtectionGroupArchivalRunFilterParams**](ProtectionGroupArchivalRunFilterParams.md) |  | [optional] 
**backup_run_params** | [**ProtectionGroupBackupRunFilterParams**](ProtectionGroupBackupRunFilterParams.md) | Specifies the additional filters in case activity type is set to &#39;BackupRun&#39;. This does not apply to RPaaS. | [optional] 
**environments** | **List[str]** | Specifies the list of environments. | [optional] 
**from_time_usecs** | **int** | Specifies the time in Unix timestamp epoch in microsecond which filters all the activity started after this value. | [optional] 
**include_object_details** | **bool** | Specifies whether to include details for objects in response. By default this is false. | [optional] 
**protection_group_identifiers** | **List[str]** | Specifies the list of Protection Group identifiers to filter the activity. | [optional] 
**run_start_time_usecs** | **int** | Specifies the time in Unix timestamp epoch in microsecond which filters all the activity started at this time. | [optional] 
**statuses** | **List[str]** | Specifies the list of statuses to filter activity events. | [optional] 
**to_time_usecs** | **int** | Specifies the time in Unix timestamp epoch in microsecond which filters all the activity started before this value. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.get_mcm_protection_groups_activity_req_params import GetMcmProtectionGroupsActivityReqParams

# TODO update the JSON string below
json = "{}"
# create an instance of GetMcmProtectionGroupsActivityReqParams from a JSON string
get_mcm_protection_groups_activity_req_params_instance = GetMcmProtectionGroupsActivityReqParams.from_json(json)
# print the JSON string representation of the object
print(GetMcmProtectionGroupsActivityReqParams.to_json())

# convert the object into a dict
get_mcm_protection_groups_activity_req_params_dict = get_mcm_protection_groups_activity_req_params_instance.to_dict()
# create an instance of GetMcmProtectionGroupsActivityReqParams from a dict
get_mcm_protection_groups_activity_req_params_from_dict = GetMcmProtectionGroupsActivityReqParams.from_dict(get_mcm_protection_groups_activity_req_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


