# S3LifecycleManagement

Specifies the S3 Lifecycle policy of the bucket. If not specified no Lifecycle management is performed for objects in this bucket.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version_id** | **int, none_type** | Specifies a unique monotonically increasing version for the lifecycle configuration. | [optional] 
**rules** | [**[LifecycleRule], none_type**](LifecycleRule.md) | Specifies Lifecycle configuration rules for an Amazon S3 bucket. A maximum of 1000 rules can be specified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


