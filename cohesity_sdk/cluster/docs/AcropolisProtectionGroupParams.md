# AcropolisProtectionGroupParams

Specifies the parameters which are related to Acropolis Protection Groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[AcropolisProtectionGroupObjectParams]**](AcropolisProtectionGroupObjectParams.md) | Specifies the objects included in the Protection Group. | 
**app_consistent_snapshot** | **bool, none_type** | Specifies whether or not to quiesce apps and the file system in order to take app consistent snapshots. If not specified or false then snapshots will not be app consistent. | [optional] 
**continue_on_quiesce_failure** | **bool, none_type** | Specifies whether to continue backing up on quiesce failure | [optional] 
**exclude_object_ids** | **[int], none_type** | Specifies the object ids to be excluded in the Protection Group. | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**source_id** | **int, none_type** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str, none_type** | Specifies the name of the parent of the objects. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


