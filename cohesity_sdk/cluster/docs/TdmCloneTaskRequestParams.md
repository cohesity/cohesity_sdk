# TdmCloneTaskRequestParams

Specifies the request parameters to create a clone task.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str, none_type** | Specifies the environment of the TDM Clone task. | 
**snapshot_id** | **str, none_type** | Specifies the snapshot ID, from which the clone is to be created. | 
**target_host_id** | **int, none_type** | Specifies the ID of the host, where the clone needs to be created. | 
**protection_group_id** | **str, none_type** | Specifies the ID of an existing protection group, which should start protecting this clone. Specifying this implies that the clone is eligible for automated snapshots based on the policy configuration. If this is specified, policyId should also be specified and protectionGroupName should not be specified. | [optional] 
**protection_group_name** | **str, none_type** | Specifies the name of a new protection group, which should be created to protect this clone. Specifying this implies that the clone is eligible for automated snapshots based on the policy configuration. If this is specified, policyId should also be specified and protectionGroupId should not be specified. | [optional] 
**policy_id** | **str, none_type** | Specifies the ID of the policy, which should be used to protect this clone. This is useful for automatic snapshots. This must be specified if either of protectionGroupId and protectionGroupName is specified. | [optional] 
**point_in_time_usecs** | **int, none_type** | Specifies the timestamp (in usecs from epoch) for creating the clone at a point in time in the past. | [optional] 
**oracle_params** | [**OracleCloneTask**](OracleCloneTask.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


