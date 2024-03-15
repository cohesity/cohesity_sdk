# AwsS3ProtectionGroupParams

Specifies the parameters which are specific to AWS S3 Protection.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_object_level_acls** | **bool, none_type** | Specifies whether to backup object level acls. Default value is false. | [optional] 
**objects** | [**[AwsS3ProtectionGroupObjectParams]**](AwsS3ProtectionGroupObjectParams.md) | Specifies the objects to be protected. | [optional] 
**skip_on_error** | **bool, none_type** | Specifies whether to skip files on error or not. Default value is false. | [optional] 
**source_id** | **int, none_type** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str, none_type** | Specifies the name of the parent of the objects. | [optional] [readonly] 
**storage_class** | **[str]** | Specifies the AWS S3 Storage classes to backup. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


