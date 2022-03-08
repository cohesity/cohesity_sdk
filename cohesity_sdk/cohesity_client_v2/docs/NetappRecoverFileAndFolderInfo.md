# NetappRecoverFileAndFolderInfo

Specifies the info about the netapp files and folders to be recovered.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**absolute_path** | **str, none_type** | Specifies the absolute path to the file or folder. | 
**destination_dir** | **str, none_type** | Specifies the destination directory where the file/directory was copied. | [optional] [readonly] 
**is_directory** | **bool, none_type** | Specifies whether this is a directory or not. | [optional] 
**status** | **str, none_type** | Specifies the recovery status for this file or folder. | [optional] [readonly] 
**messages** | **[str], none_type** | Specify error messages about the file during recovery. | [optional] [readonly] 
**inode_id** | **int, none_type** | Specifies the source inode number of the file being recovered. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


