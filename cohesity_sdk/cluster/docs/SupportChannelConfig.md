# SupportChannelConfig

Specifies the support channel configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_extension** | **bool** | Specifies if the support channel extension is allowed. | [optional] 
**end_time_usecs** | **int** | Specifies the support channel expiry time. | 
**extension_duration_hours** | **int** | Specifies the support channel extension duration in hours. | [optional] 
**force_enable_reverse_tunnel** | **bool** | Specifies if SSH reverse tunnel should be initiated with RT server. Use this only if there are connectivity issues with Support Channel server. | [optional] 
**is_enabled** | **bool** | Specifies if the support channel should be enabled. | 
**node_ids** | **List[int]** | List of nodes where support channel should be enabled in addition to master node. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.support_channel_config import SupportChannelConfig

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


