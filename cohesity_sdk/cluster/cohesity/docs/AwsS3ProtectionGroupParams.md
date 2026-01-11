# AwsS3ProtectionGroupParams

Specifies the parameters which are specific to AWS S3 Protection.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_object_level_acls** | **bool, none_type** | Specifies whether to backup object level acls. Default value is false. | [optional] 
**baseline_incremental_frequency** | **str, none_type** | Specifies the baseline incremental frequency. | [optional] 
**exclude_object_ids** | **[int], none_type** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**inventory_report_destination** | **str, none_type** | ARN of the inventory report destination bucket for S3 backups. | [optional] 
**inventory_report_destination_prefix** | **str, none_type** | The prefix in the S3 destination bucket where inventory reports will be stored. | [optional] 
**inventory_report_frequency** | **str, none_type** | Specifies the frequency to generate inventory reports. | [optional] 
**objects** | [**[AwsS3ProtectionGroupObjectParams]**](AwsS3ProtectionGroupObjectParams.md) | Specifies the objects to be protected. | [optional] 
**skip_on_error** | **bool, none_type** | Specifies whether to skip files on error or not. Default value is false. | [optional] 
**source_id** | **int, none_type** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str, none_type** | Specifies the name of the parent of the objects. | [optional] [readonly] 
**storage_class** | **[str]** | Specifies the AWS S3 Storage classes to backup. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


