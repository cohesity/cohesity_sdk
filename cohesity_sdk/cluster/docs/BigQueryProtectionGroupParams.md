# BigQueryProtectionGroupParams

Specifies the parameters which are specific to GCP BigQuery related Protection Groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_storage_bucket_name** | **str** | The Google Cloud Storage bucket name for BigQuery backup. | 
**bucket_auto_create** | **bool, none_type** | Specifies whether to auto create the Cloud Storage bucket if it doesn&#39;t exist. | [optional] 
**exclude_object_ids** | **[int], none_type** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**objects** | [**[BigQueryProtectionGroupObjectParams]**](BigQueryProtectionGroupObjectParams.md) | Specifies the BigQuery datasets to be included in the Protection Group. | [optional] 
**source_id** | **int, none_type** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str, none_type** | Specifies the name of the parent of the objects. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


