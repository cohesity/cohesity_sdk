# TargetMsGroupParam

Specifies the target MS group to recover to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_new_group** | **bool** | Specifies whether to create a new MS group to restore to or not. | [optional] 
**group_display_name** | **str** | Specifies the display name of the group to be newly created. This should only be specified when createNewGroup is true. | [optional] 
**group_mail_nickname** | **str** | Specifies the mailbox nickname of the group to be newly created. Users must ensure this field is unique in the M365 domain the restore is targeted to. This should only be specified when createNewGroup is true. | [optional] 
**target_ms_group_object** | [**TargetMsGroupObject**](TargetMsGroupObject.md) |  | [optional] 
**target_parent_source_id** | **int** | Specifies the id of the target domain during alternate groups restore. If restore is to be done in the same domain as that of the source group, then this parameter is not required to be set. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.target_ms_group_param import TargetMsGroupParam

# TODO update the JSON string below
json = "{}"
# create an instance of TargetMsGroupParam from a JSON string
target_ms_group_param_instance = TargetMsGroupParam.from_json(json)
# print the JSON string representation of the object
print(TargetMsGroupParam.to_json())

# convert the object into a dict
target_ms_group_param_dict = target_ms_group_param_instance.to_dict()
# create an instance of TargetMsGroupParam from a dict
target_ms_group_param_from_dict = TargetMsGroupParam.from_dict(target_ms_group_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


