# FailoverRunConfiguration

Specifies the configuration required for execting special run as a part of failover workflow. This special run is triggered during palnned failover to sync the source cluster to replication cluster with minimum possible delta. Please note that if this object is passed then this special run will ignore the other archivals and retention settings.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replication_cluster_id** | **int, none_type** | Specifies the replication cluster Id where planned run will replicate objects. | 
**objects** | [**[FailoverObject], none_type**](FailoverObject.md) | Specifies the list of all local entity ids of all the objects being failed from the source cluster. | 
**protection_group_id** | **str, none_type** | Specifies the active protection group id on the source cluster from where the objects are being failed over. | 
**run_type** | **str** | Specifies the type of the backup run to be triggered by this request. If this is not set defaults to incremental backup. | [optional] 
**view_id** | **int, none_type** | If failover is initiated by view based orchastrator, then this field specifies the local view id of source cluster which is being failed over. | [optional] 
**cancel_non_failover_runs** | **bool, none_type** | If set to true, other ongoing runs backing up the same set of entities being failed over will be initiated for cancellation. Non conflicting run operations such as replications to other clusters, archivals will not be cancelled. If set to false, then new run will wait for all the pending operations to finish normally before scheduling a new backup/replication. | [optional] 
**pause_next_runs** | **bool, none_type** | If this is set to true then unless failover operation is completed, all the next runs will be pasued. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


