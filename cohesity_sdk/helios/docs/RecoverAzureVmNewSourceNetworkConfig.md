# RecoverAzureVmNewSourceNetworkConfig

Specifies the network config parameters to be applied for Azure VMs if recovering to new Source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_resource_group** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies id of the resource group for the selected virtual network. | [optional] 
**subnet** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the subnet within the above virtual network. | 
**virtual_network** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the Virtual Network. | 

## Example

```python
from cohesity_sdk.helios.models.recover_azure_vm_new_source_network_config import RecoverAzureVmNewSourceNetworkConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAzureVmNewSourceNetworkConfig from a JSON string
recover_azure_vm_new_source_network_config_instance = RecoverAzureVmNewSourceNetworkConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverAzureVmNewSourceNetworkConfig.to_json())

# convert the object into a dict
recover_azure_vm_new_source_network_config_dict = recover_azure_vm_new_source_network_config_instance.to_dict()
# create an instance of RecoverAzureVmNewSourceNetworkConfig from a dict
recover_azure_vm_new_source_network_config_from_dict = RecoverAzureVmNewSourceNetworkConfig.from_dict(recover_azure_vm_new_source_network_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


