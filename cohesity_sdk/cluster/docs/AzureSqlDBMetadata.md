# AzureSqlDBMetadata

Specifies the metadata types and values of azure SQL DB.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**AzureCredentials**](AzureCredentials.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.azure_sql_db_metadata import AzureSqlDBMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AzureSqlDBMetadata from a JSON string
azure_sql_db_metadata_instance = AzureSqlDBMetadata.from_json(json)
# print the JSON string representation of the object
print(AzureSqlDBMetadata.to_json())

# convert the object into a dict
azure_sql_db_metadata_dict = azure_sql_db_metadata_instance.to_dict()
# create an instance of AzureSqlDBMetadata from a dict
azure_sql_db_metadata_from_dict = AzureSqlDBMetadata.from_dict(azure_sql_db_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


