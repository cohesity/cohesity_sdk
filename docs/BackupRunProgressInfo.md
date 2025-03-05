# BackupRunProgressInfo

Specifies the progress of a local backup run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time_usecs** | **int** | Specifies the end time of the progress task in Unix epoch Timestamp(in microseconds). | [optional] 
**events** | [**List[ProgressTaskEvent]**](ProgressTaskEvent.md) | Specifies the event log created for progress Task. | [optional] 
**expected_remaining_time_usecs** | **int** | Specifies the expected remaining time of the progress task in Unix epoch Timestamp(in microseconds). | [optional] 
**percentage_completed** | **float** | Specifies the current completed percentage of the progress task. | [optional] 
**start_time_usecs** | **int** | Specifies the start time of the progress task in Unix epoch Timestamp(in microseconds). | [optional] 
**stats** | [**ProgressStats**](ProgressStats.md) |  | [optional] 
**status** | **str** | Specifies the current status of the progress task. | [optional] 
**objects** | [**List[ObjectProgressInfo]**](ObjectProgressInfo.md) | Specifies progress for objects. | [optional] 

## Example

```python
from cohesity_sdk.models.backup_run_progress_info import BackupRunProgressInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BackupRunProgressInfo from a JSON string
backup_run_progress_info_instance = BackupRunProgressInfo.from_json(json)
# print the JSON string representation of the object
print(BackupRunProgressInfo.to_json())

# convert the object into a dict
backup_run_progress_info_dict = backup_run_progress_info_instance.to_dict()
# create an instance of BackupRunProgressInfo from a dict
backup_run_progress_info_from_dict = BackupRunProgressInfo.from_dict(backup_run_progress_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


