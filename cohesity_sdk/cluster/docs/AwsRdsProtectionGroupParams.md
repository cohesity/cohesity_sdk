# AwsRdsProtectionGroupParams

Specifies the parameters which are specific to AWS RDS related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**exclude_rds_tag_ids** | **List[List[int]]** | Array of arrays of RDS Tag Ids that Specify db instaces to Exclude. | [optional] 
**objects** | [**List[AwsRdsProtectionGroupObjectParams]**](AwsRdsProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | [optional] 
**rds_tag_ids** | **List[List[int]]** | Array of arrays of RDS Tag Ids that Specify db instaces to Protect. | [optional] 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.aws_rds_protection_group_params import AwsRdsProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsRdsProtectionGroupParams from a JSON string
aws_rds_protection_group_params_instance = AwsRdsProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(AwsRdsProtectionGroupParams.to_json())

# convert the object into a dict
aws_rds_protection_group_params_dict = aws_rds_protection_group_params_instance.to_dict()
# create an instance of AwsRdsProtectionGroupParams from a dict
aws_rds_protection_group_params_from_dict = AwsRdsProtectionGroupParams.from_dict(aws_rds_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


