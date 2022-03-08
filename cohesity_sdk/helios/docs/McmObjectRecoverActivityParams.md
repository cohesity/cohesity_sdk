# McmObjectRecoverActivityParams

Specifies the Object activity of a recovery.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Specifies the id of the Recovery. | [optional] 
**name** | **str, none_type** | Specifies the name of the Recovery. | [optional] 
**start_time_usecs** | **int, none_type** | Specifies the start time of the Recovery in Unix timestamp epoch in microseconds. | [optional] 
**end_time_usecs** | **int, none_type** | Specifies the end time of the Recovery in Unix timestamp epoch in microseconds. This field will be populated only after Recovery is finished. | [optional] 
**status** | **str, none_type** | Status of the Recovery. &#39;Running&#39; indicates that the Recovery is still running. &#39;Canceled&#39; indicates that the Recovery has been cancelled. &#39;Canceling&#39; indicates that the Recovery is in the process of being cancelled. &#39;Failed&#39; indicates that the Recovery has failed. &#39;Succeeded&#39; indicates that the Recovery has finished successfully. &#39;SucceededWithWarning&#39; indicates that the Recovery finished successfully, but there were some warning messages. | [optional] 
**progress_task_id** | **str, none_type** | Progress monitor task id for Recovery. | [optional] 
**recovery_type** | **str, none_type** | Specifies the recovery type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


