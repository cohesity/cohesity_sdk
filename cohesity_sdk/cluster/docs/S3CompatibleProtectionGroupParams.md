# S3CompatibleProtectionGroupParams

Specifies the parameters which are specific to S3 Compatible related Protection Groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[S3CompatibleProtectionGroupObjectParams]**](S3CompatibleProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | 
**backup_object_level_acls** | **bool, none_type** | Specifies whether to backup object level acls. Default value is false. | [optional] 
**source_id** | **int, none_type** | Specifies the parent id of the objects being protected. | [optional] [readonly] 
**source_name** | **str, none_type** | Specifies the parent source name of the objects being protected. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


