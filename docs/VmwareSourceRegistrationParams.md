# VmwareSourceRegistrationParams

Specifies the paramaters to register a VMware source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**esxi_params** | [**EsxiRegistrationParams**](EsxiRegistrationParams.md) |  | [optional] 
**type** | **str** | Specifies the VMware Source type. | 
**v_center_params** | [**VcenterRegistrationParams**](VcenterRegistrationParams.md) |  | [optional] 
**vcd_params** | [**VcdRegistrationParams**](VcdRegistrationParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.vmware_source_registration_params import VmwareSourceRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareSourceRegistrationParams from a JSON string
vmware_source_registration_params_instance = VmwareSourceRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(VmwareSourceRegistrationParams.to_json())

# convert the object into a dict
vmware_source_registration_params_dict = vmware_source_registration_params_instance.to_dict()
# create an instance of VmwareSourceRegistrationParams from a dict
vmware_source_registration_params_from_dict = VmwareSourceRegistrationParams.from_dict(vmware_source_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


