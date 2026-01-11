# RecoverAzureBlobStorageParams

Specifies the parameters to recover Azure Blob Storage .

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | defaults to "kAzure"
**azure_target_params** | [**AzureTargetParamsForRecoverAzureBlobStorage**](AzureTargetParamsForRecoverAzureBlobStorage.md) |  | [optional] 
**blob_storage_restore_filter_policy** | [**AzureBlobStorageRestoreFilterPolicy**](AzureBlobStorageRestoreFilterPolicy.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


