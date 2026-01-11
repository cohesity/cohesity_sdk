# RecoverPhysicalParams

Specifies the recovery options specific to Physical environment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[CommonRecoverObjectSnapshotParams], none_type**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of Recover Object parameters. For recovering files, specifies the object contains the file to recover. | 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 
**download_file_and_folder_params** | [**CommonDownloadFileAndFolderParams**](CommonDownloadFileAndFolderParams.md) |  | [optional] 
**mount_volume_params** | [**MountPhysicalVolumeParams**](MountPhysicalVolumeParams.md) |  | [optional] 
**recover_file_and_folder_params** | [**RecoverPhysicalFileAndFolderParams**](RecoverPhysicalFileAndFolderParams.md) |  | [optional] 
**recover_snapshot_to_view_params** | [**RecoverPhysicalSnapshotToViewParams**](RecoverPhysicalSnapshotToViewParams.md) |  | [optional] 
**recover_volume_params** | [**RecoverPhysicalVolumeParams**](RecoverPhysicalVolumeParams.md) |  | [optional] 
**system_recovery_params** | [**SystemRecoveryParams**](SystemRecoveryParams.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


