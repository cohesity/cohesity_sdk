# VmwareVAppRecoveryTargetConfig

Specifies the target object parameters to recover VMware vApps.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverVmwareVAppNewSourceConfig**](RecoverVmwareVAppNewSourceConfig.md) |  | [optional] 
**original_source_config** | [**RecoverVmwareVAppOriginalSourceConfig**](RecoverVmwareVAppOriginalSourceConfig.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing Source Target. | 

## Example

```python
from cohesity_sdk.models.vmware_v_app_recovery_target_config import VmwareVAppRecoveryTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareVAppRecoveryTargetConfig from a JSON string
vmware_v_app_recovery_target_config_instance = VmwareVAppRecoveryTargetConfig.from_json(json)
# print the JSON string representation of the object
print(VmwareVAppRecoveryTargetConfig.to_json())

# convert the object into a dict
vmware_v_app_recovery_target_config_dict = vmware_v_app_recovery_target_config_instance.to_dict()
# create an instance of VmwareVAppRecoveryTargetConfig from a dict
vmware_v_app_recovery_target_config_from_dict = VmwareVAppRecoveryTargetConfig.from_dict(vmware_v_app_recovery_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


