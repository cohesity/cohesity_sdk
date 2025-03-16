# GcpVmRecoveryTargetConfig

Specifies the target object parameters to recover GCP vms.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverGcpVmNewSourceConfig**](RecoverGcpVmNewSourceConfig.md) | Specifies the new destination Source configuration parameters where the VMs will be recovered. This is mandatory if recoverToNewSource is set to true. | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing Source Target. | 

## Example

```python
from cohesity_sdk.helios.models.gcp_vm_recovery_target_config import GcpVmRecoveryTargetConfig

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


