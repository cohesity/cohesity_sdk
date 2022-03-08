# DownloadFilesAndFoldersRequestParams

Specifies the parameters to create a download files and folders Recovery.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the name of the recovery task. This field must be set and must be a unique name. | 
**object** | [**CommonRecoverObjectSnapshotParams**](CommonRecoverObjectSnapshotParams.md) |  | 
**files_and_folders** | [**[FilesAndFoldersObject], none_type**](FilesAndFoldersObject.md) | Specifies the list of files and folders to download. | 
**parent_recovery_id** | **str, none_type** | If current recovery is child task triggered through another parent recovery operation, then this field will specify the id of the parent recovery. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


