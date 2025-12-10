# AzureSqlDBEntityMetadata

Specifies the entity metadata of azure SQL DB entities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_list** | [**List[AzureSqlDBMetadata]**](AzureSqlDBMetadata.md) | Specifies the metadata list. | 

## Example

```python
from cohesity_sdk.cluster.models.azure_sql_db_entity_metadata import AzureSqlDBEntityMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AzureSqlDBEntityMetadata from a JSON string
azure_sql_db_entity_metadata_instance = AzureSqlDBEntityMetadata.from_json(json)
# print the JSON string representation of the object
print(AzureSqlDBEntityMetadata.to_json())

# convert the object into a dict
azure_sql_db_entity_metadata_dict = azure_sql_db_entity_metadata_instance.to_dict()
# create an instance of AzureSqlDBEntityMetadata from a dict
azure_sql_db_entity_metadata_from_dict = AzureSqlDBEntityMetadata.from_dict(azure_sql_db_entity_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


