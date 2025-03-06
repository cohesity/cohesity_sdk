# SearchFileRequestParams

Specifies the request parameters to search for files and file folders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_string** | **str** | Specifies the search string to filter the files. User can specify a wildcard character &#39;*&#39; as a suffix to a string where all files name are matched with the prefix string. | [optional] 
**source_environments** | **List[str]** | Specifies a list of the source environments. Only files from these types of source will be returned. | [optional] 
**types** | **List[str]** | Specifies a list of file types. Only files within the given types will be returned. | [optional] 
**source_ids** | **List[int]** | Specifies a list of source ids. Only files found in these sources will be returned. | [optional] 
**object_ids** | **List[int]** | Specifies a list of object ids. Only files found in these objects will be returned. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.search_file_request_params import SearchFileRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of SearchFileRequestParams from a JSON string
search_file_request_params_instance = SearchFileRequestParams.from_json(json)
# print the JSON string representation of the object
print(SearchFileRequestParams.to_json())

# convert the object into a dict
search_file_request_params_dict = search_file_request_params_instance.to_dict()
# create an instance of SearchFileRequestParams from a dict
search_file_request_params_from_dict = SearchFileRequestParams.from_dict(search_file_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


