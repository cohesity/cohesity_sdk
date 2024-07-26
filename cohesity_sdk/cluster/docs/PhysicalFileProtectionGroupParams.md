# PhysicalFileProtectionGroupParams

Specifies the parameters which are specific to Physical related Protection Groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[PhysicalFileProtectionGroupObjectParams]**](PhysicalFileProtectionGroupObjectParams.md) | Specifies the list of objects protected by this Protection Group. | 
**allow_parallel_runs** | **bool, none_type** | Specifies whether or not this job can have parallel runs. | [optional] 
**cobmr_backup** | **bool, none_type** | Specifies whether to take CoBMR backup. | [optional] 
**continue_on_quiesce_failure** | **bool, none_type** | Specifies whether to continue backing up on quiesce failure. | [optional] 
**dedup_exclusion_source_ids** | **[int]** | Specifies ids of sources for which deduplication has to be disabled. | [optional] 
**excluded_vss_writers** | **[str], none_type** | Specifies writer names which should be excluded from physical file based backups. | [optional] 
**global_exclude_fs** | **[str]** | Specifies global exclude filesystems which are applied to all sources in a job. | [optional] 
**global_exclude_paths** | **[str]** | Specifies global exclude filters which are applied to all sources in a job. | [optional] 
**ignorable_errors** | **[str], none_type** | Specifies the Errors to be ignored in error db. | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**perform_brick_based_deduplication** | **bool, none_type** | Specifies whether or not to perform brick based deduplication on this Protection Group. | [optional] 
**perform_source_side_deduplication** | **bool, none_type** | Specifies whether or not to perform source side deduplication on this Protection Group. | [optional] 
**pre_post_script** | [**PrePostScriptParams**](PrePostScriptParams.md) |  | [optional] 
**quiesce** | **bool, none_type** | Specifies Whether to take app-consistent snapshots by quiescing apps and the filesystem before taking a backup. | [optional] 
**task_timeouts** | [**[CancellationTimeoutParams], none_type**](CancellationTimeoutParams.md) | Specifies the timeouts for all the objects inside this Protection Group, for both full and incremental backups. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


