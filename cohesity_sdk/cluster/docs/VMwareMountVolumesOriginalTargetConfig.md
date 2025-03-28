# VMwareMountVolumesOriginalTargetConfig

Specifies the configuration for mounting volumes to the original target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bring_disks_online** | **bool** | Specifies whether the volumes need to be online within the target environment after attaching the disks. For linux VMs, this should always be set to true. For Windows, this is optional. If this is set to true, VMware tools must be installed on the VM. If this is set to false, useExistingAgent and targetCredentials are not needed. | 
**target_vm_credentials** | [**Credentials**](Credentials.md) |  | [optional] 
**use_existing_agent** | **bool** | Specifies whether this will use an existing agent on the target vm or will deploy a new agent. This is required if bringDisksOnline is set to true. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.v_mware_mount_volumes_original_target_config import VMwareMountVolumesOriginalTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VMwareMountVolumesOriginalTargetConfig from a JSON string
v_mware_mount_volumes_original_target_config_instance = VMwareMountVolumesOriginalTargetConfig.from_json(json)
# print the JSON string representation of the object
print(VMwareMountVolumesOriginalTargetConfig.to_json())

# convert the object into a dict
v_mware_mount_volumes_original_target_config_dict = v_mware_mount_volumes_original_target_config_instance.to_dict()
# create an instance of VMwareMountVolumesOriginalTargetConfig from a dict
v_mware_mount_volumes_original_target_config_from_dict = VMwareMountVolumesOriginalTargetConfig.from_dict(v_mware_mount_volumes_original_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


