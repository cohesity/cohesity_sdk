# ArchivalTargetResult

Archival result for an archival target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_task_id** | **str** | Specifies the archival task id. This is a protection group UID which only applies when archival type is &#39;Tape&#39;. | [optional] 
**ownership_context** | **str** | Specifies the ownership context for the target. | [optional] 
**target_id** | **int** | Specifies the archival target ID. | [optional] 
**target_name** | **str** | Specifies the archival target name. | [optional] 
**target_type** | **str** | Specifies the archival target type. | [optional] 
**tier_settings** | [**ArchivalTargetTierInfo**](ArchivalTargetTierInfo.md) |  | [optional] 
**usage_type** | **str** | Specifies the usage type for the target. | [optional] 
**cancelled_app_objects_count** | **int** | Specifies the count of app objects for which backup was cancelled. | [optional] 
**cancelled_objects_count** | **int** | Specifies the count of objects for which backup was cancelled. | [optional] 
**data_lock_constraints** | [**DataLockConstraints**](DataLockConstraints.md) |  | [optional] 
**end_time_usecs** | **int** | Specifies the end time of replication run in Unix epoch Timestamp(in microseconds) for an archival target. | [optional] 
**expiry_time_usecs** | **int** | Specifies the expiry time of attempt in Unix epoch Timestamp (in microseconds). | [optional] 
**failed_app_objects_count** | **int** | Specifies the count of app objects for which backup failed. | [optional] 
**failed_objects_count** | **int** | Specifies the count of objects for which backup failed. | [optional] 
**indexing_task_id** | **str** | Progress monitor task for indexing. | [optional] 
**is_cad_archive** | **bool** | Whether this is CAD archive or not | [optional] 
**is_forever_incremental** | **bool** | Whether this is forever incremental or not | [optional] 
**is_incremental** | **bool** | Whether this is an incremental archive. If set to true, this is an incremental archive, otherwise this is a full archive. | [optional] 
**is_manually_deleted** | **bool** | Specifies whether the snapshot is deleted manually. | [optional] 
**is_sla_violated** | **bool** | Indicated if SLA has been violated for this run. | [optional] 
**message** | **str** | Message about the archival run. | [optional] 
**on_legal_hold** | **bool** | Specifies the legal hold status for a archival target. | [optional] 
**progress_task_id** | **str** | Progress monitor task id for archival. | [optional] 
**queued_time_usecs** | **int** | Specifies the time when the archival is queued for schedule in Unix epoch Timestamp(in microseconds) for a target. | [optional] 
**run_type** | **str** | Type of Protection Group run. &#39;kRegular&#39; indicates an incremental (CBT) backup. Incremental backups utilizing CBT (if supported) are captured of the target protection objects. The first run of a kRegular schedule captures all the blocks. &#39;kFull&#39; indicates a full (no CBT) backup. A complete backup (all blocks) of the target protection objects are always captured and Change Block Tracking (CBT) is not utilized. &#39;kLog&#39; indicates a Database Log backup. Capture the database transaction logs to allow rolling back to a specific point in time. &#39;kSystem&#39; indicates system volume backup. It produces an image for bare metal recovery. | [optional] 
**snapshot_id** | **str** | Snapshot id for a successful snapshot. This field will not be set if the archival Run fails to take the snapshot. | [optional] 
**start_time_usecs** | **int** | Specifies the start time of replication run in Unix epoch Timestamp(in microseconds) for an archival target. | [optional] 
**stats** | [**ArchivalDataStats**](ArchivalDataStats.md) |  | [optional] 
**stats_task_id** | **str** | Run Stats task id for archival. | [optional] 
**status** | **str** | Status of the replication run for an archival target. &#39;Running&#39; indicates that the run is still running. &#39;Canceled&#39; indicates that the run has been canceled. &#39;Canceling&#39; indicates that the run is in the process of being canceled. &#39;Paused&#39; indicates that the ongoing run has been paused. &#39;Failed&#39; indicates that the run has failed. &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening. &#39;Succeeded&#39; indicates that the run has finished successfully. &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages. &#39;Skipped&#39; indicates that the run was skipped. | [optional] 
**successful_app_objects_count** | **int** | Specifies the count of app objects for which backup was successful. | [optional] 
**successful_objects_count** | **int** | Specifies the count of objects for which backup was successful. | [optional] 
**worm_properties** | [**WormProperties**](WormProperties.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.archival_target_result import ArchivalTargetResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArchivalTargetResult from a JSON string
archival_target_result_instance = ArchivalTargetResult.from_json(json)
# print the JSON string representation of the object
print(ArchivalTargetResult.to_json())

# convert the object into a dict
archival_target_result_dict = archival_target_result_instance.to_dict()
# create an instance of ArchivalTargetResult from a dict
archival_target_result_from_dict = ArchivalTargetResult.from_dict(archival_target_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


