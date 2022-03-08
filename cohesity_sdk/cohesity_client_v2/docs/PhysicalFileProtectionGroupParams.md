# PhysicalFileProtectionGroupParams

Specifies the parameters which are specific to Physical related Protection Groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[PhysicalFileProtectionGroupObjectParams]**](PhysicalFileProtectionGroupObjectParams.md) | Specifies the list of objects protected by this Protection Group. | 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**perform_source_side_deduplication** | **bool, none_type** | Specifies whether or not to perform source side deduplication on this Protection Group. | [optional] 
**quiesce** | **bool, none_type** | Specifies Whether to take app-consistent snapshots by quiescing apps and the filesystem before taking a backup. | [optional] 
**continue_on_quiesce_failure** | **bool, none_type** | Specifies whether to continue backing up on quiesce failure. | [optional] 
**pre_post_script** | [**PrePostScriptParams**](PrePostScriptParams.md) |  | [optional] 
**dedup_exclusion_source_ids** | **[int]** | Specifies ids of sources for which deduplication has to be disabled. | [optional] 
**global_exclude_paths** | **[str]** | Specifies global exclude filters which are applied to all sources in a job. | [optional] 
**global_exclude_fs** | **[str]** | Specifies global exclude filesystems which are applied to all sources in a job. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


