# GCPTargetParamsForRecoverGoogleSpanner

Specifies the recovery target params for Google Spanner target config.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing target. | 
**vpc_network** | **str** | VPC network name for Dataflow processing. | 
**vpc_subnet** | **str** | Subnet name within the VPC for Dataflow processing. | 
**max_workers** | **int** | Maximum number of Dataflow workers to use (cost limiter). | defaults to 10
**cloud_storage_bucket_name** | **str, none_type** | The Google Cloud Storage bucket name for Spanner recovery. | [optional] 
**new_source_config** | [**RecoverGoogleSpannerNewSourceConfig**](RecoverGoogleSpannerNewSourceConfig.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


