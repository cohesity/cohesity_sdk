# TargetTeamsChannelParam

Specifies the target Microsoft 365 Team channel to recover to in case of granular restore

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_owners** | [**List[RecoveryObjectIdentifier]**](RecoveryObjectIdentifier.md) | List of owners for the private channel. At least one owner is needed to create a private channel | [optional] 
**channel_type** | **str** | Specifies whether to create a public or private channel | [optional] 
**create_new_channel** | **bool** | Specifies whether we should create a new channel. If this is true name must not be empty | [optional] 
**id** | **str** | Specifies the id of the target channel. | [optional] 
**name** | **str** | Specifies the name of the target channel. | [optional] 

## Example

```python
from cohesity_sdk.models.target_teams_channel_param import TargetTeamsChannelParam

# TODO update the JSON string below
json = "{}"
# create an instance of TargetTeamsChannelParam from a JSON string
target_teams_channel_param_instance = TargetTeamsChannelParam.from_json(json)
# print the JSON string representation of the object
print(TargetTeamsChannelParam.to_json())

# convert the object into a dict
target_teams_channel_param_dict = target_teams_channel_param_instance.to_dict()
# create an instance of TargetTeamsChannelParam from a dict
target_teams_channel_param_from_dict = TargetTeamsChannelParam.from_dict(target_teams_channel_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


