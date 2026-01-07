# GCPTargetParamsForRecoverGCPBigQuery

Specifies the recovery target params for GCP BigQuery target config.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing target. | 
**bucket_auto_create** | **bool, none_type** | Specifies whether to auto create the Cloud Storage bucket if it does not exist. | [optional] 
**cloud_storage_bucket_name** | **str, none_type** | The Google Cloud Storage bucket name for BigQuery recovery. | [optional] 
**new_source_config** | [**RecoverGCPBigQueryNewSourceConfig**](RecoverGCPBigQueryNewSourceConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


