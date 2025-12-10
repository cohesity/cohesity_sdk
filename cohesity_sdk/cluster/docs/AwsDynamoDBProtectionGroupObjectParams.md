# AwsDynamoDBProtectionGroupObjectParams

Specifies the object parameters to create AWS DyanmoDB Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the object. | 
**name** | **str** | Specifies the name of the table. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.aws_dynamo_db_protection_group_object_params import AwsDynamoDBProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsDynamoDBProtectionGroupObjectParams from a JSON string
aws_dynamo_db_protection_group_object_params_instance = AwsDynamoDBProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(AwsDynamoDBProtectionGroupObjectParams.to_json())

# convert the object into a dict
aws_dynamo_db_protection_group_object_params_dict = aws_dynamo_db_protection_group_object_params_instance.to_dict()
# create an instance of AwsDynamoDBProtectionGroupObjectParams from a dict
aws_dynamo_db_protection_group_object_params_from_dict = AwsDynamoDBProtectionGroupObjectParams.from_dict(aws_dynamo_db_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


