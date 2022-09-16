# PureProtectionGroupParams

Specifies the parameters which are specific to Pure related Protection Groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[PureProtectionGroupObjectParams]**](PureProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | 
**max_snapshots_on_primary** | **int, none_type** | Specifies the number of snapshots to retain on the primary environment. If not specified, then snapshots will not be deleted from the primary environment. | [optional] 
**source_id** | **int, none_type** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str, none_type** | Specifies the name of the parent of the objects. | [optional] [readonly] 
**pre_post_script** | [**HostBasedBackupScriptParams**](HostBasedBackupScriptParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


