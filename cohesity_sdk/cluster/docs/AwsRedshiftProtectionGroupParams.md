# AwsRedshiftProtectionGroupParams

Specifies the parameters which are specific to AWS Redshift related Protection Groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_auto_create** | **bool, none_type** | Specifies whether to auto create the Cloud Storage bucket if it does not exist. | [optional] 
**cloud_storage_bucket_name** | **str, none_type** | The Cloud Storage bucket name for Redshift backup. | [optional] 
**exclude_object_ids** | **[int], none_type** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**exclude_redshift_tag_ids** | **[[int]], none_type** | Array of arrays of Tag Ids that Specify Redshift databases to Exclude. | [optional] 
**objects** | [**[AwsRedshiftProtectionGroupObjectParams]**](AwsRedshiftProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | [optional] 
**redshift_tag_ids** | **[[int]], none_type** | Array of arrays of Tag Ids that specify Redshift databases to Protect. | [optional] 
**source_id** | **int, none_type** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str, none_type** | Specifies the name of the parent of the objects. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


