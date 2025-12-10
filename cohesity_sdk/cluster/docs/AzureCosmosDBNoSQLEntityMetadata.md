# AzureCosmosDBNoSQLEntityMetadata

Specifies the entity metadata of azure cosmosdb nosql entities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_list** | [**List[AzureCosmosDBNoSQLMetadata]**](AzureCosmosDBNoSQLMetadata.md) | Specifies the metadata list. | 

## Example

```python
from cohesity_sdk.cluster.models.azure_cosmos_dbno_sql_entity_metadata import AzureCosmosDBNoSQLEntityMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AzureCosmosDBNoSQLEntityMetadata from a JSON string
azure_cosmos_dbno_sql_entity_metadata_instance = AzureCosmosDBNoSQLEntityMetadata.from_json(json)
# print the JSON string representation of the object
print(AzureCosmosDBNoSQLEntityMetadata.to_json())

# convert the object into a dict
azure_cosmos_dbno_sql_entity_metadata_dict = azure_cosmos_dbno_sql_entity_metadata_instance.to_dict()
# create an instance of AzureCosmosDBNoSQLEntityMetadata from a dict
azure_cosmos_dbno_sql_entity_metadata_from_dict = AzureCosmosDBNoSQLEntityMetadata.from_dict(azure_cosmos_dbno_sql_entity_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


