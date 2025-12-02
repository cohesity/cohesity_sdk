# AzureBlobStorageRestoreFilterPolicy

Specifies the filtering policy for Blob Storage Restore. This contains a list of include prefixes. If specified, only Blobs with a matching prefix will be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_list** | **List[str]** | List of include prefixes that need to be recovered. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.azure_blob_storage_restore_filter_policy import AzureBlobStorageRestoreFilterPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of AzureBlobStorageRestoreFilterPolicy from a JSON string
azure_blob_storage_restore_filter_policy_instance = AzureBlobStorageRestoreFilterPolicy.from_json(json)
# print the JSON string representation of the object
print(AzureBlobStorageRestoreFilterPolicy.to_json())

# convert the object into a dict
azure_blob_storage_restore_filter_policy_dict = azure_blob_storage_restore_filter_policy_instance.to_dict()
# create an instance of AzureBlobStorageRestoreFilterPolicy from a dict
azure_blob_storage_restore_filter_policy_from_dict = AzureBlobStorageRestoreFilterPolicy.from_dict(azure_blob_storage_restore_filter_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


