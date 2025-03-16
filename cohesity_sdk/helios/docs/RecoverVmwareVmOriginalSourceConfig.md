# RecoverVmwareVmOriginalSourceConfig

Specifies the Source configuration if VM's are being recovered to Original Source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_config** | [**RecoverVmwareVmOriginalSourceNetworkConfig**](RecoverVmwareVmOriginalSourceNetworkConfig.md) | Specifies the networking configuration to be applied to the recovered VMs. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.recover_vmware_vm_original_source_config import RecoverVmwareVmOriginalSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverVmwareVmOriginalSourceConfig from a JSON string
recover_vmware_vm_original_source_config_instance = RecoverVmwareVmOriginalSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverVmwareVmOriginalSourceConfig.to_json())

# convert the object into a dict
recover_vmware_vm_original_source_config_dict = recover_vmware_vm_original_source_config_instance.to_dict()
# create an instance of RecoverVmwareVmOriginalSourceConfig from a dict
recover_vmware_vm_original_source_config_from_dict = RecoverVmwareVmOriginalSourceConfig.from_dict(recover_vmware_vm_original_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


