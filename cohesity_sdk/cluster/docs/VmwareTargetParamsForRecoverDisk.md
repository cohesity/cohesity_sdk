# VmwareTargetParamsForRecoverDisk

Specifies the parameters for a VMware recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool** | Specifies whether or not to continue performing the recovery in the event that an error is encountered. | [optional] 
**original_source_config** | [**VmwareRecoverDisksOriginalSourceConfig**](VmwareRecoverDisksOriginalSourceConfig.md) |  | [optional] 
**power_off_vms** | **bool** | Specifies whether or not to power off VMs before performing the recovery. | [optional] 
**power_on_vms** | **bool** | Specifies whether or not to power on VMs after performing the recovery. | [optional] 
**target_source_config** | [**VmwareRecoverDisksTargetSourceConfig**](VmwareRecoverDisksTargetSourceConfig.md) |  | [optional] 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.vmware_target_params_for_recover_disk import VmwareTargetParamsForRecoverDisk

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareTargetParamsForRecoverDisk from a JSON string
vmware_target_params_for_recover_disk_instance = VmwareTargetParamsForRecoverDisk.from_json(json)
# print the JSON string representation of the object
print(VmwareTargetParamsForRecoverDisk.to_json())

# convert the object into a dict
vmware_target_params_for_recover_disk_dict = vmware_target_params_for_recover_disk_instance.to_dict()
# create an instance of VmwareTargetParamsForRecoverDisk from a dict
vmware_target_params_for_recover_disk_from_dict = VmwareTargetParamsForRecoverDisk.from_dict(vmware_target_params_for_recover_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


