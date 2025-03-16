# TargetMsTeamParam

Specifies the target Microsoft 365 Team to recover to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_source_id** | **int** | Specifies the id of the domain during alternate domain recovery. | [optional] 
**target_team** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the selected existing target team info. | [optional] 
**target_teams_channel_param** | [**TargetTeamsChannelParam**](TargetTeamsChannelParam.md) | Specifies the ms team target channel parameters in case of granular restore to alternate location. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.target_ms_team_param import TargetMsTeamParam

# TODO update the JSON string below
json = "{}"
# create an instance of TargetMsTeamParam from a JSON string
target_ms_team_param_instance = TargetMsTeamParam.from_json(json)
# print the JSON string representation of the object
print(TargetMsTeamParam.to_json())

# convert the object into a dict
target_ms_team_param_dict = target_ms_team_param_instance.to_dict()
# create an instance of TargetMsTeamParam from a dict
target_ms_team_param_from_dict = TargetMsTeamParam.from_dict(target_ms_team_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


