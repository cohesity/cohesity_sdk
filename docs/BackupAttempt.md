# BackupAttempt

Specifies a backup attempt for an object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admitted_time_usecs** | **int** | Specifies the time at which the backup task was admitted to run in Unix epoch Timestamp(in microseconds) for an object. | [optional] 
**end_time_usecs** | **int** | Specifies the end time of attempt in Unix epoch Timestamp(in microseconds) for an object. | [optional] 
**message** | **str** | A message about the error if encountered while performing backup. | [optional] 
**permit_grant_time_usecs** | **int** | Specifies the time when gatekeeper permit is granted to the backup task. If the backup task is rescheduled due to errors, the field is updated to the time when permit is granted again. | [optional] 
**progress_task_id** | **str** | Progress monitor task for an object.. | [optional] 
**queue_duration_usecs** | **int** | Specifies the duration between the startTime and when gatekeeper permit is granted to the backup task. If the backup task is rescheduled due to errors, the field is updated considering the time when permit is granted again. Queue duration &#x3D; PermitGrantTimeUsecs - StartTimeUsecs | [optional] 
**snapshot_creation_time_usecs** | **int** | Specifies the time at which the source snapshot was taken in Unix epoch Timestamp(in microseconds) for an object. | [optional] 
**start_time_usecs** | **int** | Specifies the start time of attempt in Unix epoch Timestamp(in microseconds) for an object. | [optional] 
**stats** | [**BackupDataStats**](BackupDataStats.md) |  | [optional] 
**status** | **str** | Status of the attempt for an object. &#39;Running&#39; indicates that the run is still running. &#39;Canceled&#39; indicates that the run has been canceled. &#39;Canceling&#39; indicates that the run is in the process of being canceled. &#39;Paused&#39; indicates that the ongoing run has been paused. &#39;Pausing&#39; indicates that the ongoing run is in the process of being paused. &#39;Resuming&#39; indicates that the already paused run is in the process of being running again. &#39;Failed&#39; indicates that the run has failed. &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening. &#39;Succeeded&#39; indicates that the run has finished successfully. &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages. &#39;Skipped&#39; indicates that the run was skipped. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.backup_attempt import BackupAttempt

# TODO update the JSON string below
json = "{}"
# create an instance of BackupAttempt from a JSON string
backup_attempt_instance = BackupAttempt.from_json(json)
# print the JSON string representation of the object
print(BackupAttempt.to_json())

# convert the object into a dict
backup_attempt_dict = backup_attempt_instance.to_dict()
# create an instance of BackupAttempt from a dict
backup_attempt_from_dict = BackupAttempt.from_dict(backup_attempt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


