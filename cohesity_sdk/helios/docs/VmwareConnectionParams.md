# VmwareConnectionParams

Specifies the parameters to connect to a seed node and fetch information from its config file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Specifies the VMware Source type. | 
**vcd_params** | [**VcdConnectionParams**](VcdConnectionParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.vmware_connection_params import VmwareConnectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareConnectionParams from a JSON string
vmware_connection_params_instance = VmwareConnectionParams.from_json(json)
# print the JSON string representation of the object
print(VmwareConnectionParams.to_json())

# convert the object into a dict
vmware_connection_params_dict = vmware_connection_params_instance.to_dict()
# create an instance of VmwareConnectionParams from a dict
vmware_connection_params_from_dict = VmwareConnectionParams.from_dict(vmware_connection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


