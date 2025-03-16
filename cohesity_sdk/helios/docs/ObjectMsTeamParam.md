# ObjectMsTeamParam

Specifies recovery parameters associated with a Microsoft 365 Team.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ms_team_param** | [**MsTeamParam**](MsTeamParam.md) | Specifies parameters to recover a Microsoft 365 Team. | 
**recover_object** | [**CommonRecoverObjectSnapshotParams**](CommonRecoverObjectSnapshotParams.md) | Specifies the Microsoft 365 Team recover object info. | 

## Example

```python
from cohesity_sdk.helios.models.object_ms_team_param import ObjectMsTeamParam

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectMsTeamParam from a JSON string
object_ms_team_param_instance = ObjectMsTeamParam.from_json(json)
# print the JSON string representation of the object
print(ObjectMsTeamParam.to_json())

# convert the object into a dict
object_ms_team_param_dict = object_ms_team_param_instance.to_dict()
# create an instance of ObjectMsTeamParam from a dict
object_ms_team_param_from_dict = ObjectMsTeamParam.from_dict(object_ms_team_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


