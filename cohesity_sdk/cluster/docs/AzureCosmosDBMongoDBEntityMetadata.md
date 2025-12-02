# AzureCosmosDBMongoDBEntityMetadata

Specifies the entity metadata of azure cosmosdb mongodb entities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_list** | [**List[AzureCosmosDBMongoDBMetadata]**](AzureCosmosDBMongoDBMetadata.md) | Specifies the metadata list. | 

## Example

```python
from cohesity_sdk.cluster.models.azure_cosmos_db_mongo_db_entity_metadata import AzureCosmosDBMongoDBEntityMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AzureCosmosDBMongoDBEntityMetadata from a JSON string
azure_cosmos_db_mongo_db_entity_metadata_instance = AzureCosmosDBMongoDBEntityMetadata.from_json(json)
# print the JSON string representation of the object
print(AzureCosmosDBMongoDBEntityMetadata.to_json())

# convert the object into a dict
azure_cosmos_db_mongo_db_entity_metadata_dict = azure_cosmos_db_mongo_db_entity_metadata_instance.to_dict()
# create an instance of AzureCosmosDBMongoDBEntityMetadata from a dict
azure_cosmos_db_mongo_db_entity_metadata_from_dict = AzureCosmosDBMongoDBEntityMetadata.from_dict(azure_cosmos_db_mongo_db_entity_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


