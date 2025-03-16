# HyperVVmRecoveryTargetConfig

Specifies the target object parameters to recover HyperV vms.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverHyperVVmNewSourceConfig**](RecoverHyperVVmNewSourceConfig.md) | Specifies the new destination Source configuration parameters where the VMs will be recovered. This is mandatory if recoverToNewSource is set to true. | [optional] 
**original_source_config** | [**RecoverHyperVVmOriginalSourceConfig**](RecoverHyperVVmOriginalSourceConfig.md) | Specifies the Source configuration if VM&#39;s are being recovered to Original Source. If not specified, all the configuration parameters will be retained. | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing Source Target. | 

## Example

```python
from cohesity_sdk.helios.models.hyper_vvm_recovery_target_config import HyperVVmRecoveryTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HyperVVmRecoveryTargetConfig from a JSON string
hyper_vvm_recovery_target_config_instance = HyperVVmRecoveryTargetConfig.from_json(json)
# print the JSON string representation of the object
print(HyperVVmRecoveryTargetConfig.to_json())

# convert the object into a dict
hyper_vvm_recovery_target_config_dict = hyper_vvm_recovery_target_config_instance.to_dict()
# create an instance of HyperVVmRecoveryTargetConfig from a dict
hyper_vvm_recovery_target_config_from_dict = HyperVVmRecoveryTargetConfig.from_dict(hyper_vvm_recovery_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


