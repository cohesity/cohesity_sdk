# AzureMySqlMetadata

Specifies the metadata types and values of azure mysql.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**AzureCredentials**](AzureCredentials.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.azure_my_sql_metadata import AzureMySqlMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMySqlMetadata from a JSON string
azure_my_sql_metadata_instance = AzureMySqlMetadata.from_json(json)
# print the JSON string representation of the object
print(AzureMySqlMetadata.to_json())

# convert the object into a dict
azure_my_sql_metadata_dict = azure_my_sql_metadata_instance.to_dict()
# create an instance of AzureMySqlMetadata from a dict
azure_my_sql_metadata_from_dict = AzureMySqlMetadata.from_dict(azure_my_sql_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


