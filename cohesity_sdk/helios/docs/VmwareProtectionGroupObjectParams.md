# VmwareProtectionGroupObjectParams

Specifies the input for a protection object in the VMware environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_disks** | [**List[DiskInfo]**](DiskInfo.md) | Specifies a list of disks to exclude from being protected. This is only applicable to VM objects. | [optional] 
**truncate_exchange_logs** | **bool** | Specifies whether or not to truncate MS Exchange logs while taking an app consistent snapshot of this object. This is only applicable to objects which have a registered MS Exchange app. | [optional] 
**cdp_info** | **object** | Specifies the CDP related information for a given object. This field will only be populated when protection group is configured with policy having CDP retnetion settings. | [optional] 
**id** | **int** | Specifies the id of the object being protected. This can be a leaf level or non leaf level object. | 
**is_autoprotected** | **bool** | Specifies whether the vm is part of an Autoprotection and there is at least one object-specific setting applied to this vm. True implies that the vm or its parent directory is autoprotected and will remain part of the autoprotection with additional settings specified here. False implies the object is not part of an Autoprotection and will remain protected and its individual settings here even if a parent directory&#39;s Autoprotection setting is altered. Default is false. | [optional] 
**name** | **str** | Specifies the name of the virtual machine. | [optional] [readonly] 
**standby_info** | **object** | Specifies the standby related information for a given object. This field will only be populated when standby is configured in backup job settings. | [optional] 
**type** | **str** | Specifies the type of the VMware object. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.vmware_protection_group_object_params import VmwareProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareProtectionGroupObjectParams from a JSON string
vmware_protection_group_object_params_instance = VmwareProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(VmwareProtectionGroupObjectParams.to_json())

# convert the object into a dict
vmware_protection_group_object_params_dict = vmware_protection_group_object_params_instance.to_dict()
# create an instance of VmwareProtectionGroupObjectParams from a dict
vmware_protection_group_object_params_from_dict = VmwareProtectionGroupObjectParams.from_dict(vmware_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


