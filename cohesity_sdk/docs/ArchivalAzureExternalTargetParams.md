# ArchivalAzureExternalTargetParams

Specifies the common parameters which are specific to Azure related External Targets.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_name** | **str, none_type** | Specifies the container name of the external target. | 
**storage_account_name** | **str, none_type** | Specifies the storage account name of the external target. | 
**storage_class** | **str, none_type** | Specifies the Azure External Target storage class. | 
**client_id** | **str, none_type** | Specifies the client id of the managed identity assigned to the cluster This is used only for clusters running as Azure VMs where authentication is done using AD. | [optional] 
**region** | **str, none_type** | Specifies region of the External Target. This is only populated for FortKnox vaults. | [optional] 
**storage_access_key** | **str, none_type** | Specifies the storage access key of the external target. | [optional] 
**is_forever_incremental_archival_enabled** | **bool, none_type** | Specifies if Forever Incremental Archival setting is enabled or not. | [optional] 
**is_incremental_archival_enabled** | **bool, none_type** | Specifies if Incremental Archival setting is enabled or not. | [optional] 
**is_worm_enabled** | **bool, none_type** | Specifies whether write once read many (WORM) protection is enabled for the Azure container or not. | [optional] 
**source_side_deduplication** | **bool, none_type** | Specifies the Source Side Deduplication setting for the Azure external target | [optional] 
**worm_specific_target_params** | [**WormSpecificTargetParams**](WormSpecificTargetParams.md) |  | [optional] 
**archive_blob_params** | [**AzureArchiveBlobParams**](AzureArchiveBlobParams.md) |  | [optional] 
**cool_blob_params** | [**AzureCoolBlobParams**](AzureCoolBlobParams.md) |  | [optional] 
**hot_blob_params** | [**AzureHotBlobParams**](AzureHotBlobParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


