# ArchivalAwsExternalTargetParams

Specifies the common parameters which are specific to AWS related External Targets.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str, none_type** | Specifies bucket name of the External Target. | 
**region** | **str, none_type** | Specifies region of the External Target. | 
**storage_class** | **str, none_type** | Specifies the AWS External Target storage class. | 
**bucket_owner_account_id** | **str, none_type** | Specifies the account Id of the S3 bucket owner. | [optional] 
**is_forever_incremental_archival_enabled** | **bool, none_type** | Specifies if Forever Incremental Archival setting is enabled or not. | [optional] 
**is_incremental_archival_enabled** | **bool, none_type** | Specifies if Incremental Archival setting is enabled or not. | [optional] 
**source_side_deduplication** | **bool, none_type** | Specifies the Source Side Deduplication setting for the AWS external target | [optional] 
**aws_glacier_params** | [**AwsGlacierParams**](AwsGlacierParams.md) |  | [optional] 
**aws_s3_glacier_deep_archive_params** | [**AwsS3GlacierDeepArchiveParams**](AwsS3GlacierDeepArchiveParams.md) |  | [optional] 
**aws_s3_glacier_ir_params** | [**AwsS3GlacierIRParams**](AwsS3GlacierIRParams.md) |  | [optional] 
**aws_s3_glacier_params** | [**AwsS3GlacierParams**](AwsS3GlacierParams.md) |  | [optional] 
**aws_s3_intelligent_params** | [**AwsS3IntelligentParams**](AwsS3IntelligentParams.md) |  | [optional] 
**aws_s3_one_zone_ia_params** | [**AwsS3OneZoneIAParams**](AwsS3OneZoneIAParams.md) |  | [optional] 
**aws_s3_standard_ia_params** | [**AwsS3StandardIAParams**](AwsS3StandardIAParams.md) |  | [optional] 
**aws_s3_standard_params** | [**AwsS3StandardParams**](AwsS3StandardParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


