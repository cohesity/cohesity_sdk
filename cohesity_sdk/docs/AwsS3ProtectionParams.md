# AwsS3ProtectionParams

Specifies the parameters which are specific to AWS Object Protection for AWS S3. Atlease one of tags or objects must be specified.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_object_level_acls** | **bool, none_type** | Specifies whether to backup object level acls. Default value is false. | [optional] 
**objects** | [**[AwsS3ObjectLevelParams]**](AwsS3ObjectLevelParams.md) | Specifies the objects to be protected. | [optional] 
**skip_on_error** | **bool, none_type** | Specifies whether to skip files on error or not. Default value is false. | [optional] 
**storage_class** | **[str]** | Specifies the AWS S3 Storage classes to backup. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


