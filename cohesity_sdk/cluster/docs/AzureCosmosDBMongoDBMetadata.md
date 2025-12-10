# AzureCosmosDBMongoDBMetadata

Specifies the metadata types and values of azure cosmosdb mongodb.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**AzureCredentials**](AzureCredentials.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.azure_cosmos_db_mongo_db_metadata import AzureCosmosDBMongoDBMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AzureCosmosDBMongoDBMetadata from a JSON string
azure_cosmos_db_mongo_db_metadata_instance = AzureCosmosDBMongoDBMetadata.from_json(json)
# print the JSON string representation of the object
print(AzureCosmosDBMongoDBMetadata.to_json())

# convert the object into a dict
azure_cosmos_db_mongo_db_metadata_dict = azure_cosmos_db_mongo_db_metadata_instance.to_dict()
# create an instance of AzureCosmosDBMongoDBMetadata from a dict
azure_cosmos_db_mongo_db_metadata_from_dict = AzureCosmosDBMongoDBMetadata.from_dict(azure_cosmos_db_mongo_db_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


