# AwsDynamoDBProtectionGroupParams

Specifies the parameters which are specific to AWS Dynamo DB related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**objects** | [**List[AwsDynamoDBProtectionGroupObjectParams]**](AwsDynamoDBProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | [optional] 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.aws_dynamo_db_protection_group_params import AwsDynamoDBProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsDynamoDBProtectionGroupParams from a JSON string
aws_dynamo_db_protection_group_params_instance = AwsDynamoDBProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(AwsDynamoDBProtectionGroupParams.to_json())

# convert the object into a dict
aws_dynamo_db_protection_group_params_dict = aws_dynamo_db_protection_group_params_instance.to_dict()
# create an instance of AwsDynamoDBProtectionGroupParams from a dict
aws_dynamo_db_protection_group_params_from_dict = AwsDynamoDBProtectionGroupParams.from_dict(aws_dynamo_db_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


