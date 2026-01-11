# RecoverNutanixFSParams

Specifies the recovery options specific to NutanixFS environment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[CommonRecoverObjectSnapshotParams], none_type**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of recover Object parameters. | 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 
**download_file_and_folder_params** | [**CommonDownloadFileAndFolderParams**](CommonDownloadFileAndFolderParams.md) |  | [optional] 
**recover_file_and_folder_params** | [**RecoverNutanixFSFilesParams**](RecoverNutanixFSFilesParams.md) |  | [optional] 
**recover_nas_volume_params** | [**RecoverNutanixFSNasVolumeParams**](RecoverNutanixFSNasVolumeParams.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


