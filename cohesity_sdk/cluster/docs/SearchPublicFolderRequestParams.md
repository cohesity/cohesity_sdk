# SearchPublicFolderRequestParams

Specifies the request parameters to search for Public Folder items.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bcc_recipient_addresses** | **[str], none_type** | Filters the public folder items which are sent to specified email addresses in BCC. | [optional] 
**cc_recipient_addresses** | **[str], none_type** | Filters the public folder items which are sent to specified email addresses in CC. | [optional] 
**has_attachment** | **bool, none_type** | Filters the public folder items which have attachment. | [optional] 
**received_end_time_secs** | **int, none_type** | Specifies the end time in Unix timestamp epoch in seconds where the received time of the public folder items is less than specified value. | [optional] 
**received_start_time_secs** | **int, none_type** | Specifies the start time in Unix timestamp epoch in seconds where the received time of the public folder item is more than specified value. | [optional] 
**recipient_addresses** | **[str], none_type** | Filters the public folder items which are sent to specified email addresses. | [optional] 
**search_string** | **str, none_type** | Specifies the search string to filter the items. User can specify a wildcard character &#39;*&#39; as a suffix to a string where all item names are matched with the prefix string. | [optional] 
**sender_address** | **str, none_type** | Filters the public folder items which are received from specified user&#39;s email address. | [optional] 
**types** | **[str], none_type** | Specifies a list of public folder item types. Only items within the given types will be returned. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


