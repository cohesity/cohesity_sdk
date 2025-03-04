# VmwareStandbyObject

Specifies the VMware specific standby object details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **int** | Specifies the entity id of the corresponding backup object for which this standby is configured. | [optional] 
**protection_group_id** | **str** | Specifies the protection group id to which this standby object belongs. | [optional] [readonly] 
**cdp_standby_status** | **str** | Specifies the current status of the standby object protected using continuous data protection policy. | [optional] 
**guest_id** | **str** | Specifies the guest ID(OS) of the standby VM for the corresponding backup object. | [optional] [readonly] 
**standby_m_oref** | [**MOref**](MOref.md) |  | [optional] 
**standby_time** | **int** | Specifies the time till which the standby object has been hydrated for the corresponding backup object. | [optional] 

## Example

```python
from cohesity_sdk.models.vmware_standby_object import VmwareStandbyObject

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareStandbyObject from a JSON string
vmware_standby_object_instance = VmwareStandbyObject.from_json(json)
# print the JSON string representation of the object
print(VmwareStandbyObject.to_json())

# convert the object into a dict
vmware_standby_object_dict = vmware_standby_object_instance.to_dict()
# create an instance of VmwareStandbyObject from a dict
vmware_standby_object_from_dict = VmwareStandbyObject.from_dict(vmware_standby_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


