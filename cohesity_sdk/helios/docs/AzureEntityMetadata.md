# AzureEntityMetadata

Specifies the entity metadata of azure entities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_sql_params** | [**AzureSqlEntityMetadata**](AzureSqlEntityMetadata.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.azure_entity_metadata import AzureEntityMetadata

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


