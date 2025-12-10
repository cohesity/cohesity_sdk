# S3CompatibleBucketRestoreFilterPolicy

Specifies the filtering policy for S3 Bucket Restore. This contains a list of include prefixes. If specified, only S3 Objects with a matching prefix will be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_list** | **List[str]** | List of include prefixes that need to be recovered. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.s3_compatible_bucket_restore_filter_policy import S3CompatibleBucketRestoreFilterPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of S3CompatibleBucketRestoreFilterPolicy from a JSON string
s3_compatible_bucket_restore_filter_policy_instance = S3CompatibleBucketRestoreFilterPolicy.from_json(json)
# print the JSON string representation of the object
print(S3CompatibleBucketRestoreFilterPolicy.to_json())

# convert the object into a dict
s3_compatible_bucket_restore_filter_policy_dict = s3_compatible_bucket_restore_filter_policy_instance.to_dict()
# create an instance of S3CompatibleBucketRestoreFilterPolicy from a dict
s3_compatible_bucket_restore_filter_policy_from_dict = S3CompatibleBucketRestoreFilterPolicy.from_dict(s3_compatible_bucket_restore_filter_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


