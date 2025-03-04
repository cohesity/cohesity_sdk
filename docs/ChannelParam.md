# ChannelParam

Specifies the parameters to recover a Microsoft 365 Teams Channel.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_library_params** | [**List[OneDriveParam]**](OneDriveParam.md) | Specifies the list of doclibs of the Channel to recover. It is populated iff recoverEntireChannel is false. | [optional] 
**id** | **str** | Specifies the Channel id. | 
**name** | **str** | Specifies the Channel name. | [optional] 
**recover_entire_channel** | **bool** | Specifies whether to recover the whole Microsoft 365 Channel. | 
**type** | **str** | Specifies the type of channel public or private | [optional] 

## Example

```python
from cohesity_sdk.models.channel_param import ChannelParam

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelParam from a JSON string
channel_param_instance = ChannelParam.from_json(json)
# print the JSON string representation of the object
print(ChannelParam.to_json())

# convert the object into a dict
channel_param_dict = channel_param_instance.to_dict()
# create an instance of ChannelParam from a dict
channel_param_from_dict = ChannelParam.from_dict(channel_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


