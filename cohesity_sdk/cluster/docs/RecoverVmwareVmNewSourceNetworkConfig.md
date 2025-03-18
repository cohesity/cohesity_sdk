# RecoverVmwareVmNewSourceNetworkConfig

Specifies the network config parameters to be applied to VMware VMs if recovering to new Source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detach_network** | **bool** | If this is set to true, then the network will be detached from the recovered VMs. All the other networking parameters set will be ignored if set to true. Default value is false. | [optional] 
**new_network_config** | [**RecoverVmwareVmNewNetworkConfig**](RecoverVmwareVmNewNetworkConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_vmware_vm_new_source_network_config import RecoverVmwareVmNewSourceNetworkConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverVmwareVmNewSourceNetworkConfig from a JSON string
recover_vmware_vm_new_source_network_config_instance = RecoverVmwareVmNewSourceNetworkConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverVmwareVmNewSourceNetworkConfig.to_json())

# convert the object into a dict
recover_vmware_vm_new_source_network_config_dict = recover_vmware_vm_new_source_network_config_instance.to_dict()
# create an instance of RecoverVmwareVmNewSourceNetworkConfig from a dict
recover_vmware_vm_new_source_network_config_from_dict = RecoverVmwareVmNewSourceNetworkConfig.from_dict(recover_vmware_vm_new_source_network_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


