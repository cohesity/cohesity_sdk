# AzureArchiveBlobParams

Specifies the parameters which are specific to Azure related with tier type Archive Blob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Specifies the category of the external target. | 

## Example

```python
from cohesity_sdk.helios.models.azure_archive_blob_params import AzureArchiveBlobParams

# TODO update the JSON string below
json = "{}"
# create an instance of AzureArchiveBlobParams from a JSON string
azure_archive_blob_params_instance = AzureArchiveBlobParams.from_json(json)
# print the JSON string representation of the object
print(AzureArchiveBlobParams.to_json())

# convert the object into a dict
azure_archive_blob_params_dict = azure_archive_blob_params_instance.to_dict()
# create an instance of AzureArchiveBlobParams from a dict
azure_archive_blob_params_from_dict = AzureArchiveBlobParams.from_dict(azure_archive_blob_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


