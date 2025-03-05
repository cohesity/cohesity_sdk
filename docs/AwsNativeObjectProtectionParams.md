# AwsNativeObjectProtectionParams

Specifies the parameters which are specific to AWS Object Protection Groups using AWS native snapshot APIs. Atlease one of tags or objects must be specified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[AwsObjectLevelParams]**](AwsObjectLevelParams.md) | Specifies the objects to be protected. | [optional] 
**volume_exclusion_params** | [**EbsVolumeExclusionParams**](EbsVolumeExclusionParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.aws_native_object_protection_params import AwsNativeObjectProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsNativeObjectProtectionParams from a JSON string
aws_native_object_protection_params_instance = AwsNativeObjectProtectionParams.from_json(json)
# print the JSON string representation of the object
print(AwsNativeObjectProtectionParams.to_json())

# convert the object into a dict
aws_native_object_protection_params_dict = aws_native_object_protection_params_instance.to_dict()
# create an instance of AwsNativeObjectProtectionParams from a dict
aws_native_object_protection_params_from_dict = AwsNativeObjectProtectionParams.from_dict(aws_native_object_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


