# ProtectionRunSummary

Specifies the summary of a protection run.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes_written** | **int, none_type** | Specifies total size of data in bytes written after taking backup. | [optional] 
**end_time_usecs** | **int, none_type** | Specifies the end time of backup run in Unix epoch Timestamp(in microseconds). | [optional] 
**environment** | **str, none_type** | Specifies the environment type of the Protection Group. | [optional] 
**id** | **str, none_type** | Specifies the ID of the Protection Group run. | [optional] 
**is_full_run** | **bool, none_type** | Specifies if the protection run is a full run. | [optional] 
**is_sla_violated** | **bool, none_type** | Indicated if SLA has been violated for this run. | [optional] 
**logical_size_bytes** | **int, none_type** | Specifies total logical size of object(s) in bytes. | [optional] 
**protection_group_id** | **str, none_type** | ProtectionGroupId to which this run belongs. | [optional] 
**protection_group_name** | **str, none_type** | Name of the Protection Group to which this run belongs. | [optional] 
**start_time_usecs** | **int, none_type** | Specifies the start time of backup run in Unix epoch Timestamp(in microseconds). | [optional] 
**status** | **str, none_type** | Status of the backup run. &#39;Running&#39; indicates that the run is still running. &#39;Canceled&#39; indicates that the run has been canceled. &#39;Canceling&#39; indicates that the run is in the process of being canceled. &#39;Paused&#39; indicates that the ongoing run has been paused. &#39;Failed&#39; indicates that the run has failed. &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening. &#39;Succeeded&#39; indicates that the run has finished successfully. &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages. &#39;Skipped&#39; indicates that the run was skipped. | [optional] 
**success_objects_count** | **int, none_type** | Specifies the number of objects which are successfully protected in this run. | [optional] 
**total_objects_count** | **int, none_type** | Specifies the total number of objects protected in this run. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


