# RecoverHyperVVmStandaloneHostSourceConfig

Specifies the new destination Source configuration where the VMs will be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_config** | [**RecoverHyperVVmNewSourceNetworkConfig**](RecoverHyperVVmNewSourceNetworkConfig.md) | Specifies the networking configuration to be applied to the recovered VMs. | [optional] 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the id of the parent source to recover the VMs. | 
**volume** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the datastore object where the VMs&#39; files should be recovered to. | 

## Example

```python
from cohesity_sdk.helios.models.recover_hyper_vvm_standalone_host_source_config import RecoverHyperVVmStandaloneHostSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverHyperVVmStandaloneHostSourceConfig from a JSON string
recover_hyper_vvm_standalone_host_source_config_instance = RecoverHyperVVmStandaloneHostSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverHyperVVmStandaloneHostSourceConfig.to_json())

# convert the object into a dict
recover_hyper_vvm_standalone_host_source_config_dict = recover_hyper_vvm_standalone_host_source_config_instance.to_dict()
# create an instance of RecoverHyperVVmStandaloneHostSourceConfig from a dict
recover_hyper_vvm_standalone_host_source_config_from_dict = RecoverHyperVVmStandaloneHostSourceConfig.from_dict(recover_hyper_vvm_standalone_host_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


