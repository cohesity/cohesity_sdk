# RecoverKvmVmNewNetworkConfig

Specifies the network config parameters to be applied for KVM VMs if recovering to a new source with a new network.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_port_group** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 
**vnic_profile** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_kvm_vm_new_network_config import RecoverKvmVmNewNetworkConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverKvmVmNewNetworkConfig from a JSON string
recover_kvm_vm_new_network_config_instance = RecoverKvmVmNewNetworkConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverKvmVmNewNetworkConfig.to_json())

# convert the object into a dict
recover_kvm_vm_new_network_config_dict = recover_kvm_vm_new_network_config_instance.to_dict()
# create an instance of RecoverKvmVmNewNetworkConfig from a dict
recover_kvm_vm_new_network_config_from_dict = RecoverKvmVmNewNetworkConfig.from_dict(recover_kvm_vm_new_network_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


