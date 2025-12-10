# AwsEntityMetadata

Specifies the entity metadata of aws entities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aurora_params** | [**AwsAuroraEntityMetadata**](AwsAuroraEntityMetadata.md) |  | [optional] 
**child_metadata** | [**AwsEntityChildMetadata**](AwsEntityChildMetadata.md) |  | [optional] 
**document_db_params** | [**AwsDocumentDBEntityMetadata**](AwsDocumentDBEntityMetadata.md) |  | [optional] 
**postgres_params** | [**AwsPostgresEntityMetadata**](AwsPostgresEntityMetadata.md) |  | [optional] 
**rds_params** | [**AwsRdsEntityMetadata**](AwsRdsEntityMetadata.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.aws_entity_metadata import AwsEntityMetadata

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


