# VmwareAdditionalParams

Additional params for VMware protection source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vcd_params** | [**VcdAdditionalParams**](VcdAdditionalParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.vmware_additional_params import VmwareAdditionalParams

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareAdditionalParams from a JSON string
vmware_additional_params_instance = VmwareAdditionalParams.from_json(json)
# print the JSON string representation of the object
print(VmwareAdditionalParams.to_json())

# convert the object into a dict
vmware_additional_params_dict = vmware_additional_params_instance.to_dict()
# create an instance of VmwareAdditionalParams from a dict
vmware_additional_params_from_dict = VmwareAdditionalParams.from_dict(vmware_additional_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


