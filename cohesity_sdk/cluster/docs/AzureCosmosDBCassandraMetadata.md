# AzureCosmosDBCassandraMetadata

Specifies the metadata types and values of azure cosmosdb cassandra.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**AzureCredentials**](AzureCredentials.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.azure_cosmos_db_cassandra_metadata import AzureCosmosDBCassandraMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AzureCosmosDBCassandraMetadata from a JSON string
azure_cosmos_db_cassandra_metadata_instance = AzureCosmosDBCassandraMetadata.from_json(json)
# print the JSON string representation of the object
print(AzureCosmosDBCassandraMetadata.to_json())

# convert the object into a dict
azure_cosmos_db_cassandra_metadata_dict = azure_cosmos_db_cassandra_metadata_instance.to_dict()
# create an instance of AzureCosmosDBCassandraMetadata from a dict
azure_cosmos_db_cassandra_metadata_from_dict = AzureCosmosDBCassandraMetadata.from_dict(azure_cosmos_db_cassandra_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


