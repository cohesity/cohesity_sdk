# RecoverAcropolisVmOriginalSourceNetworkConfig

Specifies the network config parameters to be applied for Acropolis VMs if recovering to original Source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detach_network** | **bool** | If this is set to true, then the network will be detached from the recovered VMs. All the other networking parameters set will be ignored if set to true. Default value is false. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.recover_acropolis_vm_original_source_network_config import RecoverAcropolisVmOriginalSourceNetworkConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAcropolisVmOriginalSourceNetworkConfig from a JSON string
recover_acropolis_vm_original_source_network_config_instance = RecoverAcropolisVmOriginalSourceNetworkConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverAcropolisVmOriginalSourceNetworkConfig.to_json())

# convert the object into a dict
recover_acropolis_vm_original_source_network_config_dict = recover_acropolis_vm_original_source_network_config_instance.to_dict()
# create an instance of RecoverAcropolisVmOriginalSourceNetworkConfig from a dict
recover_acropolis_vm_original_source_network_config_from_dict = RecoverAcropolisVmOriginalSourceNetworkConfig.from_dict(recover_acropolis_vm_original_source_network_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


