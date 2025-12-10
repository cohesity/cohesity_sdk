# RecoverDynamoDBParams

Specifies the parameters to recover AWS Dynamo DB Tables.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_target_params** | [**AwsTargetParamsForDynamoDB**](AwsTargetParamsForDynamoDB.md) |  | [optional] 
**custom_tags** | [**List[SimpleTags]**](SimpleTags.md) | Specifies the custom tags that need to be present on on every entity that this job creates. Only supported for new location recovery. | [optional] 
**prefix** | **str** | Specifies the prefix to be prepended to the object name after the recovery. | [optional] 
**suffix** | **str** | Specifies the suffix to be appended to the object name after the recovery. | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_dynamo_db_params import RecoverDynamoDBParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverDynamoDBParams from a JSON string
recover_dynamo_db_params_instance = RecoverDynamoDBParams.from_json(json)
# print the JSON string representation of the object
print(RecoverDynamoDBParams.to_json())

# convert the object into a dict
recover_dynamo_db_params_dict = recover_dynamo_db_params_instance.to_dict()
# create an instance of RecoverDynamoDBParams from a dict
recover_dynamo_db_params_from_dict = RecoverDynamoDBParams.from_dict(recover_dynamo_db_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


