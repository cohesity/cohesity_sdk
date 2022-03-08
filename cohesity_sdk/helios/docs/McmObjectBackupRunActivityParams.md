# McmObjectBackupRunActivityParams

Specifies the Object activity of a backup Run.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str, none_type** | Specifies the ID of the Protection Run. | [optional] 
**protection_group_id** | **str, none_type** | Specifies the Protection Group Id. | [optional] 
**protection_group_name** | **str, none_type** | Specifies the Protection Group name. | [optional] 
**policy_id** | **str, none_type** | Specifies the Protection Policy Id. | [optional] 
**policy_name** | **str, none_type** | Specifies the Protection Policy Name. | [optional] 
**snapshot_id** | **str, none_type** | Specifies the id of the object snapshot that is created as a part of this Run. This field is only populated for runs which are successful. | [optional] 
**start_time_usecs** | **int, none_type** | Specifies the start time of Run in Unix epoch Timestamp(in microseconds). | [optional] 
**end_time_usecs** | **int, none_type** | Specifies the end time of Run in Unix epoch Timestamp(in microseconds). | [optional] 
**status** | **str, none_type** | Status of the Run. &#39;Running&#39; indicates that the run is still running. &#39;Canceled&#39; indicates that the run has been canceled. &#39;Canceling&#39; indicates that the run is in the process of being canceled. &#39;Failed&#39; indicates that the run has failed. &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening. &#39;Succeeded&#39; indicates that the run has finished successfully. &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages. | [optional] 
**progress_task_id** | **str, none_type** | Progress monitor task id for the Run. | [optional] 
**protection_environment_type** | **str, none_type** | Specifies the type of protection environment. | [optional] 
**is_stubbed_run** | **bool, none_type** | Specifies whether this is a stubbed run. This is set by the server and if set to true, this run entry specifies the user intent to create a run instead of actual run itself | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


