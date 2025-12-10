# AzureTargetParamsForRecoverAzureBlobStorage

Specifies the recovery target params for Azure Blob Storage target config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool** | Specifies whether to continue restore on receiving error or not. Default is true. | [optional] 
**new_source_config** | [**RecoverAzureBlobStorageNewSourceConfig**](RecoverAzureBlobStorageNewSourceConfig.md) |  | [optional] 
**object_prefix** | **str** | Specifies the prefix to be added to all the objects being recovered. | [optional] 
**overwrite_existing** | **bool** | Specifies whether to override the existing objects. Default is false. | [optional] 
**preserve_object_attributes** | **bool** | Specifies if we should preserve object attributes at the time of restore. | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing target. | 

## Example

```python
from cohesity_sdk.cluster.models.azure_target_params_for_recover_azure_blob_storage import AzureTargetParamsForRecoverAzureBlobStorage

# TODO update the JSON string below
json = "{}"
# create an instance of AzureTargetParamsForRecoverAzureBlobStorage from a JSON string
azure_target_params_for_recover_azure_blob_storage_instance = AzureTargetParamsForRecoverAzureBlobStorage.from_json(json)
# print the JSON string representation of the object
print(AzureTargetParamsForRecoverAzureBlobStorage.to_json())

# convert the object into a dict
azure_target_params_for_recover_azure_blob_storage_dict = azure_target_params_for_recover_azure_blob_storage_instance.to_dict()
# create an instance of AzureTargetParamsForRecoverAzureBlobStorage from a dict
azure_target_params_for_recover_azure_blob_storage_from_dict = AzureTargetParamsForRecoverAzureBlobStorage.from_dict(azure_target_params_for_recover_azure_blob_storage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


