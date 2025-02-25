# RecoverIsilonParams

Specifies the recovery options specific to Isilon environment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[CommonRecoverObjectSnapshotParams], none_type**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of recover Object parameters. | 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 
**download_file_and_folder_params** | [**CommonDownloadFileAndFolderParams**](CommonDownloadFileAndFolderParams.md) |  | [optional] 
**recover_file_and_folder_params** | [**RecoverIsilonFilesParams**](RecoverIsilonFilesParams.md) |  | [optional] 
**recover_nas_volume_params** | [**RecoverIsilonNasVolumeParams**](RecoverIsilonNasVolumeParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


