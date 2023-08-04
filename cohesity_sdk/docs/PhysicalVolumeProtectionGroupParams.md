# PhysicalVolumeProtectionGroupParams

Specifies the parameters which are specific to Volume based physical Protection Groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[PhysicalVolumeProtectionGroupObjectParams]**](PhysicalVolumeProtectionGroupObjectParams.md) |  | 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**perform_source_side_deduplication** | **bool, none_type** | Specifies whether or not to perform source side deduplication on this Protection Group. | [optional] 
**quiesce** | **bool, none_type** | Specifies Whether to take app-consistent snapshots by quiescing apps and the filesystem before taking a backup | [optional] 
**continue_on_quiesce_failure** | **bool, none_type** | Specifies whether to continue backing up on quiesce failure | [optional] 
**incremental_backup_after_restart** | **bool, none_type** | Specifies whether or not to perform an incremental backup after the server restarts. This is applicable to windows environments. | [optional] 
**pre_post_script** | [**PrePostScriptParams**](PrePostScriptParams.md) |  | [optional] 
**dedup_exclusion_source_ids** | **[int]** | Specifies ids of sources for which deduplication has to be disabled. | [optional] 
**excluded_vss_writers** | **[str], none_type** | Specifies writer names which should be excluded from physical volume based backups. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


