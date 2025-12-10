# AzureSqlMIEntityMetadata

Specifies the entity metadata of azure SQL MI entities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_list** | [**List[AzureSqlMIMetadata]**](AzureSqlMIMetadata.md) | Specifies the metadata list. | 

## Example

```python
from cohesity_sdk.cluster.models.azure_sql_mi_entity_metadata import AzureSqlMIEntityMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AzureSqlMIEntityMetadata from a JSON string
azure_sql_mi_entity_metadata_instance = AzureSqlMIEntityMetadata.from_json(json)
# print the JSON string representation of the object
print(AzureSqlMIEntityMetadata.to_json())

# convert the object into a dict
azure_sql_mi_entity_metadata_dict = azure_sql_mi_entity_metadata_instance.to_dict()
# create an instance of AzureSqlMIEntityMetadata from a dict
azure_sql_mi_entity_metadata_from_dict = AzureSqlMIEntityMetadata.from_dict(azure_sql_mi_entity_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


