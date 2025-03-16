# VmwareObjectEntityParams

Object details for Vmware.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cdp_info** | [**VmwareCdpObject**](VmwareCdpObject.md) |  | [optional] 
**is_template** | **bool** | Specifies if the object is a VM template. | [optional] 
**type** | **str** | VMware Object type. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.vmware_object_entity_params import VmwareObjectEntityParams

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareObjectEntityParams from a JSON string
vmware_object_entity_params_instance = VmwareObjectEntityParams.from_json(json)
# print the JSON string representation of the object
print(VmwareObjectEntityParams.to_json())

# convert the object into a dict
vmware_object_entity_params_dict = vmware_object_entity_params_instance.to_dict()
# create an instance of VmwareObjectEntityParams from a dict
vmware_object_entity_params_from_dict = VmwareObjectEntityParams.from_dict(vmware_object_entity_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


