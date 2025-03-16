# BackupRunSummary

Specifies summary information about local snapshot run across all objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancelled_app_objects_count** | **int** | Specifies the count of app objects for which backup was cancelled. | [optional] 
**cancelled_objects_count** | **int** | Specifies the count of objects for which backup was cancelled. | [optional] 
**data_lock** | **str** | This field is deprecated. Use DataLockConstraints field instead. | [optional] 
**data_lock_constraints** | [**DataLockConstraints**](DataLockConstraints.md) |  | [optional] 
**end_time_usecs** | **int** | Specifies the end time of backup run in Unix epoch Timestamp(in microseconds). | [optional] 
**failed_app_objects_count** | **int** | Specifies the count of app objects for which backup failed. | [optional] 
**failed_objects_count** | **int** | Specifies the count of objects for which backup failed. | [optional] 
**indexing_task_id** | **str** | Progress monitor task for indexing. | [optional] 
**is_sla_violated** | **bool** | Indicated if SLA has been violated for this run. | [optional] 
**local_snapshot_stats** | [**BackupDataStats**](BackupDataStats.md) |  | [optional] 
**local_task_id** | **str** | Task ID for a local protection run. | [optional] 
**messages** | **List[str]** | Message about the backup run. | [optional] 
**progress_task_id** | **str** | Progress monitor task id for local backup run. | [optional] 
**run_type** | **str** | Type of Protection Group run. &#39;kRegular&#39; indicates an incremental (CBT) backup. Incremental backups utilizing CBT (if supported) are captured of the target protection objects. The first run of a kRegular schedule captures all the blocks. &#39;kFull&#39; indicates a full (no CBT) backup. A complete backup (all blocks) of the target protection objects are always captured and Change Block Tracking (CBT) is not utilized. &#39;kLog&#39; indicates a Database Log backup. Capture the database transaction logs to allow rolling back to a specific point in time. &#39;kSystem&#39; indicates system volume backup. It produces an image for bare metal recovery. &#39;kStorageArraySnapshot&#39; indicates storage array snapshot backup. | [optional] 
**skipped_objects_count** | **int** | Specifies the count of objects for which backup was skipped. | [optional] 
**start_time_usecs** | **int** | Specifies the start time of backup run in Unix epoch Timestamp(in microseconds). | [optional] 
**stats_task_id** | **str** | Stats task id for local backup run. | [optional] 
**status** | **str** | Status of the backup run. &#39;Running&#39; indicates that the run is still running. &#39;Canceled&#39; indicates that the run has been canceled. &#39;Canceling&#39; indicates that the run is in the process of being canceled. &#39;Paused&#39; indicates that the ongoing run has been paused. &#39;Failed&#39; indicates that the run has failed. &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening. &#39;Succeeded&#39; indicates that the run has finished successfully. &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages. &#39;Skipped&#39; indicates that the run was skipped. | [optional] 
**successful_app_objects_count** | **int** | Specifies the count of app objects for which backup was successful. | [optional] 
**successful_objects_count** | **int** | Specifies the count of objects for which backup was successful. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.backup_run_summary import BackupRunSummary

# TODO update the JSON string below
json = "{}"
# create an instance of BackupRunSummary from a JSON string
backup_run_summary_instance = BackupRunSummary.from_json(json)
# print the JSON string representation of the object
print(BackupRunSummary.to_json())

# convert the object into a dict
backup_run_summary_dict = backup_run_summary_instance.to_dict()
# create an instance of BackupRunSummary from a dict
backup_run_summary_from_dict = BackupRunSummary.from_dict(backup_run_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


