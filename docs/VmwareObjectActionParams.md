# VmwareObjectActionParams

Specifies the parameters to perform an action on VMware Objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specifies the action on the Object. | 
**enable_app_protection_params** | [**VmwareObjectEnableAppProtectionParams**](VmwareObjectEnableAppProtectionParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.vmware_object_action_params import VmwareObjectActionParams

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareObjectActionParams from a JSON string
vmware_object_action_params_instance = VmwareObjectActionParams.from_json(json)
# print the JSON string representation of the object
print(VmwareObjectActionParams.to_json())

# convert the object into a dict
vmware_object_action_params_dict = vmware_object_action_params_instance.to_dict()
# create an instance of VmwareObjectActionParams from a dict
vmware_object_action_params_from_dict = VmwareObjectActionParams.from_dict(vmware_object_action_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


