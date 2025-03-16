# RecoverKvmVmNewSourceNetworkConfig

Specifies the network config parameters to be applied for KVM VMs if recovering to new Source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detach_network** | **bool** | If this is set to true, then the network will be detached from the recovered VMs. All the other networking parameters set will be ignored if set to true. Default value is false. | [optional] 
**new_network_config** | [**RecoverKvmVmNewNetworkConfig**](RecoverKvmVmNewNetworkConfig.md) | Specifies the new network configuration of the Kvm recovery. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.recover_kvm_vm_new_source_network_config import RecoverKvmVmNewSourceNetworkConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverKvmVmNewSourceNetworkConfig from a JSON string
recover_kvm_vm_new_source_network_config_instance = RecoverKvmVmNewSourceNetworkConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverKvmVmNewSourceNetworkConfig.to_json())

# convert the object into a dict
recover_kvm_vm_new_source_network_config_dict = recover_kvm_vm_new_source_network_config_instance.to_dict()
# create an instance of RecoverKvmVmNewSourceNetworkConfig from a dict
recover_kvm_vm_new_source_network_config_from_dict = RecoverKvmVmNewSourceNetworkConfig.from_dict(recover_kvm_vm_new_source_network_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


