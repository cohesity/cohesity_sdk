# RecoverAcropolisVmNewSourceNetworkConfig

Specifies the network config parameters to applied for Acropolis VMs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detach_network** | **bool** | If this is set to true, then the network will be detached from the recovered VMs. All the other networking parameters set will be ignored if set to true. Default value is false. | [optional] 
**network_port_group** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.recover_acropolis_vm_new_source_network_config import RecoverAcropolisVmNewSourceNetworkConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAcropolisVmNewSourceNetworkConfig from a JSON string
recover_acropolis_vm_new_source_network_config_instance = RecoverAcropolisVmNewSourceNetworkConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverAcropolisVmNewSourceNetworkConfig.to_json())

# convert the object into a dict
recover_acropolis_vm_new_source_network_config_dict = recover_acropolis_vm_new_source_network_config_instance.to_dict()
# create an instance of RecoverAcropolisVmNewSourceNetworkConfig from a dict
recover_acropolis_vm_new_source_network_config_from_dict = RecoverAcropolisVmNewSourceNetworkConfig.from_dict(recover_acropolis_vm_new_source_network_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


