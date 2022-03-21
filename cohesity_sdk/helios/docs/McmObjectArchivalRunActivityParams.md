# McmObjectArchivalRunActivityParams

Specifies the Object activity of an archival run.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str, none_type** | Specifies the ID of the Protection Run. | [optional] 
**run_type** | **str, none_type** | Specifies the type of the Protection Run. | [optional] 
**protection_group_id** | **str, none_type** | Specifies the Protection Group Id. | [optional] 
**protection_group_name** | **str, none_type** | Specifies the Protection Group name. | [optional] 
**snapshot_id** | **str, none_type** | Specifies the id of the object snapshot that is created as a part of this Run. This field is only populated for runs which are successful. | [optional] 
**policy_id** | **str, none_type** | Specifies the Protection Policy Id. | [optional] 
**policy_name** | **str, none_type** | Specifies the Protection Policy Name. | [optional] 
**start_time_usecs** | **int, none_type** | Specifies the start time of Run in Unix epoch Timestamp(in microseconds). | [optional] 
**end_time_usecs** | **int, none_type** | Specifies the end time of Run in Unix epoch Timestamp(in microseconds). | [optional] 
**status** | **str, none_type** | Status of the Run. &#39;Running&#39; indicates that the run is still running. &#39;Canceled&#39; indicates that the run has been canceled. &#39;Canceling&#39; indicates that the run is in the process of being canceled. &#39;Failed&#39; indicates that the run has failed. &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening. &#39;Succeeded&#39; indicates that the run has finished successfully. &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages. | [optional] 
**progress_task_id** | **str, none_type** | Progress monitor task id for the Run. | [optional] 
**archival_target_id** | **int, none_type** | Specifies the id of archival target. | [optional] 
**archival_target_name** | **str, none_type** | Specifies the name of archival target. | [optional] 
**protection_environment_type** | **str, none_type** | Specifies the type of protection environment. | [optional] 
**is_stubbed_run** | **bool, none_type** | Specifies whether this is a stubbed run. This is set by the server and if set to true, this run entry specifies the user intent to create a run instead of actual run itself | [optional] 
**is_sla_violated** | **bool, none_type** | Indicated if SLA has been violated for this run. | [optional] 
**logical_size_bytes** | **int, none_type** | Specifies total logical size of the object in bytes. | [optional] 
**bytes_written** | **int, none_type** | Specifies total size of data in bytes written after taking backup. | [optional] 
**bytes_read** | **int, none_type** | Specifies total logical bytes read for creating the snapshot. | [optional] 
**message_code** | **str, none_type** | Specifies a short message describing the type of error which occurred. | [optional] 
**message_guid** | **str, none_type** | Specifies the identifier of the error code. | [optional] 
**error_message** | **str, none_type** | Specifies the full text of the error message if any error occurs. | [optional] 
**is_cloud_archival_direct** | **bool, none_type** | Specifies whether the run is a CAD run if cloud archive direct feature is enabled. If this field is true, the primary backup copy will only be available at the given archived location. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


