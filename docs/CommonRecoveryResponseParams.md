# CommonRecoveryResponseParams

Specifies the common response parameters to create a Recovery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_tear_down** | **bool** | Specifies whether it&#39;s possible to tear down the objects created by the recovery. | [optional] 
**creation_info** | [**CreationInfo**](CreationInfo.md) |  | [optional] 
**end_time_usecs** | **int** | Specifies the end time of the Recovery in Unix timestamp epoch in microseconds. This field will be populated only after Recovery is finished. | [optional] 
**id** | **str** | Specifies the id of the Recovery. | [optional] 
**is_multi_stage_restore** | **bool** | Specifies whether the current recovery operation is a multi-stage restore operation. This is currently used by VMware recoveres for the migration/hot-standby use case. | [optional] 
**is_parent_recovery** | **bool** | Specifies whether the current recovery operation has created child recoveries. This is currently used in SQL recovery where multiple child recoveries can be tracked under a common/parent recovery. | [optional] 
**messages** | **List[str]** | Specifies messages about the recovery. | [optional] 
**name** | **str** | Specifies the name of the Recovery. | [optional] 
**parent_recovery_id** | **str** | If current recovery is child recovery triggered by another parent recovery operation, then this field willt specify the id of the parent recovery. | [optional] 
**permissions** | [**List[TenantInfo]**](TenantInfo.md) | Specifies the list of tenants that have permissions for this recovery. | [optional] 
**progress_task_id** | **str** | Progress monitor task id for Recovery. | [optional] 
**recovery_action** | **str** | Specifies the type of recover action. | [optional] 
**retrieve_archive_tasks** | [**List[RetrieveArchiveTask]**](RetrieveArchiveTask.md) | Specifies the list of persistent state of a retrieve of an archive task. | [optional] 
**snapshot_environment** | **str** | Specifies the type of snapshot environment for which the Recovery was performed. | [optional] 
**start_time_usecs** | **int** | Specifies the start time of the Recovery in Unix timestamp epoch in microseconds. | [optional] 
**status** | **str** | Status of the Recovery. &#39;Running&#39; indicates that the Recovery is still running. &#39;Canceled&#39; indicates that the Recovery has been cancelled. &#39;Canceling&#39; indicates that the Recovery is in the process of being cancelled. &#39;Failed&#39; indicates that the Recovery has failed. &#39;Succeeded&#39; indicates that the Recovery has finished successfully. &#39;SucceededWithWarning&#39; indicates that the Recovery finished successfully, but there were some warning messages. &#39;Skipped&#39; indicates that the Recovery task was skipped. | [optional] 
**tear_down_message** | **str** | Specifies the error message about the tear down operation if it fails. | [optional] 
**tear_down_status** | **str** | Specifies the status of the tear down operation. This is only set when the canTearDown is set to true. &#39;DestroyScheduled&#39; indicates that the tear down is ready to schedule. &#39;Destroying&#39; indicates that the tear down is still running. &#39;Destroyed&#39; indicates that the tear down succeeded. &#39;DestroyError&#39; indicates that the tear down failed. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.common_recovery_response_params import CommonRecoveryResponseParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonRecoveryResponseParams from a JSON string
common_recovery_response_params_instance = CommonRecoveryResponseParams.from_json(json)
# print the JSON string representation of the object
print(CommonRecoveryResponseParams.to_json())

# convert the object into a dict
common_recovery_response_params_dict = common_recovery_response_params_instance.to_dict()
# create an instance of CommonRecoveryResponseParams from a dict
common_recovery_response_params_from_dict = CommonRecoveryResponseParams.from_dict(common_recovery_response_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


