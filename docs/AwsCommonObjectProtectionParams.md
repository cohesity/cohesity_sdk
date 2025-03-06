# AwsCommonObjectProtectionParams

Specifies the parameters which are specific to AWS related Object Protection and common to different AWS protection types.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protection_type** | **str** | Specifies the AWS Protection Job type. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.aws_common_object_protection_params import AwsCommonObjectProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsCommonObjectProtectionParams from a JSON string
aws_common_object_protection_params_instance = AwsCommonObjectProtectionParams.from_json(json)
# print the JSON string representation of the object
print(AwsCommonObjectProtectionParams.to_json())

# convert the object into a dict
aws_common_object_protection_params_dict = aws_common_object_protection_params_instance.to_dict()
# create an instance of AwsCommonObjectProtectionParams from a dict
aws_common_object_protection_params_from_dict = AwsCommonObjectProtectionParams.from_dict(aws_common_object_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


