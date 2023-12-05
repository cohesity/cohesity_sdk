# O365TeamsChannelsSearchRequestParams

Specifies the request parameters related to channels for Microsoft365 teams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_email** | **str, none_type** | Specifies the email id of the channel. | [optional] 
**channel_id** | **str, none_type** | Specifies the unique id of the channel. | [optional] 
**channel_name** | **str, none_type** | Specifies the name of the channel. Only items within the specified channel will be returned. | [optional] 
**include_private_channels** | **bool, none_type** | Specifies whether to include private channels in the response. Default is true. | [optional]  if omitted the server will use the default value of True
**include_public_channels** | **bool, none_type** | Specifies whether to include public channels in the response. Default is true. | [optional]  if omitted the server will use the default value of True

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


