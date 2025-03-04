# GcpNativeProtectionGroupObjectParams

Specifies the object parameters to create GCP Native Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_exclusion_name_params** | **List[str]** | Specifies the paramaters to exclude disks attached to GCP VM instances. Here only the name of the disks are taken for exclusion. | [optional] 
**id** | **int** | Specifies the id of the object. | 
**name** | **str** | Specifies the name of the virtual machine. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.gcp_native_protection_group_object_params import GcpNativeProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of GcpNativeProtectionGroupObjectParams from a JSON string
gcp_native_protection_group_object_params_instance = GcpNativeProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(GcpNativeProtectionGroupObjectParams.to_json())

# convert the object into a dict
gcp_native_protection_group_object_params_dict = gcp_native_protection_group_object_params_instance.to_dict()
# create an instance of GcpNativeProtectionGroupObjectParams from a dict
gcp_native_protection_group_object_params_from_dict = GcpNativeProtectionGroupObjectParams.from_dict(gcp_native_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


