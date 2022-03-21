# McmRecoveryTask

Specifies the recovery task.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Specifies the id of the Recovery. | [optional] 
**name** | **str, none_type** | Specifies the name of the Recovery. | [optional] 
**cluster_id** | **int, none_type** | Specifies the cluster id. | [optional] 
**cluster_incarnation_id** | **int, none_type** | Specifies the cluster incarnation id. | [optional] 
**cluster_name** | **str, none_type** | Specifies the cluster name. | [optional] 
**region_id** | **str, none_type** | Specifies the region id where the cluster is located for DMaaS. | [optional] [readonly] 
**rpaas_region_id** | **str, none_type** | Specifies the region id where the snapshots are from to perform the recovery. This is only for RPaaS. | [optional] [readonly] 
**start_time_usecs** | **int, none_type** | Specifies the start time of the Recovery in Unix timestamp epoch in microseconds. | [optional] 
**end_time_usecs** | **int, none_type** | Specifies the end time of the Recovery in Unix timestamp epoch in microseconds. This field will be populated only after Recovery is finished. | [optional] 
**status** | **str, none_type** | Status of the Recovery. &#39;Running&#39; indicates that the Recovery is still running. &#39;Canceled&#39; indicates that the Recovery has been cancelled. &#39;Canceling&#39; indicates that the Recovery is in the process of being cancelled. &#39;Failed&#39; indicates that the Recovery has failed. &#39;Succeeded&#39; indicates that the Recovery has finished successfully. &#39;SucceededWithWarning&#39; indicates that the Recovery finished successfully, but there were some warning messages. | [optional] 
**progress_task_id** | **str, none_type** | Progress monitor task id for Recovery. | [optional] 
**recovery_action** | **str, none_type** | Specifies the recovery action. | [optional] 
**snapshot_environment** | **str, none_type** | Specifies the snapshot environment. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


