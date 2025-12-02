# RecoverS3CompatibleBucketParams

Specifies the parameters to recover S3 Compatible Buckets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_protection_group_runs_params** | [**List[RecoverProtectionGroupRunParams]**](RecoverProtectionGroupRunParams.md) | Specifies the Protection Group Runs params to recover. | [optional] 
**s3_compatible_bucket_restore_filter_policy** | [**S3CompatibleBucketRestoreFilterPolicy**](S3CompatibleBucketRestoreFilterPolicy.md) |  | [optional] 
**s3_compatible_target_params** | [**S3CompatibleTargetParams**](S3CompatibleTargetParams.md) |  | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_s3_compatible_bucket_params import RecoverS3CompatibleBucketParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverS3CompatibleBucketParams from a JSON string
recover_s3_compatible_bucket_params_instance = RecoverS3CompatibleBucketParams.from_json(json)
# print the JSON string representation of the object
print(RecoverS3CompatibleBucketParams.to_json())

# convert the object into a dict
recover_s3_compatible_bucket_params_dict = recover_s3_compatible_bucket_params_instance.to_dict()
# create an instance of RecoverS3CompatibleBucketParams from a dict
recover_s3_compatible_bucket_params_from_dict = RecoverS3CompatibleBucketParams.from_dict(recover_s3_compatible_bucket_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


