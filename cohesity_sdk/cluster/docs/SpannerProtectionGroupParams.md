# SpannerProtectionGroupParams

Specifies the parameters which are specific to Google Spanner related Protection Groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vpc_network** | **str** | VPC network name for Dataflow processing. | 
**vpc_subnet** | **str** | Subnet name within the VPC for Dataflow processing. | 
**enable_data_boost** | **bool, none_type** | Enables Spanner Data Boost to minimize impact on OLTP workloads. | [optional]  if omitted the server will use the default value of True
**exclude_object_ids** | **[int], none_type** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**export_bucket_name** | **str, none_type** | The Google Cloud Storage bucket name for Spanner export. | [optional] 
**max_workers** | **int, none_type** | Maximum number of Dataflow workers to use (cost limiter). | [optional] 
**objects** | [**[SpannerProtectionGroupObjectParams]**](SpannerProtectionGroupObjectParams.md) | Specifies the Spanner databases to be included in the Protection Group. | [optional] 
**source_id** | **int, none_type** | Specifies the id of the parent of the objects. | [optional] 
**source_name** | **str, none_type** | Specifies the name of the parent of the objects. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


