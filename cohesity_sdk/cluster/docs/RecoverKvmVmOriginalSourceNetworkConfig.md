# RecoverKvmVmOriginalSourceNetworkConfig

Specifies the network config parameters to be applied for KVM VMs if recovering to original Source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detach_network** | **bool** | If this is set to true, then the network will be detached from the recovered VMs. All the other networking parameters set will be ignored if set to true. Default value is false. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_kvm_vm_original_source_network_config import RecoverKvmVmOriginalSourceNetworkConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverKvmVmOriginalSourceNetworkConfig from a JSON string
recover_kvm_vm_original_source_network_config_instance = RecoverKvmVmOriginalSourceNetworkConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverKvmVmOriginalSourceNetworkConfig.to_json())

# convert the object into a dict
recover_kvm_vm_original_source_network_config_dict = recover_kvm_vm_original_source_network_config_instance.to_dict()
# create an instance of RecoverKvmVmOriginalSourceNetworkConfig from a dict
recover_kvm_vm_original_source_network_config_from_dict = RecoverKvmVmOriginalSourceNetworkConfig.from_dict(recover_kvm_vm_original_source_network_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


