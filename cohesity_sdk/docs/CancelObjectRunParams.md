# CancelObjectRunParams

One object run to cancel.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str, none_type** | Specifies the id of the run to cancel. | 
**archival_target_ids** | **[int], none_type** | Specifies the archival target ids where the tasks run. If specified, the archival target ids must be present within the run specified by the runId above. | [optional] 
**cancel_local_run** | **bool, none_type** | Specifies whether to cancel the local backup run. Default is false. | [optional] 
**cloud_spin_target_ids** | **[int], none_type** | Specifies the cloud spin target ids where the tasks run. If specified, the archival target ids must be present within the run specified by the runId above. | [optional] 
**replication_targets** | [**[ClusterIdentifier], none_type**](ClusterIdentifier.md) | Specifies the cluster identifiers where the tasks run. If specified, the archival target ids must be present within the run specified by the runId above. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


