# DynamoDBSpecificParams

Specifies the Dynamo DB specific parameters for source registration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s3_uri** | **str** | Specifies the s3 bucket URI which is used for import and export during backup and recovery. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.dynamo_db_specific_params import DynamoDBSpecificParams

# TODO update the JSON string below
json = "{}"
# create an instance of DynamoDBSpecificParams from a JSON string
dynamo_db_specific_params_instance = DynamoDBSpecificParams.from_json(json)
# print the JSON string representation of the object
print(DynamoDBSpecificParams.to_json())

# convert the object into a dict
dynamo_db_specific_params_dict = dynamo_db_specific_params_instance.to_dict()
# create an instance of DynamoDBSpecificParams from a dict
dynamo_db_specific_params_from_dict = DynamoDBSpecificParams.from_dict(dynamo_db_specific_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


