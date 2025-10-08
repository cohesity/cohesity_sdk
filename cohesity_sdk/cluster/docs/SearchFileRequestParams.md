# SearchFileRequestParams

Specifies the request parameters to search for files and file folders.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_string** | **str, none_type** | Specifies the search string to filter the files. User can specify a wildcard character &#39;*&#39; as a suffix to a string where all files name are matched with the prefix string. | [optional] 
**source_environments** | **[str], none_type** | Specifies a list of the source environments. Only files from these types of source will be returned. | [optional] 
**types** | **[str], none_type** | Specifies a list of file types. Only files within the given types will be returned. | [optional] 
**source_ids** | **[int], none_type** | Specifies a list of source ids. Only files found in these sources will be returned. | [optional] 
**object_ids** | **[int], none_type** | Specifies a list of object ids. Only files found in these objects will be returned. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


