# TieringAzureExternalTargetParams

Specifies the common parameters which are specific to Azure related External Targets.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_name** | **str, none_type** | Specifies the container name of the external target. | 
**storage_account_name** | **str, none_type** | Specifies the storage account name of the external target. | 
**storage_class** | **str, none_type** | Specifies the Azure External Target class. | defaults to "AzureHotBlob"
**client_id** | **str, none_type** | Specifies the client id of the managed identity assigned to the cluster This is used only for clusters running as Azure VMs where authentication is done using AD. | [optional] 
**region** | **str, none_type** | Specifies region of the External Target. This is only populated for FortKnox vaults. | [optional] 
**storage_access_key** | **str, none_type** | Specifies the storage access key of the external target. | [optional] 
**hot_blob_params** | [**AzureHotBlobParams**](AzureHotBlobParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


