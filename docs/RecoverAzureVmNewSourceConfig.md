# RecoverAzureVmNewSourceConfig

Specifies the new destination Source configuration where the VMs will be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability_set** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 
**compute_option** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 
**data_transfer_info** | [**DataTransferInfo**](DataTransferInfo.md) |  | [optional] 
**network_config** | [**RecoverAzureVmNewSourceNetworkConfig**](RecoverAzureVmNewSourceNetworkConfig.md) |  | 
**region** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 
**resource_group** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**storage_account** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 
**storage_container** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 
**storage_resource_group** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 
**subscription** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.recover_azure_vm_new_source_config import RecoverAzureVmNewSourceConfig

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


