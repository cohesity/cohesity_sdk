# RecoverKvmVmNewSourceConfig

Specifies the new destination Source configuration where the VMs will be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the resource (KVMH host) to which the restored VM will be attached | 
**data_center** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the datacenter where the VM&#39;s files should be restored to. | 
**network_config** | [**RecoverKvmVmNewSourceNetworkConfig**](RecoverKvmVmNewSourceNetworkConfig.md) | Specifies the networking configuration to be applied to the recovered VMs. | [optional] 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the id of the parent source to recover the VMs. | 
**storage_domain** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the Storage Domain where the VM&#39;s disk should be restored to. | 

## Example

```python
from cohesity_sdk.helios.models.recover_kvm_vm_new_source_config import RecoverKvmVmNewSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverKvmVmNewSourceConfig from a JSON string
recover_kvm_vm_new_source_config_instance = RecoverKvmVmNewSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverKvmVmNewSourceConfig.to_json())

# convert the object into a dict
recover_kvm_vm_new_source_config_dict = recover_kvm_vm_new_source_config_instance.to_dict()
# create an instance of RecoverKvmVmNewSourceConfig from a dict
recover_kvm_vm_new_source_config_from_dict = RecoverKvmVmNewSourceConfig.from_dict(recover_kvm_vm_new_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


