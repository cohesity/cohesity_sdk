# CommonArchivalAwsExternalTargetParams

Specifies the common parameters which are specific to AWS related External Targets of archival purpose type.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str, none_type** | Specifies bucket name of the External Target. | 
**region** | **str, none_type** | Specifies region of the External Target. | 
**storage_class** | **str, none_type** | Specifies the AWS External Target storage class. | 
**bucket_owner_account_id** | **str, none_type** | Specifies the account Id of the S3 bucket owner. | [optional] 
**is_forever_incremental_archival_enabled** | **bool, none_type** | Specifies if Forever Incremental Archival setting is enabled or not. | [optional] 
**is_incremental_archival_enabled** | **bool, none_type** | Specifies if Incremental Archival setting is enabled or not. | [optional] 
**lambda_private_endpoint** | **str, none_type** | Lambda private endpoint if the traffic needs to be routed through a private link. | [optional] 
**private_endpoint** | **str, none_type** | Private endpoint if specified. | [optional] 
**source_side_deduplication** | **bool, none_type** | Specifies the Source Side Deduplication setting for the AWS external target | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


