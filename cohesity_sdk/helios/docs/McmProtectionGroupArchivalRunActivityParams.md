# McmProtectionGroupArchivalRunActivityParams

Specifies the Protection Group activity of an archival run.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_full_archive** | **bool, none_type** | Specifies if the archival run is full archive. | [optional] 
**start_time_usecs** | **int, none_type** | Specifies the start time of Run in Unix epoch Timestamp(in microseconds). | [optional] 
**end_time_usecs** | **int, none_type** | Specifies the end time of Run in Unix epoch Timestamp(in microseconds). | [optional] 
**status** | **str, none_type** | Status of the Run. &#39;Running&#39; indicates that the run is still running. &#39;Canceled&#39; indicates that the run has been canceled. &#39;Canceling&#39; indicates that the run is in the process of being canceled. &#39;Failed&#39; indicates that the run has failed. &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening. &#39;Succeeded&#39; indicates that the run has finished successfully. &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages. | [optional] 
**archival_target_id** | **int, none_type** | Specifies the id of archival target. | [optional] 
**archival_target_name** | **str, none_type** | Specifies the name of archival target. | [optional] 
**rpaas_region_id** | **str, none_type** | Specifies the region id for RPaaS. | [optional] [readonly] 
**protection_environment_type** | **str, none_type** | Specifies the type of protection environment. | [optional] 
**logical_size_bytes** | **int, none_type** | Specifies total logical size of the objects in bytes. | [optional] 
**physical_bytes_transferred** | **int, none_type** | Specifies total size of physical data in bytes transferred after archival. | [optional] 
**logical_bytes_transferred** | **int, none_type** | Specifies total size of logical data in bytes transferred after archival. | [optional] 
**error_code** | **str, none_type** | Specifies a short message describing the type of error which occurred. | [optional] 
**error_guid** | **str, none_type** | Specifies the identifier of the error code. | [optional] 
**message_codes** | **str, none_type** | Specifies the full text of the error message if any error occurs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


