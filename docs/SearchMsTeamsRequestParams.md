# SearchMsTeamsRequestParams

Specifies the request params to search for Teams items.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_types** | **List[str]** | Specifies a list of teams files types. Only items within the given types will be returned. | [optional] 
**channel_names** | **List[str]** | Specifies the list of channel names to filter while doing search for files. | [optional] 
**channel_params** | [**O365TeamsChannelsSearchRequestParams**](O365TeamsChannelsSearchRequestParams.md) |  | [optional] 
**creation_end_time_secs** | **int** | Specifies the end time in Unix timestamp epoch in seconds when the item is created. | [optional] 
**creation_start_time_secs** | **int** | Specifies the start time in Unix timestamp epoch in seconds when the item is created. | [optional] 
**o365_params** | [**O365SearchRequestParams**](O365SearchRequestParams.md) |  | [optional] 
**owner_names** | **List[str]** | Specifies the list of owner email ids to filter on owner of the item. | [optional] 
**search_string** | **str** | Specifies the search string to filter the items. User can specify a wildcard character &#39;*&#39; as a suffix to a string where all item names are matched with the prefix string. | [optional] 
**size_bytes_lower_limit** | **int** | Specifies the minimum size of the item in bytes. | [optional] 
**size_bytes_upper_limit** | **int** | Specifies the maximum size of the item in bytes. | [optional] 
**types** | **List[str]** | Specifies a list of Teams item types. Only items within the given types will be returned. | [optional] 

## Example

```python
from cohesity_sdk.models.search_ms_teams_request_params import SearchMsTeamsRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of SearchMsTeamsRequestParams from a JSON string
search_ms_teams_request_params_instance = SearchMsTeamsRequestParams.from_json(json)
# print the JSON string representation of the object
print(SearchMsTeamsRequestParams.to_json())

# convert the object into a dict
search_ms_teams_request_params_dict = search_ms_teams_request_params_instance.to_dict()
# create an instance of SearchMsTeamsRequestParams from a dict
search_ms_teams_request_params_from_dict = SearchMsTeamsRequestParams.from_dict(search_ms_teams_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


