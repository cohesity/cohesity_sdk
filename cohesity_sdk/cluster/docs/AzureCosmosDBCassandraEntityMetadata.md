# AzureCosmosDBCassandraEntityMetadata

Specifies the entity metadata of azure cosmosdb cassandra entities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_list** | [**List[AzureCosmosDBCassandraMetadata]**](AzureCosmosDBCassandraMetadata.md) | Specifies the metadata list. | 

## Example

```python
from cohesity_sdk.cluster.models.azure_cosmos_db_cassandra_entity_metadata import AzureCosmosDBCassandraEntityMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AzureCosmosDBCassandraEntityMetadata from a JSON string
azure_cosmos_db_cassandra_entity_metadata_instance = AzureCosmosDBCassandraEntityMetadata.from_json(json)
# print the JSON string representation of the object
print(AzureCosmosDBCassandraEntityMetadata.to_json())

# convert the object into a dict
azure_cosmos_db_cassandra_entity_metadata_dict = azure_cosmos_db_cassandra_entity_metadata_instance.to_dict()
# create an instance of AzureCosmosDBCassandraEntityMetadata from a dict
azure_cosmos_db_cassandra_entity_metadata_from_dict = AzureCosmosDBCassandraEntityMetadata.from_dict(azure_cosmos_db_cassandra_entity_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


