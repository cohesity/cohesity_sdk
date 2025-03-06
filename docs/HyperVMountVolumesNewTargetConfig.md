# HyperVMountVolumesNewTargetConfig

Specifies the configuration for mounting volumes to a new target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bring_disks_online** | **bool** | Specifies whether the volumes need to be online within the target environment after attaching the disks. For linux VMs, this should always be set to false because bring disks online is only supported for Windows VM. If this is set to true, HyperV Integration Services must be installed on the VM. | 
**mount_target** | [**RecoverTarget**](RecoverTarget.md) |  | 
**target_vm_credentials** | [**Credentials**](Credentials.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.hyper_v_mount_volumes_new_target_config import HyperVMountVolumesNewTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HyperVMountVolumesNewTargetConfig from a JSON string
hyper_v_mount_volumes_new_target_config_instance = HyperVMountVolumesNewTargetConfig.from_json(json)
# print the JSON string representation of the object
print(HyperVMountVolumesNewTargetConfig.to_json())

# convert the object into a dict
hyper_v_mount_volumes_new_target_config_dict = hyper_v_mount_volumes_new_target_config_instance.to_dict()
# create an instance of HyperVMountVolumesNewTargetConfig from a dict
hyper_v_mount_volumes_new_target_config_from_dict = HyperVMountVolumesNewTargetConfig.from_dict(hyper_v_mount_volumes_new_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


