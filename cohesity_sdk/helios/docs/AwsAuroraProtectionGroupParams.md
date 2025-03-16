# AwsAuroraProtectionGroupParams

Specifies the parameters which are specific to AWS Aurora related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aurora_tag_ids** | **List[List[int]]** | Array of arrays of Aurora Tag Ids that specify aurora clusters to protect. | [optional] 
**exclude_aurora_tag_ids** | **List[List[int]]** | Array of arrays of RDS Tag Ids that specify aurora clusters to exclude. | [optional] 
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**objects** | [**List[AwsAuroraProtectionGroupObjectParams]**](AwsAuroraProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | [optional] 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.aws_aurora_protection_group_params import AwsAuroraProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsAuroraProtectionGroupParams from a JSON string
aws_aurora_protection_group_params_instance = AwsAuroraProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(AwsAuroraProtectionGroupParams.to_json())

# convert the object into a dict
aws_aurora_protection_group_params_dict = aws_aurora_protection_group_params_instance.to_dict()
# create an instance of AwsAuroraProtectionGroupParams from a dict
aws_aurora_protection_group_params_from_dict = AwsAuroraProtectionGroupParams.from_dict(aws_aurora_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


