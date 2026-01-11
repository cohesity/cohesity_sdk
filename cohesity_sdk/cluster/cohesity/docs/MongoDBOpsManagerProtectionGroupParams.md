# MongoDBOpsManagerProtectionGroupParams

Specifies parameters related to the Mongodb Physical Protection job.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**convert_to_full_on_failure** | **bool, none_type** | Specifies the flag to convert incremental backup to full backup on node failure. | [optional] 
**exclude_object_ids** | **[int], none_type** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**objects** | [**[MongoDBOpsManagerProtectionGroupObjectParams], none_type**](MongoDBOpsManagerProtectionGroupObjectParams.md) | Specifies the list of objects to be protected. | [optional] 
**preferred_backup_nodes** | **str, none_type** | Specifies the comma separated list of hostnames to take backup from; in the order of preference. If provided, these nodes will be preferred as a backup source. The hostnames MUST match the hostnames reported by OpsManager in cluster status result. | [optional] 
**preferred_node** | **str, none_type** | Specifies the preferred node for backup. | [optional] 
**source_id** | **int, none_type** | Object ID of the Source on which this protection was run . | [optional] [readonly] 
**source_name** | **str, none_type** | Specifies the name of the parent of the objects. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


