# AwsRecoverS3NewTargetConfig

Specifies the configuration for recovering S3 objects and buckets to a new target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**region** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.aws_recover_s3_new_target_config import AwsRecoverS3NewTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AwsRecoverS3NewTargetConfig from a JSON string
aws_recover_s3_new_target_config_instance = AwsRecoverS3NewTargetConfig.from_json(json)
# print the JSON string representation of the object
print(AwsRecoverS3NewTargetConfig.to_json())

# convert the object into a dict
aws_recover_s3_new_target_config_dict = aws_recover_s3_new_target_config_instance.to_dict()
# create an instance of AwsRecoverS3NewTargetConfig from a dict
aws_recover_s3_new_target_config_from_dict = AwsRecoverS3NewTargetConfig.from_dict(aws_recover_s3_new_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


