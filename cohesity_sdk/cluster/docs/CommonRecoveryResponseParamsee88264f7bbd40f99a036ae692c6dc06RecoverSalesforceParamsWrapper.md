# CommonRecoveryResponseParamsee88264f7bbd40f99a036ae692c6dc06RecoverSalesforceParamsWrapper


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Specifies the id of the Recovery. | [optional] 
**name** | **str, none_type** | Specifies the name of the Recovery. | [optional] 
**start_time_usecs** | **int, none_type** | Specifies the start time of the Recovery in Unix timestamp epoch in microseconds. | [optional] 
**end_time_usecs** | **int, none_type** | Specifies the end time of the Recovery in Unix timestamp epoch in microseconds. This field will be populated only after Recovery is finished. | [optional] 
**status** | **str, none_type** | Status of the Recovery. &#39;Running&#39; indicates that the Recovery is still running. &#39;Canceled&#39; indicates that the Recovery has been cancelled. &#39;Canceling&#39; indicates that the Recovery is in the process of being cancelled. &#39;Failed&#39; indicates that the Recovery has failed. &#39;Succeeded&#39; indicates that the Recovery has finished successfully. &#39;SucceededWithWarning&#39; indicates that the Recovery finished successfully, but there were some warning messages. &#39;Skipped&#39; indicates that the Recovery task was skipped. | [optional] 
**progress_task_id** | **str, none_type** | Progress monitor task id for Recovery. | [optional] 
**snapshot_environment** | **str** | Specifies the type of snapshot environment for which the Recovery was performed. | [optional] 
**recovery_action** | **str** | Specifies the type of recover action. | [optional] 
**permissions** | [**[Tenant], none_type**](Tenant.md) | Specifies the list of tenants that have permissions for this recovery. | [optional] 
**creation_info** | [**CreationInfo**](CreationInfo.md) |  | [optional] 
**can_tear_down** | **bool, none_type** | Specifies whether it&#39;s possible to tear down the objects created by the recovery. | [optional] 
**tear_down_status** | **str, none_type** | Specifies the status of the tear down operation. This is only set when the canTearDown is set to true. &#39;DestroyScheduled&#39; indicates that the tear down is ready to schedule. &#39;Destroying&#39; indicates that the tear down is still running. &#39;Destroyed&#39; indicates that the tear down succeeded. &#39;DestroyError&#39; indicates that the tear down failed. | [optional] 
**tear_down_message** | **str, none_type** | Specifies the error message about the tear down operation if it fails. | [optional] 
**messages** | **[str], none_type** | Specifies messages about the recovery. | [optional] 
**is_parent_recovery** | **bool, none_type** | Specifies whether the current recovery operation has created child recoveries. This is currently used in SQL recovery where multiple child recoveries can be tracked under a common/parent recovery. | [optional] 
**parent_recovery_id** | **str, none_type** | If current recovery is child recovery triggered by another parent recovery operation, then this field willt specify the id of the parent recovery. | [optional] 
**retrieve_archive_tasks** | [**[RetrieveArchiveTask], none_type**](RetrieveArchiveTask.md) | Specifies the list of persistent state of a retrieve of an archive task. | [optional] 
**is_multi_stage_restore** | **bool, none_type** | Specifies whether the current recovery operation is a multi-stage restore operation. This is currently used by VMware recoveres for the migration/hot-standby use case. | [optional] 
**sfdc_params** | [**RecoverSalesforceParams**](RecoverSalesforceParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


