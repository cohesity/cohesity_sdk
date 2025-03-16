# DownloadChatsParams

Specifies the Download chat/posts specific parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_ids** | **List[str]** | Specifies channel IDs whose posts needs to be downloaded. If channelIds is nil or empty then full teams&#39; posts will be downloaded. | [optional] 
**download_file_type** | **str** | Specifies the file type for the downloaded content. | 
**html_template** | **str** | Specifies the html template for the downloaded chats. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.download_chats_params import DownloadChatsParams

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadChatsParams from a JSON string
download_chats_params_instance = DownloadChatsParams.from_json(json)
# print the JSON string representation of the object
print(DownloadChatsParams.to_json())

# convert the object into a dict
download_chats_params_dict = download_chats_params_instance.to_dict()
# create an instance of DownloadChatsParams from a dict
download_chats_params_from_dict = DownloadChatsParams.from_dict(download_chats_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


