# AwsTargetParamsForRecoverS3

Specifies the parameters for an AWS recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool** | Specifies whether to continue restore on receiving error or not. Default is true. | [optional] 
**new_target_config** | [**AwsRecoverS3NewTargetConfig**](AwsRecoverS3NewTargetConfig.md) | Specifies the configuration for recovering to a new target. | [optional] 
**object_prefix** | **str** | Specifies the prefix to be added to all the objects being recovered. | [optional] 
**overwrite_existing** | **bool** | Specifies whether to override the existing objects. Default is false. | [optional] 
**preserve_attributes** | **bool** | Specifies whether to preserve the objects attributes at the time of restore. Default is true. | [optional] 
**recover_to_original_target** | **bool** | Specifies whether to recover to the original target. If true, originalTargetConfig must be specified. If false, newTargetConfig must be specified. | 

## Example

```python
from cohesity_sdk.helios.models.aws_target_params_for_recover_s3 import AwsTargetParamsForRecoverS3

# TODO update the JSON string below
json = "{}"
# create an instance of AwsTargetParamsForRecoverS3 from a JSON string
aws_target_params_for_recover_s3_instance = AwsTargetParamsForRecoverS3.from_json(json)
# print the JSON string representation of the object
print(AwsTargetParamsForRecoverS3.to_json())

# convert the object into a dict
aws_target_params_for_recover_s3_dict = aws_target_params_for_recover_s3_instance.to_dict()
# create an instance of AwsTargetParamsForRecoverS3 from a dict
aws_target_params_for_recover_s3_from_dict = AwsTargetParamsForRecoverS3.from_dict(aws_target_params_for_recover_s3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


