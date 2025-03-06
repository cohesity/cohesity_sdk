# RecoverHyperVVmNewSourceConfig

Specifies the new destination Source configuration where the VMs will be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scvmm_server_params** | [**RecoverHyperVVmSCVMMSourceConfig**](RecoverHyperVVmSCVMMSourceConfig.md) |  | [optional] 
**source_type** | **str** | Specifies the type of HyperV source to which the VMs are being restored. | 
**standalone_cluster_params** | [**RecoverHyperVVmStandaloneClusterSourceConfig**](RecoverHyperVVmStandaloneClusterSourceConfig.md) |  | [optional] 
**standalone_host_params** | [**RecoverHyperVVmStandaloneHostSourceConfig**](RecoverHyperVVmStandaloneHostSourceConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_hyper_vvm_new_source_config import RecoverHyperVVmNewSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverHyperVVmNewSourceConfig from a JSON string
recover_hyper_vvm_new_source_config_instance = RecoverHyperVVmNewSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverHyperVVmNewSourceConfig.to_json())

# convert the object into a dict
recover_hyper_vvm_new_source_config_dict = recover_hyper_vvm_new_source_config_instance.to_dict()
# create an instance of RecoverHyperVVmNewSourceConfig from a dict
recover_hyper_vvm_new_source_config_from_dict = RecoverHyperVVmNewSourceConfig.from_dict(recover_hyper_vvm_new_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


