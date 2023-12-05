# NetappObjectProtectionRequestParams

Specifies the parameters which are specific to Netapp object protection.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[ProtectionObjectInput]**](ProtectionObjectInput.md) | Specifies the objects to be protected. | 
**continue_on_error** | **bool, none_type** | Specifies whether or not the backup should continue regardless of whether or not an error was encountered. | [optional] 
**encryption_enabled** | **bool, none_type** | Specifies whether the encryption should be used while backup or not. | [optional] 
**file_filters** | [**FileFilteringPolicy**](FileFilteringPolicy.md) |  | [optional] 
**file_lock_config** | [**FileLevelDataLockConfig**](FileLevelDataLockConfig.md) |  | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**pre_post_script** | [**HostBasedBackupScriptParams**](HostBasedBackupScriptParams.md) |  | [optional] 
**throttling_config** | [**NasThrottlingConfig**](NasThrottlingConfig.md) |  | [optional] 
**backup_existing_snapshot** | **bool, none_type** | Specifies that snapshot label is not set for Data-Protect Netapp Volumes backup. If field is set to true, existing oldest snapshot is used for backup and subsequent incremental will be selected in ascending order of snapshot create time on the source. If snapshot label is set, this field is set to false. | [optional] 
**continuous_snapshots** | [**ContinuousSnapshotParams**](ContinuousSnapshotParams.md) |  | [optional] 
**exclude_object_ids** | **[int], none_type** | Specifies the objects to be excluded in the Protection. | [optional] 
**protocol** | **str, none_type** | Specifies the protocol of the NAS device being backed up. | [optional] 
**snapshot_label** | [**SnapshotLabel**](SnapshotLabel.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


