# SearchDocumentLibraryRequestParams

Specifies the request parameters to search for files/folders in document libraries.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_string** | **str, none_type** | Specifies the search string to filter the files/folders. User can specify a wildcard character &#39;*&#39; as a suffix to a string where all item names are matched with the prefix string. | [optional] 
**include_folders** | **bool, none_type** | Specifies whether to include folders in the response. Default is true. | [optional]  if omitted the server will use the default value of True
**include_files** | **bool, none_type** | Specifies whether to include files in the response. Default is true. | [optional]  if omitted the server will use the default value of True
**category_types** | **[str], none_type** | Specifies a list of document library types. Only items within the given types will be returned. | [optional] 
**creation_start_time_secs** | **int, none_type** | Specifies the start time in Unix timestamp epoch in seconds when the file/folder is created. | [optional] 
**creation_end_time_secs** | **int, none_type** | Specifies the end time in Unix timestamp epoch in seconds when the file/folder is created. | [optional] 
**size_bytes_lower_limit** | **int, none_type** | Specifies the minimum size of the file in bytes. | [optional] 
**size_bytes_upper_limit** | **int, none_type** | Specifies the maximum size of the file in bytes. | [optional] 
**owner_names** | **[str], none_type** | Specifies the list of owner names to filter on owner of the file/folder. | [optional] 
**o365_params** | [**O365SearchRequestParams**](O365SearchRequestParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


