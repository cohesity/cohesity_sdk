# AzureSqlEntityMetadata

Specifies the entity metadata of azure sql entities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_list** | [**List[AzureSqlMetadata]**](AzureSqlMetadata.md) | Specifies the metadata list. | 

## Example

```python
from cohesity_sdk.models.azure_sql_entity_metadata import AzureSqlEntityMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AzureSqlEntityMetadata from a JSON string
azure_sql_entity_metadata_instance = AzureSqlEntityMetadata.from_json(json)
# print the JSON string representation of the object
print(AzureSqlEntityMetadata.to_json())

# convert the object into a dict
azure_sql_entity_metadata_dict = azure_sql_entity_metadata_instance.to_dict()
# create an instance of AzureSqlEntityMetadata from a dict
azure_sql_entity_metadata_from_dict = AzureSqlEntityMetadata.from_dict(azure_sql_entity_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


