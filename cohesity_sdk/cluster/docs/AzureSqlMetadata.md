# AzureSqlMetadata

Specifies the metadata types and values of azure sql.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_type** | **str** | Specifies the type of metadata being sent in the request. | 
**standard_credentials** | [**Credentials**](Credentials.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.azure_sql_metadata import AzureSqlMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AzureSqlMetadata from a JSON string
azure_sql_metadata_instance = AzureSqlMetadata.from_json(json)
# print the JSON string representation of the object
print(AzureSqlMetadata.to_json())

# convert the object into a dict
azure_sql_metadata_dict = azure_sql_metadata_instance.to_dict()
# create an instance of AzureSqlMetadata from a dict
azure_sql_metadata_from_dict = AzureSqlMetadata.from_dict(azure_sql_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


