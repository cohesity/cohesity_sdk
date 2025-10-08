# Directory

Directory is the struct to represent a file or a folder on a VM.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_stat_info** | [**FileStatInfo**](FileStatInfo.md) |  | [optional] 
**full_path** | **str, none_type** | Path of the file/directory. | [optional] 
**item_id** | **str, none_type** | ItemId is the id of the file/directory. Currently only used in case of OneDrive files/directories. | [optional] 
**name** | **str, none_type** | Name is the name of the file or folder. For /test/file.txt, name will be file.txt. | [optional] 
**type** | **str, none_type** | Specifies the file type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


