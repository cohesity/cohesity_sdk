# CloudSpinTargetResult

Cloud Spin result for a target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | Specifies the unique id of the cloud spin entity. | [optional] 
**aws_params** | [**AwsCloudSpinParams**](AwsCloudSpinParams.md) |  | [optional] 
**azure_params** | [**AzureCloudSpinParams**](AzureCloudSpinParams.md) |  | [optional] 
**name** | **str, none_type** | Specifies the name of the already added cloud spin target. | [optional] [readonly] 
**start_time_usecs** | **int, none_type** | Specifies the start time of Cloud Spin in Unix epoch Timestamp(in microseconds) for a target. | [optional] 
**end_time_usecs** | **int, none_type** | Specifies the end time of Cloud Spin in Unix epoch Timestamp(in microseconds) for a target. | [optional] 
**status** | **str, none_type** | Status of the Cloud Spin for a target. &#39;Running&#39; indicates that the run is still running. &#39;Canceled&#39; indicates that the run has been canceled. &#39;Canceling&#39; indicates that the run is in the process of being canceled. &#39;Failed&#39; indicates that the run has failed. &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening. &#39;Succeeded&#39; indicates that the run has finished successfully. &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages. | [optional] 
**message** | **str, none_type** | Message about the Cloud Spin run. | [optional] 
**stats** | [**CloudSpinDataStats**](CloudSpinDataStats.md) |  | [optional] 
**is_manually_deleted** | **bool, none_type** | Specifies whether the snapshot is deleted manually. | [optional] 
**expiry_time_usecs** | **int, none_type** | Specifies the expiry time of attempt in Unix epoch Timestamp (in microseconds) for an object. | [optional] 
**cloudspin_task_id** | **str, none_type** | Task ID for a CloudSpin protection run. | [optional] 
**progress_task_id** | **str, none_type** | Progress monitor task id for Cloud Spin run. | [optional] 
**data_lock_constraints** | [**DataLockConstraints**](DataLockConstraints.md) |  | [optional] 
**on_legal_hold** | **bool, none_type** | Specifies the legal hold status for a cloud spin target. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


