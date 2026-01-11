# RecoverS3CompatibleBucketParams

Specifies the parameters to recover S3 Compatible Buckets.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | defaults to "kS3Compatible"
**recover_protection_group_runs_params** | [**[RecoverProtectionGroupRunParams], none_type**](RecoverProtectionGroupRunParams.md) | Specifies the Protection Group Runs params to recover. | [optional] 
**s3_compatible_bucket_restore_filter_policy** | [**S3CompatibleBucketRestoreFilterPolicy**](S3CompatibleBucketRestoreFilterPolicy.md) |  | [optional] 
**s3_compatible_target_params** | [**S3CompatibleTargetParams**](S3CompatibleTargetParams.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


