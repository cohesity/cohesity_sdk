# GcpVmRecoveryTargetConfig

Specifies the target object parameters to recover GCP vms.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverGcpVmNewSourceConfig**](RecoverGcpVmNewSourceConfig.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing Source Target. | 

## Example

```python
from cohesity_sdk.cluster.models.gcp_vm_recovery_target_config import GcpVmRecoveryTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GcpVmRecoveryTargetConfig from a JSON string
gcp_vm_recovery_target_config_instance = GcpVmRecoveryTargetConfig.from_json(json)
# print the JSON string representation of the object
print(GcpVmRecoveryTargetConfig.to_json())

# convert the object into a dict
gcp_vm_recovery_target_config_dict = gcp_vm_recovery_target_config_instance.to_dict()
# create an instance of GcpVmRecoveryTargetConfig from a dict
gcp_vm_recovery_target_config_from_dict = GcpVmRecoveryTargetConfig.from_dict(gcp_vm_recovery_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


