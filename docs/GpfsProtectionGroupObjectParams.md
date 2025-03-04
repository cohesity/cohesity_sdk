# GpfsProtectionGroupObjectParams

Specifies an object protected by a GPFS Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the object. | 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.gpfs_protection_group_object_params import GpfsProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of GpfsProtectionGroupObjectParams from a JSON string
gpfs_protection_group_object_params_instance = GpfsProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(GpfsProtectionGroupObjectParams.to_json())

# convert the object into a dict
gpfs_protection_group_object_params_dict = gpfs_protection_group_object_params_instance.to_dict()
# create an instance of GpfsProtectionGroupObjectParams from a dict
gpfs_protection_group_object_params_from_dict = GpfsProtectionGroupObjectParams.from_dict(gpfs_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


