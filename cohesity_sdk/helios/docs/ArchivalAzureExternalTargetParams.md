# ArchivalAzureExternalTargetParams

Specifies the common parameters which are specific to Azure related External Targets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Specifies the client id of the managed identity assigned to the cluster This is used only for clusters running as Azure VMs where authentication is done using AD. | [optional] 
**container_name** | **str** | Specifies the container name of the external target. | 
**region** | **str** | Specifies region of the External Target. This is only populated for FortKnox vaults. | [optional] 
**storage_access_key** | **str** | Specifies the storage access key of the external target. | [optional] 
**storage_account_name** | **str** | Specifies the storage account name of the external target. | 
**is_forever_incremental_archival_enabled** | **bool** | Specifies if Forever Incremental Archival setting is enabled or not. | [optional] 
**is_incremental_archival_enabled** | **bool** | Specifies if Incremental Archival setting is enabled or not. | [optional] 
**is_worm_enabled** | **bool** | Specifies whether write once read many (WORM) protection is enabled for the Azure container or not. | [optional] 
**source_side_deduplication** | **bool** | Specifies the Source Side Deduplication setting for the Azure external target | [optional] 
**storage_class** | **str** | Specifies the Azure External Target storage class. | 
**worm_specific_target_params** | [**WormSpecificTargetParams**](WormSpecificTargetParams.md) |  | [optional] 
**archive_blob_params** | [**AzureArchiveBlobParams**](AzureArchiveBlobParams.md) |  | [optional] 
**cool_blob_params** | [**AzureCoolBlobParams**](AzureCoolBlobParams.md) |  | [optional] 
**hot_blob_params** | [**AzureHotBlobParams**](AzureHotBlobParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.archival_azure_external_target_params import ArchivalAzureExternalTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of ArchivalAzureExternalTargetParams from a JSON string
archival_azure_external_target_params_instance = ArchivalAzureExternalTargetParams.from_json(json)
# print the JSON string representation of the object
print(ArchivalAzureExternalTargetParams.to_json())

# convert the object into a dict
archival_azure_external_target_params_dict = archival_azure_external_target_params_instance.to_dict()
# create an instance of ArchivalAzureExternalTargetParams from a dict
archival_azure_external_target_params_from_dict = ArchivalAzureExternalTargetParams.from_dict(archival_azure_external_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


