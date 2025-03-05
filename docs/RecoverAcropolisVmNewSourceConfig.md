# RecoverAcropolisVmNewSourceConfig

Specifies the new destination Source configuration where the VMs will be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_config** | [**RecoverAcropolisVmNewSourceNetworkConfig**](RecoverAcropolisVmNewSourceNetworkConfig.md) |  | [optional] 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**storage_container** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.recover_acropolis_vm_new_source_config import RecoverAcropolisVmNewSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAcropolisVmNewSourceConfig from a JSON string
recover_acropolis_vm_new_source_config_instance = RecoverAcropolisVmNewSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverAcropolisVmNewSourceConfig.to_json())

# convert the object into a dict
recover_acropolis_vm_new_source_config_dict = recover_acropolis_vm_new_source_config_instance.to_dict()
# create an instance of RecoverAcropolisVmNewSourceConfig from a dict
recover_acropolis_vm_new_source_config_from_dict = RecoverAcropolisVmNewSourceConfig.from_dict(recover_acropolis_vm_new_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


