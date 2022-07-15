# SnapshotInfo

Snapshot info for an object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_id** | **str, none_type** | Snapshot id for a successful snapshot. This field will not be set if the Protection Group Run has no successful attempt. | [optional] 
**status** | **str, none_type** | Status of snapshot. | [optional] 
**status_message** | **str, none_type** | A message decribing the status. This will be populated currently only for kWaitingForOlderBackupRun status. | [optional] 
**start_time_usecs** | **int, none_type** | Specifies the start time of attempt in Unix epoch Timestamp(in microseconds) for an object. | [optional] 
**end_time_usecs** | **int, none_type** | Specifies the end time of attempt in Unix epoch Timestamp(in microseconds) for an object. | [optional] 
**admitted_time_usecs** | **int, none_type** | Specifies the time at which the backup task was admitted to run in Unix epoch Timestamp(in microseconds) for an object. | [optional] 
**permit_grant_time_usecs** | **int, none_type** | Specifies the time when gatekeeper permit is granted to the backup task. If the backup task is rescheduled due to errors, the field is updated to the time when permit is granted again. | [optional] 
**queue_duration_usecs** | **int, none_type** | Specifies the duration between the startTime and when gatekeeper permit is granted to the backup task. If the backup task is rescheduled due to errors, the field is updated considering the time when permit is granted again. Queue duration &#x3D; PermitGrantTimeUsecs - StartTimeUsecs | [optional] 
**snapshot_creation_time_usecs** | **int, none_type** | Specifies the time at which the source snapshot was taken in Unix epoch Timestamp(in microseconds) for an object. | [optional] 
**stats** | [**BackupDataStats**](BackupDataStats.md) |  | [optional] 
**progress_task_id** | **str, none_type** | Progress monitor task for an object. | [optional] 
**warnings** | **[str], none_type** | Specifies a list of warning messages. | [optional] 
**is_manually_deleted** | **bool, none_type** | Specifies whether the snapshot is deleted manually. | [optional] 
**expiry_time_usecs** | **int, none_type** | Specifies the expiry time of attempt in Unix epoch Timestamp (in microseconds) for an object. | [optional] 
**total_file_count** | **int, none_type** | The total number of file and directory entities visited in this backup. Only applicable to file based backups. | [optional] 
**backup_file_count** | **int, none_type** | The total number of file and directory entities that are backed up in this run. Only applicable to file based backups. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


