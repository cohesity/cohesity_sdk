# AzureSqlMIMetadata

Specifies the metadata types and values of azure SQL MI.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**AzureCredentials**](AzureCredentials.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.azure_sql_mi_metadata import AzureSqlMIMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AzureSqlMIMetadata from a JSON string
azure_sql_mi_metadata_instance = AzureSqlMIMetadata.from_json(json)
# print the JSON string representation of the object
print(AzureSqlMIMetadata.to_json())

# convert the object into a dict
azure_sql_mi_metadata_dict = azure_sql_mi_metadata_instance.to_dict()
# create an instance of AzureSqlMIMetadata from a dict
azure_sql_mi_metadata_from_dict = AzureSqlMIMetadata.from_dict(azure_sql_mi_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


