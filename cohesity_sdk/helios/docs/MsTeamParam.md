# MsTeamParam

Specifies the parameters to recover a Microsoft 365 Team.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_params** | [**List[ChannelParam]**](ChannelParam.md) | Specifies the list of Channels to recover. These are applicable iff recoverEntireMsTeam is false. | [optional] 
**recover_entire_ms_team** | **bool** | Specifies whether to recover the whole Microsoft 365 Team. | 

## Example

```python
from cohesity_sdk.helios.models.ms_team_param import MsTeamParam

# TODO update the JSON string below
json = "{}"
# create an instance of MsTeamParam from a JSON string
ms_team_param_instance = MsTeamParam.from_json(json)
# print the JSON string representation of the object
print(MsTeamParam.to_json())

# convert the object into a dict
ms_team_param_dict = ms_team_param_instance.to_dict()
# create an instance of MsTeamParam from a dict
ms_team_param_from_dict = MsTeamParam.from_dict(ms_team_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


