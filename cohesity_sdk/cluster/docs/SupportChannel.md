# SupportChannel

Specifies the support channel info on the cluster config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_extension** | **bool** | Specifies if the support channel extension is allowed. | [optional] 
**end_time_usecs** | **int** | Specifies the support channel expiry time. | [optional] 
**extension_duration_hours** | **int** | Specifies the support channel extension duration in hours. | [optional] 
**is_enabled** | **bool** | Specifies if the support channel is enabled. | [optional] 
**node_ids** | **List[int]** | List of nodes where support channel is enabled. | [optional] 
**support_user_token** | **str** | SSH identity key to login as &#39;support&#39; user. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.support_channel import SupportChannel

# TODO update the JSON string below
json = "{}"
# create an instance of SupportChannel from a JSON string
support_channel_instance = SupportChannel.from_json(json)
# print the JSON string representation of the object
print(SupportChannel.to_json())

# convert the object into a dict
support_channel_dict = support_channel_instance.to_dict()
# create an instance of SupportChannel from a dict
support_channel_from_dict = SupportChannel.from_dict(support_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


