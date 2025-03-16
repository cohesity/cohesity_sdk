# McmProtectionGroupBackupRunActivityParams

Specifies the Protection Group activity of a backup Run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes_read** | **int** | Specifies total logical bytes read for creating the snapshot. | [optional] 
**bytes_written** | **int** | Specifies total size of data in bytes written after taking backup. | [optional] 
**end_time_usecs** | **int** | Specifies the end time of Run in Unix epoch Timestamp(in microseconds). | [optional] 
**error_code** | **str** | Specifies a short message describing the type of error which occurred. | [optional] 
**error_guid** | **str** | Specifies the identifier of the error code. | [optional] 
**is_sla_violated** | **bool** | Indicated if SLA has been violated for this run. | [optional] 
**logical_size_bytes** | **int** | Specifies total logical size of the object in bytes. | [optional] 
**message_codes** | **str** | Specifies the full text of the error message if any error occurs. | [optional] 
**objects** | [**List[McmObjectRunResult]**](McmObjectRunResult.md) | Specifies the objects details for the run. | [optional] 
**protection_environment_type** | **str** | Specifies the type of protection environment. | [optional] 
**start_time_usecs** | **int** | Specifies the start time of Run in Unix epoch Timestamp(in microseconds). | [optional] 
**status** | **str** | Status of the Run. &#39;Running&#39; indicates that the run is still running. &#39;Canceled&#39; indicates that the run has been canceled. &#39;Canceling&#39; indicates that the run is in the process of being canceled. &#39;Failed&#39; indicates that the run has failed. &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening. &#39;Succeeded&#39; indicates that the run has finished successfully. &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages. &#39;Skipped&#39; indicates that the run was skipped. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_protection_group_backup_run_activity_params import McmProtectionGroupBackupRunActivityParams

# TODO update the JSON string below
json = "{}"
# create an instance of McmProtectionGroupBackupRunActivityParams from a JSON string
mcm_protection_group_backup_run_activity_params_instance = McmProtectionGroupBackupRunActivityParams.from_json(json)
# print the JSON string representation of the object
print(McmProtectionGroupBackupRunActivityParams.to_json())

# convert the object into a dict
mcm_protection_group_backup_run_activity_params_dict = mcm_protection_group_backup_run_activity_params_instance.to_dict()
# create an instance of McmProtectionGroupBackupRunActivityParams from a dict
mcm_protection_group_backup_run_activity_params_from_dict = McmProtectionGroupBackupRunActivityParams.from_dict(mcm_protection_group_backup_run_activity_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


