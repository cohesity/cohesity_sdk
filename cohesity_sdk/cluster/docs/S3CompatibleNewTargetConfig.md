# S3CompatibleNewTargetConfig

Specifies the configuration for recovering S3 Compatible objects and buckets to a new target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**region** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.s3_compatible_new_target_config import S3CompatibleNewTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of S3CompatibleNewTargetConfig from a JSON string
s3_compatible_new_target_config_instance = S3CompatibleNewTargetConfig.from_json(json)
# print the JSON string representation of the object
print(S3CompatibleNewTargetConfig.to_json())

# convert the object into a dict
s3_compatible_new_target_config_dict = s3_compatible_new_target_config_instance.to_dict()
# create an instance of S3CompatibleNewTargetConfig from a dict
s3_compatible_new_target_config_from_dict = S3CompatibleNewTargetConfig.from_dict(s3_compatible_new_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


