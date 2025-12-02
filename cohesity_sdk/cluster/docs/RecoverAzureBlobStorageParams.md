# RecoverAzureBlobStorageParams

Specifies the parameters to recover Azure Blob Storage .

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_target_params** | [**AzureTargetParamsForRecoverAzureBlobStorage**](AzureTargetParamsForRecoverAzureBlobStorage.md) |  | [optional] 
**blob_storage_restore_filter_policy** | [**AzureBlobStorageRestoreFilterPolicy**](AzureBlobStorageRestoreFilterPolicy.md) |  | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_azure_blob_storage_params import RecoverAzureBlobStorageParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAzureBlobStorageParams from a JSON string
recover_azure_blob_storage_params_instance = RecoverAzureBlobStorageParams.from_json(json)
# print the JSON string representation of the object
print(RecoverAzureBlobStorageParams.to_json())

# convert the object into a dict
recover_azure_blob_storage_params_dict = recover_azure_blob_storage_params_instance.to_dict()
# create an instance of RecoverAzureBlobStorageParams from a dict
recover_azure_blob_storage_params_from_dict = RecoverAzureBlobStorageParams.from_dict(recover_azure_blob_storage_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


