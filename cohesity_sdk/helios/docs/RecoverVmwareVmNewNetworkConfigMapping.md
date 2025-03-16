# RecoverVmwareVmNewNetworkConfigMapping

Specifies source VMs NIC to target network mapping for the VMware VMs being recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_network** | **bool** | Specifies whether the attached network should be left in disabled state for this mapping. Default is false. | [optional] 
**network_adapter_name** | **str** | Name of the VM&#39;s network adapter name. | [optional] 
**org_vdc_network** | [**OrgVDCNetwork**](OrgVDCNetwork.md) |  | [optional] 
**preserve_mac_address** | **bool** | Specifies whether to preserve the MAC address of the source network entity while attaching to the new target network. Default is false. | [optional] 
**source_network_entity** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the source VM&#39;s network port group (i.e, either a standard switch port group or a distributed port group or an opaque network) which is associated with specified network adapter name for which mapping is selected. | [optional] 
**target_network_entity** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the network port group (i.e, either a standard switch port group or a distributed port group or an opaque network) that will attached as backing device on the recovered object for the given network adapter name and source network entity. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.recover_vmware_vm_new_network_config_mapping import RecoverVmwareVmNewNetworkConfigMapping

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverVmwareVmNewNetworkConfigMapping from a JSON string
recover_vmware_vm_new_network_config_mapping_instance = RecoverVmwareVmNewNetworkConfigMapping.from_json(json)
# print the JSON string representation of the object
print(RecoverVmwareVmNewNetworkConfigMapping.to_json())

# convert the object into a dict
recover_vmware_vm_new_network_config_mapping_dict = recover_vmware_vm_new_network_config_mapping_instance.to_dict()
# create an instance of RecoverVmwareVmNewNetworkConfigMapping from a dict
recover_vmware_vm_new_network_config_mapping_from_dict = RecoverVmwareVmNewNetworkConfigMapping.from_dict(recover_vmware_vm_new_network_config_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


