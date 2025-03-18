# SearchDocumentLibraryRequestParams

Specifies the request parameters to search for files/folders in document libraries.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_types** | **List[str]** | Specifies a list of document library types. Only items within the given types will be returned. | [optional] 
**creation_end_time_secs** | **int** | Specifies the end time in Unix timestamp epoch in seconds when the file/folder is created. | [optional] 
**creation_start_time_secs** | **int** | Specifies the start time in Unix timestamp epoch in seconds when the file/folder is created. | [optional] 
**include_files** | **bool** | Specifies whether to include files in the response. Default is true. | [optional] [default to True]
**include_folders** | **bool** | Specifies whether to include folders in the response. Default is true. | [optional] [default to True]
**o365_params** | [**O365SearchRequestParams**](O365SearchRequestParams.md) |  | [optional] 
**owner_names** | **List[str]** | Specifies the list of owner names to filter on owner of the file/folder. | [optional] 
**search_string** | **str** | Specifies the search string to filter the files/folders. User can specify a wildcard character &#39;*&#39; as a suffix to a string where all item names are matched with the prefix string. | [optional] 
**size_bytes_lower_limit** | **int** | Specifies the minimum size of the file in bytes. | [optional] 
**size_bytes_upper_limit** | **int** | Specifies the maximum size of the file in bytes. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.search_document_library_request_params import SearchDocumentLibraryRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of SearchDocumentLibraryRequestParams from a JSON string
search_document_library_request_params_instance = SearchDocumentLibraryRequestParams.from_json(json)
# print the JSON string representation of the object
print(SearchDocumentLibraryRequestParams.to_json())

# convert the object into a dict
search_document_library_request_params_dict = search_document_library_request_params_instance.to_dict()
# create an instance of SearchDocumentLibraryRequestParams from a dict
search_document_library_request_params_from_dict = SearchDocumentLibraryRequestParams.from_dict(search_document_library_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


