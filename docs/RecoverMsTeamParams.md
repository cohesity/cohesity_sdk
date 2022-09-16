# RecoverMsTeamParams

Specifies the parameters to recover Microsoft 365 Teams.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[ObjectMsTeamParam], none_type**](ObjectMsTeamParam.md) | Specifies a list of Microsoft 365 Teams params associated with objects to recover. | 
**target_ms_team** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the target Team to recover to. If not specified, the objects will be recovered to original location. | [optional] 
**target_team_nick_name** | **str, none_type** | This field is deprecated. Specifies target team nickname in case restoreToOriginal is false. | [optional] 
**target_team_full_name** | **str, none_type** | This field is deprecated. Specifies target team name in case restoreToOriginal is false. This will be ignored if restoring to alternate existing team (i.e. to a team the nickname of which is same as the one supplied by the end user). | [optional] 
**restore_to_original** | **bool, none_type** | Specifies whether or not all Microsoft 365 Teams are restored to original location. | [optional] 
**create_new_team** | **bool, none_type** | Specifies to create new team in case the target team doesn&#39;t exists in case restoreToOriginal is false. | [optional] 
**target_team_name** | **str, none_type** | Specifies the target team name in case restoreToOriginal is false. | [optional] 
**target_ms_team_param** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the ms team target parameters in case of restoreToOriginal is false. | [optional] 
**target_team_owner** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the additional owner entity info for the selected target team. | [optional] 
**restore_original_owners** | **bool, none_type** | Specifies if the original members/owners should be part of the newly created target team or not. | [optional] 
**continue_on_error** | **bool, none_type** | Specifies whether to continue recovering other teams, if some of the teams fail to recover. Default value is false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


