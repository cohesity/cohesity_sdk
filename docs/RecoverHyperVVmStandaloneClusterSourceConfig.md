# RecoverHyperVVmStandaloneClusterSourceConfig

Specifies the new destination Source configuration where the VMs will be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**network_config** | [**RecoverHyperVVmNewSourceNetworkConfig**](RecoverHyperVVmNewSourceNetworkConfig.md) |  | [optional] 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**volume** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.models.recover_hyper_vvm_standalone_cluster_source_config import RecoverHyperVVmStandaloneClusterSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverHyperVVmStandaloneClusterSourceConfig from a JSON string
recover_hyper_vvm_standalone_cluster_source_config_instance = RecoverHyperVVmStandaloneClusterSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverHyperVVmStandaloneClusterSourceConfig.to_json())

# convert the object into a dict
recover_hyper_vvm_standalone_cluster_source_config_dict = recover_hyper_vvm_standalone_cluster_source_config_instance.to_dict()
# create an instance of RecoverHyperVVmStandaloneClusterSourceConfig from a dict
recover_hyper_vvm_standalone_cluster_source_config_from_dict = RecoverHyperVVmStandaloneClusterSourceConfig.from_dict(recover_hyper_vvm_standalone_cluster_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


