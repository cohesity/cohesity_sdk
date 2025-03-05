# AwsEntityMetadata

Specifies the entity metadata of aws entities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postgres_params** | [**AwsPostgresEntityMetadata**](AwsPostgresEntityMetadata.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.aws_entity_metadata import AwsEntityMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AwsEntityMetadata from a JSON string
aws_entity_metadata_instance = AwsEntityMetadata.from_json(json)
# print the JSON string representation of the object
print(AwsEntityMetadata.to_json())

# convert the object into a dict
aws_entity_metadata_dict = aws_entity_metadata_instance.to_dict()
# create an instance of AwsEntityMetadata from a dict
aws_entity_metadata_from_dict = AwsEntityMetadata.from_dict(aws_entity_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


