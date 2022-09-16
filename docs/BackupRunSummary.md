# BackupRunSummary

Specifies summary information about local snapshot run across all objects.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_type** | **str, none_type** | Type of Protection Group run. &#39;kRegular&#39; indicates an incremental (CBT) backup. Incremental backups utilizing CBT (if supported) are captured of the target protection objects. The first run of a kRegular schedule captures all the blocks. &#39;kFull&#39; indicates a full (no CBT) backup. A complete backup (all blocks) of the target protection objects are always captured and Change Block Tracking (CBT) is not utilized. &#39;kLog&#39; indicates a Database Log backup. Capture the database transaction logs to allow rolling back to a specific point in time. &#39;kSystem&#39; indicates system volume backup. It produces an image for bare metal recovery. | [optional] 
**is_sla_violated** | **bool, none_type** | Indicated if SLA has been violated for this run. | [optional] 
**start_time_usecs** | **int, none_type** | Specifies the start time of backup run in Unix epoch Timestamp(in microseconds). | [optional] 
**end_time_usecs** | **int, none_type** | Specifies the end time of backup run in Unix epoch Timestamp(in microseconds). | [optional] 
**status** | **str, none_type** | Status of the backup run. &#39;Running&#39; indicates that the run is still running. &#39;Canceled&#39; indicates that the run has been canceled. &#39;Canceling&#39; indicates that the run is in the process of being canceled. &#39;Failed&#39; indicates that the run has failed. &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening. &#39;Succeeded&#39; indicates that the run has finished successfully. &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages. | [optional] 
**messages** | **[str], none_type** | Message about the backup run. | [optional] 
**successful_objects_count** | **int, none_type** | Specifies the count of objects for which backup was successful. | [optional] 
**failed_objects_count** | **int, none_type** | Specifies the count of objects for which backup failed. | [optional] 
**cancelled_objects_count** | **int, none_type** | Specifies the count of objects for which backup was cancelled. | [optional] 
**successful_app_objects_count** | **int, none_type** | Specifies the count of app objects for which backup was successful. | [optional] 
**failed_app_objects_count** | **int, none_type** | Specifies the count of app objects for which backup failed. | [optional] 
**cancelled_app_objects_count** | **int, none_type** | Specifies the count of app objects for which backup was cancelled. | [optional] 
**local_snapshot_stats** | [**BackupDataStats**](BackupDataStats.md) |  | [optional] 
**indexing_task_id** | **str, none_type** | Progress monitor task for indexing. | [optional] 
**progress_task_id** | **str, none_type** | Progress monitor task id for local backup run. | [optional] 
**data_lock** | **str, none_type** | This field is deprecated. Use DataLockConstraints field instead. | [optional] 
**local_task_id** | **str, none_type** | Task ID for a local protection run. | [optional] 
**data_lock_constraints** | [**DataLockConstraints**](DataLockConstraints.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


