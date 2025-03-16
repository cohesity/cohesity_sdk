# RecoverHyperVVmSCVMMSourceConfig

Specifies the new destination Source configuration where the VMs will be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the HyperV host where the recovered VMs will be attached. For standalone host targets, the host must be the same as the source. | 
**network_config** | [**RecoverHyperVVmNewSourceNetworkConfig**](RecoverHyperVVmNewSourceNetworkConfig.md) | Specifies the networking configuration to be applied to the recovered VMs. | [optional] 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the id of the parent source to recover the VMs. | 
**volume** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the datastore object where the VMs&#39; files should be recovered to. | 

## Example

```python
from cohesity_sdk.helios.models.recover_hyper_vvm_scvmm_source_config import RecoverHyperVVmSCVMMSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverHyperVVmSCVMMSourceConfig from a JSON string
recover_hyper_vvm_scvmm_source_config_instance = RecoverHyperVVmSCVMMSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverHyperVVmSCVMMSourceConfig.to_json())

# convert the object into a dict
recover_hyper_vvm_scvmm_source_config_dict = recover_hyper_vvm_scvmm_source_config_instance.to_dict()
# create an instance of RecoverHyperVVmSCVMMSourceConfig from a dict
recover_hyper_vvm_scvmm_source_config_from_dict = RecoverHyperVVmSCVMMSourceConfig.from_dict(recover_hyper_vvm_scvmm_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


