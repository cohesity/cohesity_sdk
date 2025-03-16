# RecoverVmwareVmOriginalSourceNetworkConfig

Specifies the network config parameters to be applied for VMware VMs if recovering to original Source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detach_network** | **bool** | If this is set to true, then the network will be detached from the recovered VMs. All the other networking parameters set will be ignored if set to true. Default value is false. | [optional] 
**disable_network** | **bool** | Specifies whether the attached network should be left in disabled state. Default is false. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.recover_vmware_vm_original_source_network_config import RecoverVmwareVmOriginalSourceNetworkConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverVmwareVmOriginalSourceNetworkConfig from a JSON string
recover_vmware_vm_original_source_network_config_instance = RecoverVmwareVmOriginalSourceNetworkConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverVmwareVmOriginalSourceNetworkConfig.to_json())

# convert the object into a dict
recover_vmware_vm_original_source_network_config_dict = recover_vmware_vm_original_source_network_config_instance.to_dict()
# create an instance of RecoverVmwareVmOriginalSourceNetworkConfig from a dict
recover_vmware_vm_original_source_network_config_from_dict = RecoverVmwareVmOriginalSourceNetworkConfig.from_dict(recover_vmware_vm_original_source_network_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


