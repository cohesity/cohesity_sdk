# KvmProtectionGroupObjectParams

Specifies an object protected by a KVM Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the object. | 
**name** | **str** | Specifies the name of the virtual machine. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.kvm_protection_group_object_params import KvmProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of KvmProtectionGroupObjectParams from a JSON string
kvm_protection_group_object_params_instance = KvmProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(KvmProtectionGroupObjectParams.to_json())

# convert the object into a dict
kvm_protection_group_object_params_dict = kvm_protection_group_object_params_instance.to_dict()
# create an instance of KvmProtectionGroupObjectParams from a dict
kvm_protection_group_object_params_from_dict = KvmProtectionGroupObjectParams.from_dict(kvm_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


