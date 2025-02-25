# ReplicationTargetResult

Replication result for a target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int, none_type** | Specifies the id of the cluster. | [optional] 
**cluster_incarnation_id** | **int, none_type** | Specifies the incarnation id of the cluster. | [optional] 
**cluster_name** | **str, none_type** | Specifies the name of the cluster. | [optional] [readonly] 
**aws_target_config** | [**AWSTargetConfig**](AWSTargetConfig.md) |  | [optional] 
**azure_target_config** | [**AzureTargetConfig**](AzureTargetConfig.md) |  | [optional] 
**data_lock_constraints** | [**DataLockConstraints**](DataLockConstraints.md) |  | [optional] 
**end_time_usecs** | **int, none_type** | Specifies the end time of replication in Unix epoch Timestamp(in microseconds) for a target. | [optional] 
**entries_changed** | **int, none_type** | Specifies the number of metadata actions completed during the protection run. | [optional] 
**expiry_time_usecs** | **int, none_type** | Specifies the expiry time of attempt in Unix epoch Timestamp (in microseconds) for an object. | [optional] 
**is_in_bound** | **bool, none_type** | Specifies the direction of the replication. If the snapshot is replicated to this cluster, then isInBound is true. If the snapshot is replicated from this cluster to another cluster, then isInBound is false. | [optional] 
**is_manually_deleted** | **bool, none_type** | Specifies whether the snapshot is deleted manually. | [optional] 
**message** | **str, none_type** | Message about the replication run. | [optional] 
**multi_object_replication** | **bool, none_type** | Specifies whether view based replication was used. In this case, the view containing all objects is replicated as a whole instead of replicating on a per object basis. | [optional] 
**on_legal_hold** | **bool, none_type** | Specifies the legal hold status for a replication target. | [optional] 
**percentage_completed** | **int, none_type** | Specifies the progress in percentage. | [optional] 
**queued_time_usecs** | **int, none_type** | Specifies the time when the replication is queued for schedule in Unix epoch Timestamp(in microseconds) for a target. | [optional] 
**replication_task_id** | **str, none_type** | Task UID for a replication protection run. This is for tasks that are replicated from another cluster. | [optional] 
**start_time_usecs** | **int, none_type** | Specifies the start time of replication in Unix epoch Timestamp(in microseconds) for a target. | [optional] 
**stats** | [**ReplicationDataStats**](ReplicationDataStats.md) |  | [optional] 
**status** | **str, none_type** | Status of the replication for a target. &#39;Running&#39; indicates that the run is still running. &#39;Canceled&#39; indicates that the run has been canceled. &#39;Canceling&#39; indicates that the run is in the process of being canceled. &#39;Paused&#39; indicates that the ongoing run has been paused. &#39;Failed&#39; indicates that the run has failed. &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening. &#39;Succeeded&#39; indicates that the run has finished successfully. &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages. &#39;Skipped&#39; indicates that the run was skipped. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


