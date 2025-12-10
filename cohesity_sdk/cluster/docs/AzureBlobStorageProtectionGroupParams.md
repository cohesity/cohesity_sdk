# AzureBlobStorageProtectionGroupParams

Specifies the parameters which are specific to Azure related Protection Groups for Azure Blob Storage workload. Objects must be specified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blob_storage_tag_ids** | **List[List[int]]** | Array of arrays of Blob Storage Tag Ids that specify blob instances to Protect. | [optional] 
**exclude_blob_storage_tag_ids** | **List[List[int]]** | Array of arrays of Blob Storage Tag Ids that specify blob instances to Exclude. | [optional] 
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**objects** | [**List[AzureBlobStorageProtectionGroupObjectParams]**](AzureBlobStorageProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | [optional] 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.azure_blob_storage_protection_group_params import AzureBlobStorageProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of AzureBlobStorageProtectionGroupParams from a JSON string
azure_blob_storage_protection_group_params_instance = AzureBlobStorageProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(AzureBlobStorageProtectionGroupParams.to_json())

# convert the object into a dict
azure_blob_storage_protection_group_params_dict = azure_blob_storage_protection_group_params_instance.to_dict()
# create an instance of AzureBlobStorageProtectionGroupParams from a dict
azure_blob_storage_protection_group_params_from_dict = AzureBlobStorageProtectionGroupParams.from_dict(azure_blob_storage_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


