# HyperVMountVolumesOriginalTargetConfig

Specifies the configuration for mounting volumes to the original target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bring_disks_online** | **bool** | Specifies whether the volumes need to be online within the target environment after attaching the disks. For linux VMs, this should always be set to false because bring disks online is only supported for Windows VM. For Windows, this is optional. If this is set to true, HyperV Integration Services must be installed on the VM. | 
**target_vm_credentials** | [**Credentials**](Credentials.md) | Specifies credentials to access the target VM. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.hyper_v_mount_volumes_original_target_config import HyperVMountVolumesOriginalTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HyperVMountVolumesOriginalTargetConfig from a JSON string
hyper_v_mount_volumes_original_target_config_instance = HyperVMountVolumesOriginalTargetConfig.from_json(json)
# print the JSON string representation of the object
print(HyperVMountVolumesOriginalTargetConfig.to_json())

# convert the object into a dict
hyper_v_mount_volumes_original_target_config_dict = hyper_v_mount_volumes_original_target_config_instance.to_dict()
# create an instance of HyperVMountVolumesOriginalTargetConfig from a dict
hyper_v_mount_volumes_original_target_config_from_dict = HyperVMountVolumesOriginalTargetConfig.from_dict(hyper_v_mount_volumes_original_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


