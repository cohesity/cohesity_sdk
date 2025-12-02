# RecoverS3CompatibleParams

Specifies the recovery options specific to S3 Compatible environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[CommonRecoverObjectSnapshotParams]**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of recover Object parameters. | [optional] 
**recover_s3_bucket_params** | [**RecoverS3CompatibleBucketParams**](RecoverS3CompatibleBucketParams.md) |  | [optional] 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_s3_compatible_params import RecoverS3CompatibleParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverS3CompatibleParams from a JSON string
recover_s3_compatible_params_instance = RecoverS3CompatibleParams.from_json(json)
# print the JSON string representation of the object
print(RecoverS3CompatibleParams.to_json())

# convert the object into a dict
recover_s3_compatible_params_dict = recover_s3_compatible_params_instance.to_dict()
# create an instance of RecoverS3CompatibleParams from a dict
recover_s3_compatible_params_from_dict = RecoverS3CompatibleParams.from_dict(recover_s3_compatible_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


