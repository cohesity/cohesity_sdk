# VmwareRecoverDisksTargetSourceConfig

Specifies the configuration for restoring disks to a different VM than the one from which the snapshot was taken.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disks** | [**List[VmwareRecoverTargetSourceDiskParams]**](VmwareRecoverTargetSourceDiskParams.md) | Specifies the disks to be recovered and the location to which they will be recovered. | 
**source_id** | **int** | Specifies the source ID of the VM to which the disks will be restored. | 

## Example

```python
from cohesity_sdk.helios.models.vmware_recover_disks_target_source_config import VmwareRecoverDisksTargetSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareRecoverDisksTargetSourceConfig from a JSON string
vmware_recover_disks_target_source_config_instance = VmwareRecoverDisksTargetSourceConfig.from_json(json)
# print the JSON string representation of the object
print(VmwareRecoverDisksTargetSourceConfig.to_json())

# convert the object into a dict
vmware_recover_disks_target_source_config_dict = vmware_recover_disks_target_source_config_instance.to_dict()
# create an instance of VmwareRecoverDisksTargetSourceConfig from a dict
vmware_recover_disks_target_source_config_from_dict = VmwareRecoverDisksTargetSourceConfig.from_dict(vmware_recover_disks_target_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


