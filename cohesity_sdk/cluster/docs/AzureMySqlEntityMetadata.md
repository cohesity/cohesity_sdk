# AzureMySqlEntityMetadata

Specifies the entity metadata of azure mysql entities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_list** | [**List[AzureMySqlMetadata]**](AzureMySqlMetadata.md) | Specifies the metadata list. | 

## Example

```python
from cohesity_sdk.cluster.models.azure_my_sql_entity_metadata import AzureMySqlEntityMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMySqlEntityMetadata from a JSON string
azure_my_sql_entity_metadata_instance = AzureMySqlEntityMetadata.from_json(json)
# print the JSON string representation of the object
print(AzureMySqlEntityMetadata.to_json())

# convert the object into a dict
azure_my_sql_entity_metadata_dict = azure_my_sql_entity_metadata_instance.to_dict()
# create an instance of AzureMySqlEntityMetadata from a dict
azure_my_sql_entity_metadata_from_dict = AzureMySqlEntityMetadata.from_dict(azure_my_sql_entity_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


