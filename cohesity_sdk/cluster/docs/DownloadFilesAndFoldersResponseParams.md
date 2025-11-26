# DownloadFilesAndFoldersResponseParams

Specifies the parameters to create a download files and folders Recovery.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documents** | [**[DocumentObject], none_type**](DocumentObject.md) | Specifies the list of documents to download using item ids. Only one of filesAndFolders or documents should be used. Currently only files are supported by documents. | [optional] 
**files_and_folders** | [**[FilesAndFoldersObject], none_type**](FilesAndFoldersObject.md) | Specifies the list of files and folders to download. Only one of filesAndFolders or documents should be used. | [optional] 
**glacier_retrieval_type** | **str, none_type** | Specifies the glacier retrieval type when restoring or downloding files or folders from a Glacier-based cloud snapshot. | [optional] 
**id** | **str, none_type** | Specifies the id of the Recovery. | [optional] 
**name** | **str, none_type** | Specifies the name of the recovery task. This field must be set and must be a unique name. | [optional] 
**object** | [**CommonRecoverObjectSnapshotParams**](CommonRecoverObjectSnapshotParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


