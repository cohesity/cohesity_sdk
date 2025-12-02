# S3CompatibleTargetParams

Specifies the parameters for an S3 Compatible recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool** | Specifies whether to continue restore on receiving error or not. Default is true. | [optional] 
**new_target_config** | [**S3CompatibleNewTargetConfig**](S3CompatibleNewTargetConfig.md) |  | [optional] 
**object_prefix** | **str** | Specifies the prefix to be added to all the objects being recovered. | [optional] 
**overwrite_existing** | **bool** | Specifies whether to override the existing objects. Default is false. | [optional] 
**preserve_attributes** | **bool** | Specifies whether to preserve the objects attributes at the time of restore. Default is true. | [optional] 
**recover_to_original_target** | **bool** | Specifies whether to recover to the original target. If true, originalTargetConfig must be specified. If false, newTargetConfig must be specified. | 

## Example

```python
from cohesity_sdk.cluster.models.s3_compatible_target_params import S3CompatibleTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of S3CompatibleTargetParams from a JSON string
s3_compatible_target_params_instance = S3CompatibleTargetParams.from_json(json)
# print the JSON string representation of the object
print(S3CompatibleTargetParams.to_json())

# convert the object into a dict
s3_compatible_target_params_dict = s3_compatible_target_params_instance.to_dict()
# create an instance of S3CompatibleTargetParams from a dict
s3_compatible_target_params_from_dict = S3CompatibleTargetParams.from_dict(s3_compatible_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


