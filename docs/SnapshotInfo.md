# SnapshotInfo

Snapshot info for an object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admitted_time_usecs** | **int** | Specifies the time at which the backup task was admitted to run in Unix epoch Timestamp(in microseconds) for an object. | [optional] 
**backup_file_count** | **int** | The total number of file and directory entities that are backed up in this run. Only applicable to file based backups. | [optional] 
**data_lock_constraints** | [**DataLockConstraints**](DataLockConstraints.md) |  | [optional] 
**end_time_usecs** | **int** | Specifies the end time of attempt in Unix epoch Timestamp(in microseconds) for an object. | [optional] 
**expiry_time_usecs** | **int** | Specifies the expiry time of attempt in Unix epoch Timestamp (in microseconds) for an object. | [optional] 
**indexing_task_id** | **str** | Progress monitor task for the indexing of documents in an object. | [optional] 
**is_manually_deleted** | **bool** | Specifies whether the snapshot is deleted manually. | [optional] 
**permit_grant_time_usecs** | **int** | Specifies the time when gatekeeper permit is granted to the backup task. If the backup task is rescheduled due to errors, the field is updated to the time when permit is granted again. | [optional] 
**progress_task_id** | **str** | Progress monitor task for backup of the object. | [optional] 
**queue_duration_usecs** | **int** | Specifies the duration between the startTime and when gatekeeper permit is granted to the backup task. If the backup task is rescheduled due to errors, the field is updated considering the time when permit is granted again. Queue duration &#x3D; PermitGrantTimeUsecs - StartTimeUsecs | [optional] 
**snapshot_creation_time_usecs** | **int** | Specifies the time at which the source snapshot was taken in Unix epoch Timestamp(in microseconds) for an object. | [optional] 
**snapshot_id** | **str** | Snapshot id for a successful snapshot. This field will not be set if the Protection Group Run has no successful attempt. | [optional] 
**start_time_usecs** | **int** | Specifies the start time of attempt in Unix epoch Timestamp(in microseconds) for an object. | [optional] 
**stats** | [**BackupDataStats**](BackupDataStats.md) |  | [optional] 
**stats_task_id** | **str** | Stats task for an object. | [optional] 
**status** | **str** | Status of snapshot. | [optional] 
**status_message** | **str** | A message decribing the status. This will be populated currently only for kWaitingForOlderBackupRun status. | [optional] 
**total_file_count** | **int** | The total number of file and directory entities visited in this backup. Only applicable to file based backups. | [optional] 
**warnings** | **List[str]** | Specifies a list of warning messages. | [optional] 

## Example

```python
from cohesity_sdk.models.snapshot_info import SnapshotInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotInfo from a JSON string
snapshot_info_instance = SnapshotInfo.from_json(json)
# print the JSON string representation of the object
print(SnapshotInfo.to_json())

# convert the object into a dict
snapshot_info_dict = snapshot_info_instance.to_dict()
# create an instance of SnapshotInfo from a dict
snapshot_info_from_dict = SnapshotInfo.from_dict(snapshot_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


