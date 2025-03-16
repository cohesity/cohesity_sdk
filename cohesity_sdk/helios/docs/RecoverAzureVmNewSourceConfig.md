# RecoverAzureVmNewSourceConfig

Specifies the new destination Source configuration where the VMs will be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability_set** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the availability set. | [optional] 
**compute_option** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the type of VM (e.g. small, medium, large) when cloning/restoring the VM in Azure. | [optional] 
**data_transfer_info** | [**DataTransferInfo**](DataTransferInfo.md) |  | [optional] 
**network_config** | [**RecoverAzureVmNewSourceNetworkConfig**](RecoverAzureVmNewSourceNetworkConfig.md) | Specifies the networking configuration to be applied to the recovered VMs. | 
**region** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the region to recover the VMs. Applicable for Tenant based registration on DMaaS. | [optional] 
**resource_group** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the Azure resource group. | 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the id of the parent source to recover the VMs. | 
**storage_account** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the storage account that will contain the storage container | [optional] 
**storage_container** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the storage container within the above storage account. | [optional] 
**storage_resource_group** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies id of the resource group for the selected storage account. | [optional] 
**subscription** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the subscription id to recover the VMs. Applicable for Tenant based registration on DMaaS. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.recover_azure_vm_new_source_config import RecoverAzureVmNewSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAzureVmNewSourceConfig from a JSON string
recover_azure_vm_new_source_config_instance = RecoverAzureVmNewSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverAzureVmNewSourceConfig.to_json())

# convert the object into a dict
recover_azure_vm_new_source_config_dict = recover_azure_vm_new_source_config_instance.to_dict()
# create an instance of RecoverAzureVmNewSourceConfig from a dict
recover_azure_vm_new_source_config_from_dict = RecoverAzureVmNewSourceConfig.from_dict(recover_azure_vm_new_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


