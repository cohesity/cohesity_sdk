# AwsRDSOracleProtectionGroupParams

Specifies the parameters which are specific to AWS RDS Oracle related Protection Groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_auto_create** | **bool, none_type** | Specifies whether to auto create the Cloud Storage bucket if it doesn&#39;t exist. | [optional] 
**cloud_storage_bucket_name** | **str, none_type** | The Cloud Storage bucket name for Oracle database backup. | [optional] 
**exclude_object_ids** | **[int], none_type** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**exclude_rds_tag_ids** | **[[int]], none_type** | Array of arrays of RDS Tag Ids that Specify db instances to Exclude. | [optional] 
**objects** | [**[AwsRDSOracleProtectionGroupObjectParams]**](AwsRDSOracleProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | [optional] 
**parallel_streams** | **int, none_type** | Number of parallel streams for Oracle RMAN backup. Default value is 2. | [optional] 
**rds_tag_ids** | **[[int]], none_type** | Array of arrays of RDS Tag Ids that Specify db instances to Protect. | [optional] 
**section_size** | **int, none_type** | Specifies the size of each backup section in MB. Default value is 1024 MB. | [optional] 
**source_id** | **int, none_type** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str, none_type** | Specifies the name of the parent of the objects. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


