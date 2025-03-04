# SupportChannelConfig

Specifies the support channel configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time_usecs** | **int** | Specifies the support channel expiry time. | 
**is_enabled** | **bool** | Specifies id the support channel is enabled. | 

## Example

```python
from cohesity_sdk.models.support_channel_config import SupportChannelConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SupportChannelConfig from a JSON string
support_channel_config_instance = SupportChannelConfig.from_json(json)
# print the JSON string representation of the object
print(SupportChannelConfig.to_json())

# convert the object into a dict
support_channel_config_dict = support_channel_config_instance.to_dict()
# create an instance of SupportChannelConfig from a dict
support_channel_config_from_dict = SupportChannelConfig.from_dict(support_channel_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


