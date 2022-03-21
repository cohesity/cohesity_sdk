# McmProtectionGroupActivity

Specifies the Protection Group activity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Specifies the unique id of the activity event. | [optional] 
**cluster_id** | **int, none_type** | Specifies the cluster id. | [optional] 
**cluster_incarnation_id** | **int, none_type** | Specifies the cluster incarnation id. | [optional] 
**cluster_name** | **str, none_type** | Specifies the cluster name. | [optional] 
**region_id** | **str, none_type** | Specifies the region id. | [optional] [readonly] 
**timestamp_usecs** | **int, none_type** | Specifies the timestamp in Unix timestamp epoch in microseconds at which this activity occured. | [optional] 
**run_id** | **str, none_type** | Specifies the ID of the Protection Run. | [optional] 
**protection_group_id** | **str, none_type** | Specifies the Protection Group Id. | [optional] 
**protection_group_name** | **str, none_type** | Specifies the Protection Group name. | [optional] 
**policy_id** | **str, none_type** | Specifies the Protection Policy Id. | [optional] 
**policy_name** | **str, none_type** | Specifies the Protection Policy Name. | [optional] 
**type** | **str, none_type** | Specifies the type of activity event. | [optional] 
**backup_run_params** | [**McmProtectionGroupBackupRunActivityParams**](McmProtectionGroupBackupRunActivityParams.md) |  | [optional] 
**archival_run_params** | [**McmProtectionGroupArchivalRunActivityParams**](McmProtectionGroupArchivalRunActivityParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


