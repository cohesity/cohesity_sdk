# NutanixFSProtectionGroupObjectParams

Specifies an object protected by a Nutanix FS Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the object. | 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.nutanix_fs_protection_group_object_params import NutanixFSProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of NutanixFSProtectionGroupObjectParams from a JSON string
nutanix_fs_protection_group_object_params_instance = NutanixFSProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(NutanixFSProtectionGroupObjectParams.to_json())

# convert the object into a dict
nutanix_fs_protection_group_object_params_dict = nutanix_fs_protection_group_object_params_instance.to_dict()
# create an instance of NutanixFSProtectionGroupObjectParams from a dict
nutanix_fs_protection_group_object_params_from_dict = NutanixFSProtectionGroupObjectParams.from_dict(nutanix_fs_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


