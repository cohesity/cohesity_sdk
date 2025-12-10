# AzureCosmosDBNoSQLMetadata

Specifies the metadata types and values of azure cosmosdb nosql.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**AzureCredentials**](AzureCredentials.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.azure_cosmos_dbno_sql_metadata import AzureCosmosDBNoSQLMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AzureCosmosDBNoSQLMetadata from a JSON string
azure_cosmos_dbno_sql_metadata_instance = AzureCosmosDBNoSQLMetadata.from_json(json)
# print the JSON string representation of the object
print(AzureCosmosDBNoSQLMetadata.to_json())

# convert the object into a dict
azure_cosmos_dbno_sql_metadata_dict = azure_cosmos_dbno_sql_metadata_instance.to_dict()
# create an instance of AzureCosmosDBNoSQLMetadata from a dict
azure_cosmos_dbno_sql_metadata_from_dict = AzureCosmosDBNoSQLMetadata.from_dict(azure_cosmos_dbno_sql_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


