# VmwareTargetParamsForMountVolume

Specifies the parameters for a VMware mount volume target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mount_to_original_target** | **bool** | Specifies whether to mount to the original target. If true, originalTargetConfig must be specified. If false, newTargetConfig must be specified. | 
**mounted_volume_mapping** | [**List[MountedVolumeMapping]**](MountedVolumeMapping.md) | Specifies the mapping of original volumes and mounted volumes | [optional] [readonly] 
**new_target_config** | [**VMwareMountVolumesNewTargetConfig**](VMwareMountVolumesNewTargetConfig.md) |  | [optional] 
**original_target_config** | [**VMwareMountVolumesOriginalTargetConfig**](VMwareMountVolumesOriginalTargetConfig.md) |  | [optional] 
**read_only_mount** | **bool** | Specifies whether to perform a read-only mount. Default is false. | [optional] 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 
**volume_names** | **List[str]** | Specifies the names of volumes that need to be mounted. If this is not specified then all volumes that are part of the source VM will be mounted on the target VM. | [optional] 

## Example

```python
from cohesity_sdk.models.vmware_target_params_for_mount_volume import VmwareTargetParamsForMountVolume

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareTargetParamsForMountVolume from a JSON string
vmware_target_params_for_mount_volume_instance = VmwareTargetParamsForMountVolume.from_json(json)
# print the JSON string representation of the object
print(VmwareTargetParamsForMountVolume.to_json())

# convert the object into a dict
vmware_target_params_for_mount_volume_dict = vmware_target_params_for_mount_volume_instance.to_dict()
# create an instance of VmwareTargetParamsForMountVolume from a dict
vmware_target_params_for_mount_volume_from_dict = VmwareTargetParamsForMountVolume.from_dict(vmware_target_params_for_mount_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


