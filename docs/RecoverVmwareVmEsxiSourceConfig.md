# RecoverVmwareVmEsxiSourceConfig

Specifies the new destination Source configuration where the VMs will be recovered for ESXi sources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastores** | [**List[RecoveryObjectIdentifier]**](RecoveryObjectIdentifier.md) | Specifies the datastore objects where the object&#39;s files should be recovered to. | [optional] 
**network_config** | [**RecoverVmwareVmNewSourceNetworkConfig**](RecoverVmwareVmNewSourceNetworkConfig.md) |  | [optional] 
**resource_pool** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**vm_folder** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_vmware_vm_esxi_source_config import RecoverVmwareVmEsxiSourceConfig

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


