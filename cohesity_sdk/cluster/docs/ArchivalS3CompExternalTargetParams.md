# ArchivalS3CompExternalTargetParams

Specifies the parameters which are specific to S3 Compatible related External Targets of archival purpose type.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str, none_type** | Specifies the access key id of the external target. | 
**bucket_name** | **str, none_type** | Specifies the bucket name of the external target. | 
**end_point** | **str, none_type** | Specifies the endpoint of the external target. | 
**is_aws_snowball** | **bool, none_type** | Specifies whether the external target is AWS Snowball. | [optional] 
**region** | **str, none_type** | Specifies the region of the external target. | [optional] 
**secret_access_key** | **str, none_type** | Specifies the secret access key of the external target. | [optional] 
**secure_connection** | **bool, none_type** | Specifies the secure connection(https) is enabled or not. | [optional] 
**signature_version** | **int, none_type** | Specifies the aws signature version of the external target. | [optional] 
**bucket_owner_account_id** | **str, none_type** | Specifies the account Id of the S3 bucket owner. | [optional] 
**is_forever_incremental_archival_enabled** | **bool, none_type** | Specifies if Forever Incremental Archival setting is enabled or not. | [optional] 
**is_incremental_archival_enabled** | **bool, none_type** | Specifies if Incremental Archival setting is enabled or not. | [optional] 
**source_side_deduplication** | **bool, none_type** | Specifies the Source Side Deduplication setting for the S3 Compatible external target | [optional] 
**storage_class** | **str, none_type** | Specifies the S3Compatible External Target storage class. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


