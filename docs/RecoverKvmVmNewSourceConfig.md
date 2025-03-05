# RecoverKvmVmNewSourceConfig

Specifies the new destination Source configuration where the VMs will be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**data_center** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**network_config** | [**RecoverKvmVmNewSourceNetworkConfig**](RecoverKvmVmNewSourceNetworkConfig.md) |  | [optional] 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**storage_domain** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.models.recover_kvm_vm_new_source_config import RecoverKvmVmNewSourceConfig

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


