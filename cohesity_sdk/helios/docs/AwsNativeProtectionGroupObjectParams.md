# AwsNativeProtectionGroupObjectParams

Specifies the object parameters to create AWS Native Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the object. | 
**name** | **str** | Specifies the name of the virtual machine. | [optional] [readonly] 
**volume_exclusion_params** | [**EbsVolumeExclusionParams**](EbsVolumeExclusionParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.aws_native_protection_group_object_params import AwsNativeProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsNativeProtectionGroupObjectParams from a JSON string
aws_native_protection_group_object_params_instance = AwsNativeProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(AwsNativeProtectionGroupObjectParams.to_json())

# convert the object into a dict
aws_native_protection_group_object_params_dict = aws_native_protection_group_object_params_instance.to_dict()
# create an instance of AwsNativeProtectionGroupObjectParams from a dict
aws_native_protection_group_object_params_from_dict = AwsNativeProtectionGroupObjectParams.from_dict(aws_native_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


