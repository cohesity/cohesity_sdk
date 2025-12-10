# RecoverMsGroupParams

Specifies the parameters to recover Microsoft 365 Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool** | Specifies whether to continue recovering other MS groups if one of MS groups failed to recover. Default value is false. | [optional] 
**ms_groups** | [**List[MsGroupParam]**](MsGroupParam.md) | Specifies a list of groups getting restored. | 
**restore_original_owners** | **bool** | Specifies whether the original members/owners should be part of the newly created target group. If restoreOriginalOwners is null or false, original group owners are not used. | [optional] 
**restore_to_original** | **bool** | Specifies whether or not all groups are restored to original location. | [optional] 
**target_group** | **str** | This field is deprecated. Specifies target group nickname in case restoreToOriginal is false. This needs to be specified when restoreToOriginal is false. Use targetMsGroupParam instead of this field. | [optional] 
**target_group_name** | **str** | This field is deprecated. Specifies target group name in case restoreToOriginal is false. This needs to be specified when restoreToOriginal is false. However, this will be ignored if restoring to alternate existing group (i.e. to a group the nickname of which is same as the one supplied by the end user). Use targetMsGroupParam instead of this field. | [optional] 
**target_group_owner** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 
**target_ms_group_param** | [**TargetMsGroupParam**](TargetMsGroupParam.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_ms_group_params import RecoverMsGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverMsGroupParams from a JSON string
recover_ms_group_params_instance = RecoverMsGroupParams.from_json(json)
# print the JSON string representation of the object
print(RecoverMsGroupParams.to_json())

# convert the object into a dict
recover_ms_group_params_dict = recover_ms_group_params_instance.to_dict()
# create an instance of RecoverMsGroupParams from a dict
recover_ms_group_params_from_dict = RecoverMsGroupParams.from_dict(recover_ms_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


