# AzureEntityMetadata

Specifies the entity metadata of azure entities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_cosmos_db_cassandra_params** | [**AzureCosmosDBCassandraEntityMetadata**](AzureCosmosDBCassandraEntityMetadata.md) |  | [optional] 
**azure_cosmos_db_mongo_db_params** | [**AzureCosmosDBMongoDBEntityMetadata**](AzureCosmosDBMongoDBEntityMetadata.md) |  | [optional] 
**azure_cosmos_dbno_sql_params** | [**AzureCosmosDBNoSQLEntityMetadata**](AzureCosmosDBNoSQLEntityMetadata.md) |  | [optional] 
**azure_kubernetes_params** | [**AzureKubernetesEntityMetadata**](AzureKubernetesEntityMetadata.md) |  | [optional] 
**azure_my_sql_params** | [**AzureMySqlEntityMetadata**](AzureMySqlEntityMetadata.md) |  | [optional] 
**azure_postgre_sql_params** | [**AzurePostgreSQLEntityMetadata**](AzurePostgreSQLEntityMetadata.md) |  | [optional] 
**azure_sql_db_params** | [**AzureSqlDBEntityMetadata**](AzureSqlDBEntityMetadata.md) |  | [optional] 
**azure_sql_mi_params** | [**AzureSqlMIEntityMetadata**](AzureSqlMIEntityMetadata.md) |  | [optional] 
**azure_sql_params** | [**AzureSqlEntityMetadata**](AzureSqlEntityMetadata.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.azure_entity_metadata import AzureEntityMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AzureEntityMetadata from a JSON string
azure_entity_metadata_instance = AzureEntityMetadata.from_json(json)
# print the JSON string representation of the object
print(AzureEntityMetadata.to_json())

# convert the object into a dict
azure_entity_metadata_dict = azure_entity_metadata_instance.to_dict()
# create an instance of AzureEntityMetadata from a dict
azure_entity_metadata_from_dict = AzureEntityMetadata.from_dict(azure_entity_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


