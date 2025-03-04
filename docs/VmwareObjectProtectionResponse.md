# VmwareObjectProtectionResponse

Specifies the input for a protection object in the VMware environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_disks** | [**List[DiskInfo]**](DiskInfo.md) | Specifies a list of disks to exclude from being protected. This is only applicable to VM objects. | [optional] 
**truncate_exchange_logs** | **bool** | Specifies whether or not to truncate MS Exchange logs while taking an app consistent snapshot of this object. This is only applicable to objects which have a registered MS Exchange app. | [optional] 
**cdp_info** | [**VmwareCdpObject**](VmwareCdpObject.md) |  | [optional] 
**exclude_object_ids** | **List[Optional[int]]** | Specifies the list of IDs of the objects to not be protected in this backup. This field only applies if provided object id is non leaf entity such as Tag or a folder. This can be used to ignore specific objects under a parent object which has been included for protection. | [optional] 
**standby_info** | [**VmwareStandbyObject**](VmwareStandbyObject.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.vmware_object_protection_response import VmwareObjectProtectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareObjectProtectionResponse from a JSON string
vmware_object_protection_response_instance = VmwareObjectProtectionResponse.from_json(json)
# print the JSON string representation of the object
print(VmwareObjectProtectionResponse.to_json())

# convert the object into a dict
vmware_object_protection_response_dict = vmware_object_protection_response_instance.to_dict()
# create an instance of VmwareObjectProtectionResponse from a dict
vmware_object_protection_response_from_dict = VmwareObjectProtectionResponse.from_dict(vmware_object_protection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


