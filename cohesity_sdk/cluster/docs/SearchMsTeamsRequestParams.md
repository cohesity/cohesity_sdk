# SearchMsTeamsRequestParams

Specifies the request params to search for Teams items.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_string** | **str, none_type** | Specifies the search string to filter the items. User can specify a wildcard character &#39;*&#39; as a suffix to a string where all item names are matched with the prefix string. | [optional] 
**types** | **[str], none_type** | Specifies a list of Teams item types. Only items within the given types will be returned. | [optional] 
**category_types** | **[str], none_type** | Specifies a list of teams files types. Only items within the given types will be returned. | [optional] 
**creation_start_time_secs** | **int, none_type** | Specifies the start time in Unix timestamp epoch in seconds when the item is created. | [optional] 
**creation_end_time_secs** | **int, none_type** | Specifies the end time in Unix timestamp epoch in seconds when the item is created. | [optional] 
**size_bytes_lower_limit** | **int, none_type** | Specifies the minimum size of the item in bytes. | [optional] 
**size_bytes_upper_limit** | **int, none_type** | Specifies the maximum size of the item in bytes. | [optional] 
**owner_names** | **[str], none_type** | Specifies the list of owner email ids to filter on owner of the item. | [optional] 
**channel_names** | **[str], none_type** | Specifies the list of channel names to filter while doing search for files. | [optional] 
**channel_params** | [**O365TeamsChannelsSearchRequestParams**](O365TeamsChannelsSearchRequestParams.md) |  | [optional] 
**o365_params** | [**O365SearchRequestParams**](O365SearchRequestParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


