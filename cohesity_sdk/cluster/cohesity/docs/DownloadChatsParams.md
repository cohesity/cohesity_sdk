# DownloadChatsParams

Specifies the Download chat/posts specific parameters.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_file_type** | **str** | Specifies the file type for the downloaded content. | 
**channel_ids** | **[str], none_type** | Specifies channel IDs whose posts needs to be downloaded. If channelIds is nil or empty then full teams&#39; posts will be downloaded. This is deprecated and clients should now use channelList instead of channelIds. If both are populated, only channelList will be considered for processing. | [optional] 
**channel_list** | [**[Channel], none_type**](Channel.md) | Specifies list of channel&#39;s details, whose chats needs to be downloaded | [optional] 
**html_template** | **str, none_type** | Specifies the html template for the downloaded chats. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


