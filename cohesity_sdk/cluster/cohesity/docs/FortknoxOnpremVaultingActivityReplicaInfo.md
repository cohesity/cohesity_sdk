# FortknoxOnpremVaultingActivityReplicaInfo

Specifies replication target run activity information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time_usecs** | **int, none_type** | Specifies the end time of replication in Unix epoch Timestamp(in microseconds) for a target. | [optional] 
**origin_cluster_identifier** | [**ClusterIdentifier**](ClusterIdentifier.md) |  | [optional] 
**origin_protection_group_id** | **str, none_type** | Protection Group Id to which this run belongs on the primary cluster. | [optional] 
**progress_task_id** | **str, none_type** | Progress monitor task id for replication target protection run. | [optional] 
**replication_task_id** | **str, none_type** | Task UID for a replication target protection run. This is for tasks that are replicated from another cluster. | [optional] 
**start_time_usecs** | **int, none_type** | Specifies the start time of replication in Unix epoch Timestamp(in microseconds) for a target. | [optional] 
**status** | **str, none_type** | Status of the replication for a target. &#39;Running&#39; indicates that the run is still running. &#39;Canceled&#39; indicates that the run has been canceled. &#39;Canceling&#39; indicates that the run is in the process of being canceled. &#39;Paused&#39; indicates that the ongoing run has been paused. &#39;Failed&#39; indicates that the run has failed. &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening. &#39;Succeeded&#39; indicates that the run has finished successfully. &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages. &#39;Skipped&#39; indicates that the run was skipped. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


