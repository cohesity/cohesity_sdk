# SearchFileRequestParamsBase

Specifies the request parameters to search for files and file folders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_string** | **str** | Specifies the search string to filter the files. User can specify a wildcard character &#39;*&#39; as a suffix to a string where all files name are matched with the prefix string. | [optional] 
**source_environments** | **List[str]** | Specifies a list of the source environments. Only files from these types of source will be returned. | [optional] 
**types** | **List[str]** | Specifies a list of file types. Only files within the given types will be returned. | [optional] 

## Example

```python
from cohesity_sdk.models.search_file_request_params_base import SearchFileRequestParamsBase

# TODO update the JSON string below
json = "{}"
# create an instance of SearchFileRequestParamsBase from a JSON string
search_file_request_params_base_instance = SearchFileRequestParamsBase.from_json(json)
# print the JSON string representation of the object
print(SearchFileRequestParamsBase.to_json())

# convert the object into a dict
search_file_request_params_base_dict = search_file_request_params_base_instance.to_dict()
# create an instance of SearchFileRequestParamsBase from a dict
search_file_request_params_base_from_dict = SearchFileRequestParamsBase.from_dict(search_file_request_params_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


