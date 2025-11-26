# RecoverAzureVmNewSourceConfig

Specifies the new destination Source configuration where the VMs will be recovered.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the networking configuration to be applied to the recovered VMs. | 
**resource_group** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the Azure resource group. | 
**source** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the id of the parent source to recover the VMs. | 
**availability_set** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the availability set. | [optional] 
**compute_option** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the type of VM (e.g. small, medium, large) when cloning/restoring the VM in Azure. | [optional] 
**data_transfer_info** | [**DataTransferInfo**](DataTransferInfo.md) |  | [optional] 
**region** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the region to recover the VMs. Applicable for Tenant based registration on DMaaS. | [optional] 
**storage_account** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the storage account that will contain the storage container | [optional] 
**storage_container** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the storage container within the above storage account. | [optional] 
**storage_resource_group** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies id of the resource group for the selected storage account. | [optional] 
**subscription** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the subscription id to recover the VMs. Applicable for Tenant based registration on DMaaS. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


