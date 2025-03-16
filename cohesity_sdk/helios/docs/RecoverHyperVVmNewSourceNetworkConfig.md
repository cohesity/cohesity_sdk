# RecoverHyperVVmNewSourceNetworkConfig

Specifies the network config parameters to be applied for HyperV VMs if recovering to new Source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detach_network** | **bool** | If this is set to true, then the network will be detached from the recovered VMs. All the other networking parameters set will be ignored if set to true. Default value is false. | [optional] 
**virtual_switch** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the virtual switch that will attached to all the network interfaces of the VMs being recovered. This parameter is mandatory if detach network is specified as false. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.recover_hyper_vvm_new_source_network_config import RecoverHyperVVmNewSourceNetworkConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverHyperVVmNewSourceNetworkConfig from a JSON string
recover_hyper_vvm_new_source_network_config_instance = RecoverHyperVVmNewSourceNetworkConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverHyperVVmNewSourceNetworkConfig.to_json())

# convert the object into a dict
recover_hyper_vvm_new_source_network_config_dict = recover_hyper_vvm_new_source_network_config_instance.to_dict()
# create an instance of RecoverHyperVVmNewSourceNetworkConfig from a dict
recover_hyper_vvm_new_source_network_config_from_dict = RecoverHyperVVmNewSourceNetworkConfig.from_dict(recover_hyper_vvm_new_source_network_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


