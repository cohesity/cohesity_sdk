# ChannelItem

Specifies a M365 Teams channel item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_email** | **str** | Specifies the email of this channel. | [optional] 
**channel_id** | **str** | Specifies the id of this channel. | [optional] 
**channel_name** | **str** | Specifies the channel name. | [optional] 
**channel_type** | **str** | Specifies the channel type. | [optional] 
**creation_time_secs** | **int** | Specifies the Unix timestamp epoch in seconds at which this channel is created. | [optional] 
**owner_names** | **List[str]** | Specifies the names of owners of this channel. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.channel_item import ChannelItem

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelItem from a JSON string
channel_item_instance = ChannelItem.from_json(json)
# print the JSON string representation of the object
print(ChannelItem.to_json())

# convert the object into a dict
channel_item_dict = channel_item_instance.to_dict()
# create an instance of ChannelItem from a dict
channel_item_from_dict = ChannelItem.from_dict(channel_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


