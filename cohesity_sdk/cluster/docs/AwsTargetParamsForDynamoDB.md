# AwsTargetParamsForDynamoDB

Specifies the configuration for recovering Dynamo DB objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryption_config** | [**DDBEncryptionConfig**](DDBEncryptionConfig.md) |  | [optional] 
**new_source_config** | [**RecoverAwsDDBNewSourceConfig**](RecoverAwsDDBNewSourceConfig.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new target. If true, source and region information needs to be provided. | 

## Example

```python
from cohesity_sdk.cluster.models.aws_target_params_for_dynamo_db import AwsTargetParamsForDynamoDB

# TODO update the JSON string below
json = "{}"
# create an instance of AwsTargetParamsForDynamoDB from a JSON string
aws_target_params_for_dynamo_db_instance = AwsTargetParamsForDynamoDB.from_json(json)
# print the JSON string representation of the object
print(AwsTargetParamsForDynamoDB.to_json())

# convert the object into a dict
aws_target_params_for_dynamo_db_dict = aws_target_params_for_dynamo_db_instance.to_dict()
# create an instance of AwsTargetParamsForDynamoDB from a dict
aws_target_params_for_dynamo_db_from_dict = AwsTargetParamsForDynamoDB.from_dict(aws_target_params_for_dynamo_db_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


