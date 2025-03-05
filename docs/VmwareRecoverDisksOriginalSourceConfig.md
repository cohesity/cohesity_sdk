# VmwareRecoverDisksOriginalSourceConfig

Specifies the configuration for restoring a disk to the original VM from which the snapshot was taken.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disks** | [**List[VmwareRecoverOriginalSourceDiskParams]**](VmwareRecoverOriginalSourceDiskParams.md) | Specifies the disks to be recovered and the location to which they will be recovered. | 

## Example

```python
from cohesity_sdk.models.vmware_recover_disks_original_source_config import VmwareRecoverDisksOriginalSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareRecoverDisksOriginalSourceConfig from a JSON string
vmware_recover_disks_original_source_config_instance = VmwareRecoverDisksOriginalSourceConfig.from_json(json)
# print the JSON string representation of the object
print(VmwareRecoverDisksOriginalSourceConfig.to_json())

# convert the object into a dict
vmware_recover_disks_original_source_config_dict = vmware_recover_disks_original_source_config_instance.to_dict()
# create an instance of VmwareRecoverDisksOriginalSourceConfig from a dict
vmware_recover_disks_original_source_config_from_dict = VmwareRecoverDisksOriginalSourceConfig.from_dict(vmware_recover_disks_original_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


