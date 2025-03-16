# McmObjectBackupRunActivityParams

Specifies the Object activity of a backup Run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes_read** | **int** | Specifies total logical bytes read for creating the snapshot. | [optional] 
**bytes_written** | **int** | Specifies total size of data in bytes written after taking backup. | [optional] 
**end_time_usecs** | **int** | Specifies the end time of Run in Unix epoch Timestamp(in microseconds). | [optional] 
**error_message** | **str** | Specifies the full text of the error message if any error occurs. | [optional] 
**is_sla_violated** | **bool** | Indicated if SLA has been violated for this run. | [optional] 
**is_stubbed_run** | **bool** | Specifies whether this is a stubbed run. This is set by the server and if set to true, this run entry specifies the user intent to create a run instead of actual run itself | [optional] 
**logical_size_bytes** | **int** | Specifies total logical size of the object in bytes. | [optional] 
**message_code** | **str** | Specifies a short message describing the type of error which occurred. | [optional] 
**message_guid** | **str** | Specifies the identifier of the error code. | [optional] 
**policy_id** | **str** | Specifies the Protection Policy Id. | [optional] 
**policy_name** | **str** | Specifies the Protection Policy Name. | [optional] 
**progress_task_id** | **str** | Progress monitor task id for the Run. | [optional] 
**protection_environment_type** | **str** | Specifies the type of protection environment. | [optional] 
**protection_group_id** | **str** | Specifies the Protection Group Id. | [optional] 
**protection_group_name** | **str** | Specifies the Protection Group name. | [optional] 
**run_id** | **str** | Specifies the ID of the Protection Run. | [optional] 
**snapshot_id** | **str** | Specifies the id of the object snapshot that is created as a part of this Run. This field is only populated for runs which are successful. | [optional] 
**start_time_usecs** | **int** | Specifies the start time of Run in Unix epoch Timestamp(in microseconds). | [optional] 
**status** | **str** | Status of the Run. &#39;Running&#39; indicates that the run is still running. &#39;Canceled&#39; indicates that the run has been canceled. &#39;Canceling&#39; indicates that the run is in the process of being canceled. &#39;Failed&#39; indicates that the run has failed. &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening. &#39;Succeeded&#39; indicates that the run has finished successfully. &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages. &#39;Skipped&#39; indicates that the run was skipped. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_object_backup_run_activity_params import McmObjectBackupRunActivityParams

# TODO update the JSON string below
json = "{}"
# create an instance of McmObjectBackupRunActivityParams from a JSON string
mcm_object_backup_run_activity_params_instance = McmObjectBackupRunActivityParams.from_json(json)
# print the JSON string representation of the object
print(McmObjectBackupRunActivityParams.to_json())

# convert the object into a dict
mcm_object_backup_run_activity_params_dict = mcm_object_backup_run_activity_params_instance.to_dict()
# create an instance of McmObjectBackupRunActivityParams from a dict
mcm_object_backup_run_activity_params_from_dict = McmObjectBackupRunActivityParams.from_dict(mcm_object_backup_run_activity_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


