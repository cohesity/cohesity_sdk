# MountVmwareVolumeParams

Specifies the parameters to mount VMware Volumes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 
**vmware_target_params** | [**VmwareTargetParamsForMountVolume**](VmwareTargetParamsForMountVolume.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.mount_vmware_volume_params import MountVmwareVolumeParams

# TODO update the JSON string below
json = "{}"
# create an instance of MountVmwareVolumeParams from a JSON string
mount_vmware_volume_params_instance = MountVmwareVolumeParams.from_json(json)
# print the JSON string representation of the object
print(MountVmwareVolumeParams.to_json())

# convert the object into a dict
mount_vmware_volume_params_dict = mount_vmware_volume_params_instance.to_dict()
# create an instance of MountVmwareVolumeParams from a dict
mount_vmware_volume_params_from_dict = MountVmwareVolumeParams.from_dict(mount_vmware_volume_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


