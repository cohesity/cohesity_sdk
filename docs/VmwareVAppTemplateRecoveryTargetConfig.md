# VmwareVAppTemplateRecoveryTargetConfig

Specifies the target object parameters to recover VMware vApp templates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverVmwareVAppTemplateNewSourceConfig**](RecoverVmwareVAppTemplateNewSourceConfig.md) |  | [optional] 
**original_source_config** | [**RecoverVmwareVAppOriginalSourceConfig**](RecoverVmwareVAppOriginalSourceConfig.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing Source Target. | 

## Example

```python
from cohesity_sdk.cluster.models.vmware_v_app_template_recovery_target_config import VmwareVAppTemplateRecoveryTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareVAppTemplateRecoveryTargetConfig from a JSON string
vmware_v_app_template_recovery_target_config_instance = VmwareVAppTemplateRecoveryTargetConfig.from_json(json)
# print the JSON string representation of the object
print(VmwareVAppTemplateRecoveryTargetConfig.to_json())

# convert the object into a dict
vmware_v_app_template_recovery_target_config_dict = vmware_v_app_template_recovery_target_config_instance.to_dict()
# create an instance of VmwareVAppTemplateRecoveryTargetConfig from a dict
vmware_v_app_template_recovery_target_config_from_dict = VmwareVAppTemplateRecoveryTargetConfig.from_dict(vmware_v_app_template_recovery_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


