# O365TeamsChannelsSearchRequestParams

Specifies the request parameters related to channels for Microsoft365 teams

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_email** | **str** | Specifies the email id of the channel. | [optional] 
**channel_id** | **str** | Specifies the unique id of the channel. | [optional] 
**channel_name** | **str** | Specifies the name of the channel. Only items within the specified channel will be returned. | [optional] 
**include_private_channels** | **bool** | Specifies whether to include private channels in the response. Default is true. | [optional] [default to True]
**include_public_channels** | **bool** | Specifies whether to include public channels in the response. Default is true. | [optional] [default to True]

## Example

```python
from cohesity_sdk.helios.models.o365_teams_channels_search_request_params import O365TeamsChannelsSearchRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of O365TeamsChannelsSearchRequestParams from a JSON string
o365_teams_channels_search_request_params_instance = O365TeamsChannelsSearchRequestParams.from_json(json)
# print the JSON string representation of the object
print(O365TeamsChannelsSearchRequestParams.to_json())

# convert the object into a dict
o365_teams_channels_search_request_params_dict = o365_teams_channels_search_request_params_instance.to_dict()
# create an instance of O365TeamsChannelsSearchRequestParams from a dict
o365_teams_channels_search_request_params_from_dict = O365TeamsChannelsSearchRequestParams.from_dict(o365_teams_channels_search_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


