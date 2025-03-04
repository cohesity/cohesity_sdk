# HyperVTargetParamsForMountVolume

Specifies the parameters for a HyperV recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mount_to_original_target** | **bool** | Specifies whether to mount to the original target. If true, originalTargetConfig must be specified. If false, newTargetConfig must be specified. | 
**mounted_volume_mapping** | [**List[MountedVolumeMapping]**](MountedVolumeMapping.md) | Specifies the mapping of original volumes and mounted volumes | [optional] [readonly] 
**new_target_config** | [**HyperVMountVolumesNewTargetConfig**](HyperVMountVolumesNewTargetConfig.md) |  | [optional] 
**original_target_config** | [**HyperVMountVolumesOriginalTargetConfig**](HyperVMountVolumesOriginalTargetConfig.md) |  | [optional] 
**read_only_mount** | **bool** | Specifies whether to perform a read-only mount. Default is false. | [optional] 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 
**volume_names** | **List[str]** | Specifies the names of volumes that need to be mounted. If this is not specified then all volumes that are part of the source VM will be mounted on the target VM. | [optional] 

## Example

```python
from cohesity_sdk.models.hyper_v_target_params_for_mount_volume import HyperVTargetParamsForMountVolume

# TODO update the JSON string below
json = "{}"
# create an instance of HyperVTargetParamsForMountVolume from a JSON string
hyper_v_target_params_for_mount_volume_instance = HyperVTargetParamsForMountVolume.from_json(json)
# print the JSON string representation of the object
print(HyperVTargetParamsForMountVolume.to_json())

# convert the object into a dict
hyper_v_target_params_for_mount_volume_dict = hyper_v_target_params_for_mount_volume_instance.to_dict()
# create an instance of HyperVTargetParamsForMountVolume from a dict
hyper_v_target_params_for_mount_volume_from_dict = HyperVTargetParamsForMountVolume.from_dict(hyper_v_target_params_for_mount_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


