# AwsAuroraProtectionGroupObjectParams

Specifies the object parameters to create an AWS Aurora Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the object. | 
**name** | **str** | Specifies the name of the virtual machine. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.aws_aurora_protection_group_object_params import AwsAuroraProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsAuroraProtectionGroupObjectParams from a JSON string
aws_aurora_protection_group_object_params_instance = AwsAuroraProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(AwsAuroraProtectionGroupObjectParams.to_json())

# convert the object into a dict
aws_aurora_protection_group_object_params_dict = aws_aurora_protection_group_object_params_instance.to_dict()
# create an instance of AwsAuroraProtectionGroupObjectParams from a dict
aws_aurora_protection_group_object_params_from_dict = AwsAuroraProtectionGroupObjectParams.from_dict(aws_aurora_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


