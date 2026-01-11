# NasEnvJobParams

Specifies additional special parameters that are applicable only to Types of 'kGenericNas' type.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_audit_logging** | **bool, none_type** | Specifies whether to audit log the file tiering activity. | [optional]  if omitted the server will use the default value of False
**file_path** | [**FileFilteringPolicy**](FileFilteringPolicy.md) |  | [optional] 
**file_size** | [**FileSizePolicy**](FileSizePolicy.md) |  | [optional] 
**include_all_files** | **bool, none_type** | If set, all files in the view will be uptiered regardless of file_select_policy, num_file_access, hot_file_window, file_size constraints. | [optional]  if omitted the server will use the default value of False
**target** | [**DataTieringTarget**](DataTieringTarget.md) |  | [optional] 
**uptiering_file_age** | [**UptieringFileAgePolicy**](UptieringFileAgePolicy.md) |  | [optional] 
**auto_orphan_data_cleanup** | **bool, none_type** | Specifies whether to remove the orphan data from the target if the symlink is removed from the source. | [optional]  if omitted the server will use the default value of True
**downtiering_file_age** | [**DowntieringFileAgePolicy**](DowntieringFileAgePolicy.md) |  | [optional] 
**skip_back_symlink** | **bool, none_type** | Specifies whether to create a symlink for the migrated data from source to target. | [optional]  if omitted the server will use the default value of True
**backup_existing_snapshot** | **bool, none_type** | Specifies that snapshot label is not set for Data-Protect Netapp Volumes backup. If field is set to true, existing oldest snapshot is used for backup and subsequent incremental will be selected in ascending order of snapshot create time on the source. If snapshot label is set, this field is set to false. | [optional] 
**continue_on_error** | **bool, none_type** | Specifies whether or not the Protection Group should continue regardless of whether or not an error was encountered during protection group run. | [optional] 
**enable_faster_incremental_backups** | **bool, none_type** | Specifies whether this job will enable faster incremental backups using change list or similar APIs | [optional] 
**encryption_enabled** | **bool, none_type** | Specifies whether the protection group should use encryption while backup or not. | [optional] 
**file_lock_config** | [**FileLevelDataLockConfig**](FileLevelDataLockConfig.md) |  | [optional] 
**file_path_filters** | [**FileFilteringPolicy**](FileFilteringPolicy.md) |  | [optional] 
**filter_ip_config** | [**FilterIpConfig**](FilterIpConfig.md) |  | [optional] 
**modify_source_permissions** | **bool, none_type** | Specifies if the NAS source permissions should be modified internally to allow backups. | [optional] 
**nas_protocol** | **str, none_type** | Specifies the preferred protocol to use if this device supports multiple protocols. | [optional] 
**nfs_version_preference** | **str, none_type** | Specifies the preference of NFS version to be backed up if a volume supports multiple versions of NFS. | [optional] 
**snapshot_label** | [**SnapshotLabel**](SnapshotLabel.md) |  | [optional] 
**throttling_config** | [**NasThrottlingConfig**](NasThrottlingConfig.md) |  | [optional] 
**use_changelist** | **bool, none_type** | Specify whether to use the Isilon Changelist API to directly discover changed files/directories for faster incremental backup. Cohesity will keep an extra snapshot which will be deleted by the next successful backup. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


