# AwsDynamoDBProtectionParams

Specifies the parameters which are specific to AWS Dynamo DB related Object protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[AwsObjectLevelParams]**](AwsObjectLevelParams.md) | Specifies the objects to be protected. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.aws_dynamo_db_protection_params import AwsDynamoDBProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsDynamoDBProtectionParams from a JSON string
aws_dynamo_db_protection_params_instance = AwsDynamoDBProtectionParams.from_json(json)
# print the JSON string representation of the object
print(AwsDynamoDBProtectionParams.to_json())

# convert the object into a dict
aws_dynamo_db_protection_params_dict = aws_dynamo_db_protection_params_instance.to_dict()
# create an instance of AwsDynamoDBProtectionParams from a dict
aws_dynamo_db_protection_params_from_dict = AwsDynamoDBProtectionParams.from_dict(aws_dynamo_db_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


