# AwsEntityChildMetadata

Specifies the entity metadata of child entities of current aws entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aurora_metadata** | [**AwsAuroraEntityMetadata**](AwsAuroraEntityMetadata.md) |  | [optional] 
**document_db_metadata** | [**AwsDocumentDBEntityMetadata**](AwsDocumentDBEntityMetadata.md) |  | [optional] 
**rds_metadata** | [**AwsRdsEntityMetadata**](AwsRdsEntityMetadata.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.aws_entity_child_metadata import AwsEntityChildMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AwsEntityChildMetadata from a JSON string
aws_entity_child_metadata_instance = AwsEntityChildMetadata.from_json(json)
# print the JSON string representation of the object
print(AwsEntityChildMetadata.to_json())

# convert the object into a dict
aws_entity_child_metadata_dict = aws_entity_child_metadata_instance.to_dict()
# create an instance of AwsEntityChildMetadata from a dict
aws_entity_child_metadata_from_dict = AwsEntityChildMetadata.from_dict(aws_entity_child_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


