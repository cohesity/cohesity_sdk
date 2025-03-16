# AwsS3BucketRestoreFilterPolicy

Specifies the filtering policy for S3 Bucket Restore. This contains a list of include prefixes. If specified, only S3 Objects with a matching prefix will be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_list** | **List[str]** | List of include prefixes that need to be recovered. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.aws_s3_bucket_restore_filter_policy import AwsS3BucketRestoreFilterPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of AwsS3BucketRestoreFilterPolicy from a JSON string
aws_s3_bucket_restore_filter_policy_instance = AwsS3BucketRestoreFilterPolicy.from_json(json)
# print the JSON string representation of the object
print(AwsS3BucketRestoreFilterPolicy.to_json())

# convert the object into a dict
aws_s3_bucket_restore_filter_policy_dict = aws_s3_bucket_restore_filter_policy_instance.to_dict()
# create an instance of AwsS3BucketRestoreFilterPolicy from a dict
aws_s3_bucket_restore_filter_policy_from_dict = AwsS3BucketRestoreFilterPolicy.from_dict(aws_s3_bucket_restore_filter_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


