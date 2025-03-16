# RecoverMsTeamParams

Specifies the parameters to recover Microsoft 365 Teams.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool** | Specifies whether to continue recovering other teams, if some of the teams fail to recover. Default value is false. | [optional] 
**create_new_team** | **bool** | Specifies to create new team in case the target team doesn&#39;t exists in case restoreToOriginal is false. | [optional] 
**objects** | [**List[ObjectMsTeamParam]**](ObjectMsTeamParam.md) | Specifies a list of Microsoft 365 Teams params associated with objects to recover. | 
**restore_original_owners** | **bool** | Specifies if the original members/owners should be part of the newly created target team or not. | [optional] 
**restore_to_original** | **bool** | Specifies whether or not all Microsoft 365 Teams are restored to original location. | [optional] 
**target_ms_team** | [**TargetMsTeamParam**](TargetMsTeamParam.md) |  | [optional] 
**target_ms_team_param** | [**TargetMsTeamParam**](TargetMsTeamParam.md) |  | [optional] 
**target_team_full_name** | **str** | This field is deprecated. Specifies target team name in case restoreToOriginal is false. This will be ignored if restoring to alternate existing team (i.e. to a team the nickname of which is same as the one supplied by the end user). | [optional] 
**target_team_name** | **str** | Specifies the target team name in case restoreToOriginal is false. | [optional] 
**target_team_nick_name** | **str** | This field is deprecated. Specifies target team nickname in case restoreToOriginal is false. | [optional] 
**target_team_owner** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_ms_team_params import RecoverMsTeamParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverMsTeamParams from a JSON string
recover_ms_team_params_instance = RecoverMsTeamParams.from_json(json)
# print the JSON string representation of the object
print(RecoverMsTeamParams.to_json())

# convert the object into a dict
recover_ms_team_params_dict = recover_ms_team_params_instance.to_dict()
# create an instance of RecoverMsTeamParams from a dict
recover_ms_team_params_from_dict = RecoverMsTeamParams.from_dict(recover_ms_team_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


