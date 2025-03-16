# RecoverVmwareVmEsxiSourceConfig

Specifies the new destination Source configuration where the VMs will be recovered for ESXi sources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastores** | [**List[RecoveryObjectIdentifier]**](RecoveryObjectIdentifier.md) | Specifies the datastore objects where the object&#39;s files should be recovered to. | [optional] 
**network_config** | [**RecoverVmwareVmNewSourceNetworkConfig**](RecoverVmwareVmNewSourceNetworkConfig.md) | Specifies the networking configuration to be applied to the recovered VMs. | [optional] 
**resource_pool** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the resource pool object where the recovered objects will be attached. | 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the id of the parent source to recover the VMs. | 
**vm_folder** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Folder where the VMs should be created. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.recover_vmware_vm_esxi_source_config import RecoverVmwareVmEsxiSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverVmwareVmEsxiSourceConfig from a JSON string
recover_vmware_vm_esxi_source_config_instance = RecoverVmwareVmEsxiSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverVmwareVmEsxiSourceConfig.to_json())

# convert the object into a dict
recover_vmware_vm_esxi_source_config_dict = recover_vmware_vm_esxi_source_config_instance.to_dict()
# create an instance of RecoverVmwareVmEsxiSourceConfig from a dict
recover_vmware_vm_esxi_source_config_from_dict = RecoverVmwareVmEsxiSourceConfig.from_dict(recover_vmware_vm_esxi_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


