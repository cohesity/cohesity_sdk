# IbmFlashSystemProtectionGroupParams

Specifies the parameters which are specific to IBM Flash System related Protection Groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[IbmFlashSystemProtectionGroupObjectParams]**](IbmFlashSystemProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | 
**is_safe_guarded_copy_snapshot** | **bool, none_type** | Specifies whether the safeguarded copy snapshots are allowed or not | [optional] 
**pre_post_script** | [**HostBasedBackupScriptParams**](HostBasedBackupScriptParams.md) |  | [optional] 
**source_id** | **int, none_type** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str, none_type** | Specifies the name of the parent of the objects. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


