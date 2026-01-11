# TargetMsGroupParam

Specifies the target MS group to recover to.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_new_group** | **bool, none_type** | Specifies whether to create a new MS group to restore to or not. | [optional] 
**group_display_name** | **str, none_type** | Specifies the display name of the group to be newly created. This should only be specified when createNewGroup is true. | [optional] 
**group_mail_nickname** | **str, none_type** | Specifies the mailbox nickname of the group to be newly created. Users must ensure this field is unique in the M365 domain the restore is targeted to. This should only be specified when createNewGroup is true. | [optional] 
**target_ms_group_object** | [**TargetMsGroupObject**](TargetMsGroupObject.md) |  | [optional] 
**target_parent_source_id** | **int, none_type** | Specifies the id of the target domain during alternate groups restore. If restore is to be done in the same domain as that of the source group, then this parameter is not required to be set. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


