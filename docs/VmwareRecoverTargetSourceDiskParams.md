# VmwareRecoverTargetSourceDiskParams

Specifies disk specific parameters for performing a disk recovery.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore_id** | **int** | Specifies the ID of the datastore on which the specified disk will be spun up. | 
**disk_uuid** | **str** | Specifies the UUID of the source disk being recovered. | 

## Example

```python
from cohesity_sdk.models.vmware_recover_target_source_disk_params import VmwareRecoverTargetSourceDiskParams

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareRecoverTargetSourceDiskParams from a JSON string
vmware_recover_target_source_disk_params_instance = VmwareRecoverTargetSourceDiskParams.from_json(json)
# print the JSON string representation of the object
print(VmwareRecoverTargetSourceDiskParams.to_json())

# convert the object into a dict
vmware_recover_target_source_disk_params_dict = vmware_recover_target_source_disk_params_instance.to_dict()
# create an instance of VmwareRecoverTargetSourceDiskParams from a dict
vmware_recover_target_source_disk_params_from_dict = VmwareRecoverTargetSourceDiskParams.from_dict(vmware_recover_target_source_disk_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


