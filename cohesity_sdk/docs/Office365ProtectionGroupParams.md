# Office365ProtectionGroupParams

Specifies the parameters which are specific to Office 365 related Protection Groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[Office365ProtectionGroupObjectParams]**](Office365ProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | 
**protection_types** | **[str]** | Specifies the Office 365 Protection Group types. | 
**exclude_object_ids** | **[int], none_type** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**one_drive_protection_type_params** | [**Office365OneDriveProtectionGroupParams**](Office365OneDriveProtectionGroupParams.md) |  | [optional] 
**outlook_protection_type_params** | [**Office365OutlookProtectionGroupParams**](Office365OutlookProtectionGroupParams.md) |  | [optional] 
**public_folders_protection_type_params** | [**Office365PublicFoldersProtectionGroupParams**](Office365PublicFoldersProtectionGroupParams.md) |  | [optional] 
**share_point_protection_type_params** | [**Office365SharePointProtectionGroupParams**](Office365SharePointProtectionGroupParams.md) |  | [optional] 
**source_id** | **int, none_type** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str, none_type** | Specifies the name of the parent of the objects. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


