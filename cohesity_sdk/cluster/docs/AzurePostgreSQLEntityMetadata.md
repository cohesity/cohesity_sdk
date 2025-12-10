# AzurePostgreSQLEntityMetadata

Specifies the entity metadata of azure postgresql entities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_list** | [**List[AzurePostgreSQLMetadata]**](AzurePostgreSQLMetadata.md) | Specifies the metadata list. | 

## Example

```python
from cohesity_sdk.cluster.models.azure_postgre_sql_entity_metadata import AzurePostgreSQLEntityMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AzurePostgreSQLEntityMetadata from a JSON string
azure_postgre_sql_entity_metadata_instance = AzurePostgreSQLEntityMetadata.from_json(json)
# print the JSON string representation of the object
print(AzurePostgreSQLEntityMetadata.to_json())

# convert the object into a dict
azure_postgre_sql_entity_metadata_dict = azure_postgre_sql_entity_metadata_instance.to_dict()
# create an instance of AzurePostgreSQLEntityMetadata from a dict
azure_postgre_sql_entity_metadata_from_dict = AzurePostgreSQLEntityMetadata.from_dict(azure_postgre_sql_entity_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


