# RecoverKvmVmOriginalSourceConfig

Specifies the Source configuration if VM's are being recovered to Original Source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_config** | [**RecoverKvmVmOriginalSourceNetworkConfig**](RecoverKvmVmOriginalSourceNetworkConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.recover_kvm_vm_original_source_config import RecoverKvmVmOriginalSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverKvmVmOriginalSourceConfig from a JSON string
recover_kvm_vm_original_source_config_instance = RecoverKvmVmOriginalSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverKvmVmOriginalSourceConfig.to_json())

# convert the object into a dict
recover_kvm_vm_original_source_config_dict = recover_kvm_vm_original_source_config_instance.to_dict()
# create an instance of RecoverKvmVmOriginalSourceConfig from a dict
recover_kvm_vm_original_source_config_from_dict = RecoverKvmVmOriginalSourceConfig.from_dict(recover_kvm_vm_original_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


