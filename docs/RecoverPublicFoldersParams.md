# RecoverPublicFoldersParams

Specifies the parameters to recover Office 365 Public Folders.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**root_public_folders** | [**[RootPublicFolderParam], none_type**](RootPublicFolderParam.md) | Specifies a list of RootPublicFolder params associated with the objects to recover. | 
**target_root_public_folder** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the target RootPublicFolder to recover to. If not specified, the objects will be recovered to original location. | [optional] 
**target_folder_path** | **str, none_type** | Specifies the path to the target folder. | [optional] 
**continue_on_error** | **bool, none_type** | Specifies whether to continue recovering other Public Folders if one of Public Folder failed to recover. Default value is false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


