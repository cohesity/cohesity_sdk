# SearchPublicFolderRequestParams

Specifies the request parameters to search for Public Folder items.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bcc_recipient_addresses** | **List[str]** | Filters the public folder items which are sent to specified email addresses in BCC. | [optional] 
**cc_recipient_addresses** | **List[str]** | Filters the public folder items which are sent to specified email addresses in CC. | [optional] 
**has_attachment** | **bool** | Filters the public folder items which have attachment. | [optional] 
**received_end_time_secs** | **int** | Specifies the end time in Unix timestamp epoch in seconds where the received time of the public folder items is less than specified value. | [optional] 
**received_start_time_secs** | **int** | Specifies the start time in Unix timestamp epoch in seconds where the received time of the public folder item is more than specified value. | [optional] 
**recipient_addresses** | **List[str]** | Filters the public folder items which are sent to specified email addresses. | [optional] 
**search_string** | **str** | Specifies the search string to filter the items. User can specify a wildcard character &#39;*&#39; as a suffix to a string where all item names are matched with the prefix string. | [optional] 
**sender_address** | **str** | Filters the public folder items which are received from specified user&#39;s email address. | [optional] 
**types** | **List[str]** | Specifies a list of public folder item types. Only items within the given types will be returned. | [optional] 

## Example

```python
from cohesity_sdk.models.search_public_folder_request_params import SearchPublicFolderRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of SearchPublicFolderRequestParams from a JSON string
search_public_folder_request_params_instance = SearchPublicFolderRequestParams.from_json(json)
# print the JSON string representation of the object
print(SearchPublicFolderRequestParams.to_json())

# convert the object into a dict
search_public_folder_request_params_dict = search_public_folder_request_params_instance.to_dict()
# create an instance of SearchPublicFolderRequestParams from a dict
search_public_folder_request_params_from_dict = SearchPublicFolderRequestParams.from_dict(search_public_folder_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


