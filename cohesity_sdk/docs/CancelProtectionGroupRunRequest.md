# CancelProtectionGroupRunRequest

Specifies the request to cancel a protection run.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str, none_type** | Specifies a unique run id of the Protection Group run. | 
**local_task_id** | **str, none_type** | Specifies the task id of the local run. | [optional] 
**object_ids** | **[int], none_type** | List of entity ids for which we need to cancel the backup tasks. If this is provided it will not cancel the complete run but will cancel only subset of backup tasks (if backup tasks are cancelled correspoding copy task will also get cancelled). If the backup tasks are completed successfully it will not cancel those backup tasks. | [optional] 
**replication_task_id** | **[str], none_type** | Specifies the task id of the replication run. | [optional] 
**archival_task_id** | **[str], none_type** | Specifies the task id of the archival run. | [optional] 
**cloud_spin_task_id** | **[str], none_type** | Specifies the task id of the cloudSpin run. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


