# RecoverVmwareVmNewNetworkConfig

Specifies the new network config parameters to be applied to VMware VMs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_network** | **bool** | Specifies whether the attached network should be left in disabled state. Default is false | [optional] 
**mappings** | [**List[RecoverVmwareVmNewNetworkConfigMapping]**](RecoverVmwareVmNewNetworkConfigMapping.md) | Specifies the target network mapping for each VM&#39;s network adapter. | [optional] 
**network_port_group** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 
**preserve_mac_address** | **bool** | If this is true and we are attaching to a new network entity, then the VM&#39;s MAC address will be preserved on the new network. Default value is false. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_vmware_vm_new_network_config import RecoverVmwareVmNewNetworkConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverVmwareVmNewNetworkConfig from a JSON string
recover_vmware_vm_new_network_config_instance = RecoverVmwareVmNewNetworkConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverVmwareVmNewNetworkConfig.to_json())

# convert the object into a dict
recover_vmware_vm_new_network_config_dict = recover_vmware_vm_new_network_config_instance.to_dict()
# create an instance of RecoverVmwareVmNewNetworkConfig from a dict
recover_vmware_vm_new_network_config_from_dict = RecoverVmwareVmNewNetworkConfig.from_dict(recover_vmware_vm_new_network_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


