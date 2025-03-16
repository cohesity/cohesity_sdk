# RecoverVmwareDiskParams

Specifies the parameters to recover VMware Disks.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 
**vmware_target_params** | [**VmwareTargetParamsForRecoverDisk**](VmwareTargetParamsForRecoverDisk.md) | Specifies the params for recovering to a VMware target. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.recover_vmware_disk_params import RecoverVmwareDiskParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverVmwareDiskParams from a JSON string
recover_vmware_disk_params_instance = RecoverVmwareDiskParams.from_json(json)
# print the JSON string representation of the object
print(RecoverVmwareDiskParams.to_json())

# convert the object into a dict
recover_vmware_disk_params_dict = recover_vmware_disk_params_instance.to_dict()
# create an instance of RecoverVmwareDiskParams from a dict
recover_vmware_disk_params_from_dict = RecoverVmwareDiskParams.from_dict(recover_vmware_disk_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


