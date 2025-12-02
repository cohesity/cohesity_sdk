# AzurePostgreSQLMetadata

Specifies the metadata types and values of azure postgresql.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**AzureCredentials**](AzureCredentials.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.azure_postgre_sql_metadata import AzurePostgreSQLMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AzurePostgreSQLMetadata from a JSON string
azure_postgre_sql_metadata_instance = AzurePostgreSQLMetadata.from_json(json)
# print the JSON string representation of the object
print(AzurePostgreSQLMetadata.to_json())

# convert the object into a dict
azure_postgre_sql_metadata_dict = azure_postgre_sql_metadata_instance.to_dict()
# create an instance of AzurePostgreSQLMetadata from a dict
azure_postgre_sql_metadata_from_dict = AzurePostgreSQLMetadata.from_dict(azure_postgre_sql_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


