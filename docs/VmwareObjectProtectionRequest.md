# VmwareObjectProtectionRequest

Specifies the VMware object level settings for object protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_disks** | [**List[DiskInfo]**](DiskInfo.md) | Specifies a list of disks to exclude from being protected. This is only applicable to VM objects. | [optional] 
**truncate_exchange_logs** | **bool** | Specifies whether or not to truncate MS Exchange logs while taking an app consistent snapshot of this object. This is only applicable to objects which have a registered MS Exchange app. | [optional] 
**exclude_object_ids** | **List[Optional[int]]** | Specifies the list of IDs of the objects to not be protected in this backup. This field only applies if provided object id is non leaf entity such as Tag or a folder. This can be used to ignore specific objects under a parent object which has been included for protection. | [optional] 
**id** | **int** | Specifies the id of the object being protected. This can be a leaf level or non leaf level object. | 

## Example

```python
from cohesity_sdk.cluster.models.vmware_object_protection_request import VmwareObjectProtectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareObjectProtectionRequest from a JSON string
vmware_object_protection_request_instance = VmwareObjectProtectionRequest.from_json(json)
# print the JSON string representation of the object
print(VmwareObjectProtectionRequest.to_json())

# convert the object into a dict
vmware_object_protection_request_dict = vmware_object_protection_request_instance.to_dict()
# create an instance of VmwareObjectProtectionRequest from a dict
vmware_object_protection_request_from_dict = VmwareObjectProtectionRequest.from_dict(vmware_object_protection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


