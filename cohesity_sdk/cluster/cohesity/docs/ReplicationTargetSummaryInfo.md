# ReplicationTargetSummaryInfo

Specifies replication target summary information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int, none_type** | Specifies the id of the cluster. | [optional] 
**cluster_incarnation_id** | **int, none_type** | Specifies the incarnation id of the cluster. | [optional] 
**cluster_name** | **str, none_type** | Specifies the name of the cluster. | [optional] [readonly] 
**aws_target_config** | [**AWSTargetConfig**](AWSTargetConfig.md) |  | [optional] 
**azure_target_config** | [**AzureTargetConfig**](AzureTargetConfig.md) |  | [optional] 
**logical_size_bytes** | **int, none_type** | Specifies the logical size of this snapshot in bytes. | [optional] 
**object_ids** | **[str], none_type** | Specifies the list of object ids for which this replication run was performed. | [optional] 
**ownership_context** | **str, none_type** | Specifies the ownership context for the replication. This will only be populated when the replication target is a remote cluster. | [optional] 
**snapshot_id** | **str, none_type** | Specifies the id of the replication snapshot for the object. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


