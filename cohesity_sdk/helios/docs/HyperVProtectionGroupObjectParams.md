# HyperVProtectionGroupObjectParams

Specifies the object parameters to create HyperV Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_disks** | [**List[HyperVDiskInfo]**](HyperVDiskInfo.md) | Specifies a list of disks to exclude from being protected for the object/vm. | [optional] 
**id** | **int** | Specifies the id of the object. | 
**include_disks** | [**List[HyperVDiskInfo]**](HyperVDiskInfo.md) | Specifies a list of disks to included in the protection for the object/vm. | [optional] 
**name** | **str** | Specifies the name of the virtual machine. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.hyper_v_protection_group_object_params import HyperVProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of HyperVProtectionGroupObjectParams from a JSON string
hyper_v_protection_group_object_params_instance = HyperVProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(HyperVProtectionGroupObjectParams.to_json())

# convert the object into a dict
hyper_v_protection_group_object_params_dict = hyper_v_protection_group_object_params_instance.to_dict()
# create an instance of HyperVProtectionGroupObjectParams from a dict
hyper_v_protection_group_object_params_from_dict = HyperVProtectionGroupObjectParams.from_dict(hyper_v_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


