# Snapshot

Snapshot identified by various parameters like clusterId, protectionGroupId, objectId etc.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int, none_type** | Cluster Id of cluster to which this snapshot belongs. | 
**incarnation_id** | **int, none_type** | Incarnation id of cluster to which this snapshot belongs. | 
**protection_group_id** | **int, none_type** | Protection Group Id of protection group that created this snapshot. | 
**object_id** | **int, none_type** | The snapshot is of this Object Id. | 
**snapshot_id** | **str, none_type** | Snapshot Id of this snapshot. | [optional] 
**run_id** | **int, none_type** | Run Id of protection group run that created this snapshot. | [optional] 
**run_start_time_usecs** | **int, none_type** | Run start time (in microseconds) of protection group run that created this snapshot. | [optional] 
**tenant_ids** | **[str]** | Tenant Ids associated with this snapshot, if any. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


