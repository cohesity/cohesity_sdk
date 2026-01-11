# RecoverS3CompatibleParams

Specifies the recovery options specific to S3 Compatible environment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recovery_action** | **str** | Specifies the type of recover action to be performed. | defaults to "RecoverS3Buckets"
**objects** | [**[CommonRecoverObjectSnapshotParams], none_type**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of recover Object parameters. | [optional] 
**recover_s3_bucket_params** | [**RecoverS3CompatibleBucketParams**](RecoverS3CompatibleBucketParams.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


