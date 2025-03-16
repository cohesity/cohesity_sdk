# RecoverAwsS3BucketParams

Specifies the parameters to recover AWS S3 Buckets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_s3_bucket_restore_filter_policy** | [**AwsS3BucketRestoreFilterPolicy**](AwsS3BucketRestoreFilterPolicy.md) |  | [optional] 
**aws_target_params** | [**AwsTargetParamsForRecoverS3**](AwsTargetParamsForRecoverS3.md) |  | [optional] 
**recover_protection_group_runs_params** | [**List[RecoverProtectionGroupRunParams]**](RecoverProtectionGroupRunParams.md) | Specifies the Protection Group Runs params to recover. All the VM&#39;s that are successfully backed up by specified Runs will be recovered. This can be specified along with individual snapshots of VMs. User has to make sure that specified Object snapshots and Protection Group Runs should not have any intersection. For example, user cannot specify multiple Runs which has same Object or an Object snapshot and a Run which has same Object&#39;s snapshot. | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_aws_s3_bucket_params import RecoverAwsS3BucketParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAwsS3BucketParams from a JSON string
recover_aws_s3_bucket_params_instance = RecoverAwsS3BucketParams.from_json(json)
# print the JSON string representation of the object
print(RecoverAwsS3BucketParams.to_json())

# convert the object into a dict
recover_aws_s3_bucket_params_dict = recover_aws_s3_bucket_params_instance.to_dict()
# create an instance of RecoverAwsS3BucketParams from a dict
recover_aws_s3_bucket_params_from_dict = RecoverAwsS3BucketParams.from_dict(recover_aws_s3_bucket_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


