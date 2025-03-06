# SearchMsGroupsRequestParams

Specifies the request params to search for Groups items.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mailbox_params** | [**SearchEmailRequestParamsBase**](SearchEmailRequestParamsBase.md) |  | [optional] 
**o365_params** | [**O365SearchRequestParams**](O365SearchRequestParams.md) |  | [optional] 
**site_params** | [**SearchDocumentLibraryRequestParams**](SearchDocumentLibraryRequestParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.search_ms_groups_request_params import SearchMsGroupsRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of SearchMsGroupsRequestParams from a JSON string
search_ms_groups_request_params_instance = SearchMsGroupsRequestParams.from_json(json)
# print the JSON string representation of the object
print(SearchMsGroupsRequestParams.to_json())

# convert the object into a dict
search_ms_groups_request_params_dict = search_ms_groups_request_params_instance.to_dict()
# create an instance of SearchMsGroupsRequestParams from a dict
search_ms_groups_request_params_from_dict = SearchMsGroupsRequestParams.from_dict(search_ms_groups_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


