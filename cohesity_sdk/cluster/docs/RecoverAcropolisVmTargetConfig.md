# RecoverAcropolisVmTargetConfig

Specifies the target configuration source parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverAcropolisVmNewSourceConfig**](RecoverAcropolisVmNewSourceConfig.md) |  | [optional] 
**original_source_config** | [**RecoverAcropolisVmOriginalSourceConfig**](RecoverAcropolisVmOriginalSourceConfig.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing Source Target. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_acropolis_vm_target_config import RecoverAcropolisVmTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAcropolisVmTargetConfig from a JSON string
recover_acropolis_vm_target_config_instance = RecoverAcropolisVmTargetConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverAcropolisVmTargetConfig.to_json())

# convert the object into a dict
recover_acropolis_vm_target_config_dict = recover_acropolis_vm_target_config_instance.to_dict()
# create an instance of RecoverAcropolisVmTargetConfig from a dict
recover_acropolis_vm_target_config_from_dict = RecoverAcropolisVmTargetConfig.from_dict(recover_acropolis_vm_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


