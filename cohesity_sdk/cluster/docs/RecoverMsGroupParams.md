# RecoverMsGroupParams

Specifies the parameters to recover Microsoft 365 Group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ms_groups** | [**[MsGroupParam], none_type**](MsGroupParam.md) | Specifies a list of groups getting restored. | 
**continue_on_error** | **bool, none_type** | Specifies whether to continue recovering other MS groups if one of MS groups failed to recover. Default value is false. | [optional] 
**restore_to_original** | **bool, none_type** | Specifies whether or not all groups are restored to original location. | [optional] 
**target_group** | **str, none_type** | Specifies target group nickname in case restoreToOriginal is false. This needs to be specifid when restoreToOriginal is false. | [optional] 
**target_group_name** | **str, none_type** | Specifies target group name in case restore_to_original is false. This needs to be specifid when restoreToOriginal is false. However, this will be ignored if restoring to alternate existing group (i.e. to a group the nickname of which is same as the one supplied by the end user). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


