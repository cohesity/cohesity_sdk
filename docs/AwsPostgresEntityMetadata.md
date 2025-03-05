# AwsPostgresEntityMetadata

Specifies the entity metadata of aws postgres entities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_engine_id** | **str** | Specifies the engine id of the database which can be used to identify the type of database. | [optional] 
**metadata_list** | [**List[AwsPostgresMetadata]**](AwsPostgresMetadata.md) | Specifies the metadata list. | 

## Example

```python
from cohesity_sdk.models.aws_postgres_entity_metadata import AwsPostgresEntityMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AwsPostgresEntityMetadata from a JSON string
aws_postgres_entity_metadata_instance = AwsPostgresEntityMetadata.from_json(json)
# print the JSON string representation of the object
print(AwsPostgresEntityMetadata.to_json())

# convert the object into a dict
aws_postgres_entity_metadata_dict = aws_postgres_entity_metadata_instance.to_dict()
# create an instance of AwsPostgresEntityMetadata from a dict
aws_postgres_entity_metadata_from_dict = AwsPostgresEntityMetadata.from_dict(aws_postgres_entity_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


