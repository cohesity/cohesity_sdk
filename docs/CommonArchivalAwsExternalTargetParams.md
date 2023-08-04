# CommonArchivalAwsExternalTargetParams

Specifies the common parameters which are specific to AWS related External Targets of archival purpose type.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str, none_type** | Specifies bucket name of the External Target. | 
**region** | **str, none_type** | Specifies region of the External Target. | 
**storage_class** | **str, none_type** | Specifies the AWS External Target storage class. | 
**source_side_deduplication** | **bool, none_type** | Specifies the Source Side Deduplication setting for the AWS external target | [optional] 
**is_incremental_archival_enabled** | **bool, none_type** | Specifies if Incremental Archival setting is enabled or not. | [optional] 
**is_forever_incremental_archival_enabled** | **bool, none_type** | Specifies if Forever Incremental Archival setting is enabled or not. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


