# ArchivalTargetResult

Archival result for an archival target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_id** | **int, none_type** | Specifies the archival target ID. | [optional] 
**archival_task_id** | **str, none_type** | Specifies the archival task id. This is a protection group UID which only applies when archival type is &#39;Tape&#39;. | [optional] 
**target_name** | **str, none_type** | Specifies the archival target name. | [optional] 
**target_type** | **str, none_type** | Specifies the archival target type. | [optional] 
**tier_settings** | [**ArchivalTargetTierInfo**](ArchivalTargetTierInfo.md) |  | [optional] 
**run_type** | **str, none_type** | Type of Protection Group run. &#39;kRegular&#39; indicates an incremental (CBT) backup. Incremental backups utilizing CBT (if supported) are captured of the target protection objects. The first run of a kRegular schedule captures all the blocks. &#39;kFull&#39; indicates a full (no CBT) backup. A complete backup (all blocks) of the target protection objects are always captured and Change Block Tracking (CBT) is not utilized. &#39;kLog&#39; indicates a Database Log backup. Capture the database transaction logs to allow rolling back to a specific point in time. &#39;kSystem&#39; indicates system volume backup. It produces an image for bare metal recovery. | [optional] 
**is_sla_violated** | **bool, none_type** | Indicated if SLA has been violated for this run. | [optional] 
**snapshot_id** | **str, none_type** | Snapshot id for a successful snapshot. This field will not be set if the archival Run fails to take the snapshot. | [optional] 
**start_time_usecs** | **int, none_type** | Specifies the start time of replication run in Unix epoch Timestamp(in microseconds) for an archival target. | [optional] 
**end_time_usecs** | **int, none_type** | Specifies the end time of replication run in Unix epoch Timestamp(in microseconds) for an archival target. | [optional] 
**queued_time_usecs** | **int, none_type** | Specifies the time when the archival is queued for schedule in Unix epoch Timestamp(in microseconds) for a target. | [optional] 
**is_incremental** | **bool, none_type** | Whether this is an incremental archive. If set to true, this is an incremental archive, otherwise this is a full archive. | [optional] 
**is_forever_incremental** | **bool, none_type** | Whether this is forever incremental or not | [optional] 
**status** | **str, none_type** | Status of the replication run for an archival target. &#39;Running&#39; indicates that the run is still running. &#39;Canceled&#39; indicates that the run has been canceled. &#39;Canceling&#39; indicates that the run is in the process of being canceled. &#39;Paused&#39; indicates that the ongoing run has been paused. &#39;Failed&#39; indicates that the run has failed. &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening. &#39;Succeeded&#39; indicates that the run has finished successfully. &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages. | [optional] 
**message** | **str, none_type** | Message about the archival run. | [optional] 
**progress_task_id** | **str, none_type** | Progress monitor task id for archival. | [optional] 
**indexing_task_id** | **str, none_type** | Progress monitor task for indexing. | [optional] 
**successful_objects_count** | **int, none_type** | Specifies the count of objects for which backup was successful. | [optional] 
**failed_objects_count** | **int, none_type** | Specifies the count of objects for which backup failed. | [optional] 
**cancelled_objects_count** | **int, none_type** | Specifies the count of objects for which backup was cancelled. | [optional] 
**successful_app_objects_count** | **int, none_type** | Specifies the count of app objects for which backup was successful. | [optional] 
**failed_app_objects_count** | **int, none_type** | Specifies the count of app objects for which backup failed. | [optional] 
**cancelled_app_objects_count** | **int, none_type** | Specifies the count of app objects for which backup was cancelled. | [optional] 
**stats** | [**ArchivalDataStats**](ArchivalDataStats.md) |  | [optional] 
**is_manually_deleted** | **bool, none_type** | Specifies whether the snapshot is deleted manually. | [optional] 
**expiry_time_usecs** | **int, none_type** | Specifies the expiry time of attempt in Unix epoch Timestamp (in microseconds). | [optional] 
**data_lock_constraints** | [**DataLockConstraints**](DataLockConstraints.md) |  | [optional] 
**on_legal_hold** | **bool, none_type** | Specifies the legal hold status for a archival target. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


