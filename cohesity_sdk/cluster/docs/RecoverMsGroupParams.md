# RecoverMsGroupParams

Specifies the parameters to recover Microsoft 365 Group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ms_groups** | [**[MsGroupParam], none_type**](MsGroupParam.md) | Specifies a list of groups getting restored. | 
**continue_on_error** | **bool, none_type** | Specifies whether to continue recovering other MS groups if one of MS groups failed to recover. Default value is false. | [optional] 
**restore_original_owners** | **bool, none_type** | Specifies whether the original members/owners should be part of the newly created target group. If restoreOriginalOwners is null or false, original group owners are not used. | [optional] 
**restore_to_original** | **bool, none_type** | Specifies whether or not all groups are restored to original location. | [optional] 
**target_group** | **str, none_type** | This field is deprecated. Specifies target group nickname in case restoreToOriginal is false. This needs to be specified when restoreToOriginal is false. Use targetMsGroupParam instead of this field. | [optional] 
**target_group_name** | **str, none_type** | This field is deprecated. Specifies target group name in case restoreToOriginal is false. This needs to be specified when restoreToOriginal is false. However, this will be ignored if restoring to alternate existing group (i.e. to a group the nickname of which is same as the one supplied by the end user). Use targetMsGroupParam instead of this field. | [optional] 
**target_group_owner** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 
**target_ms_group_param** | [**TargetMsGroupParam**](TargetMsGroupParam.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


