# PhysicalProtectionGroupParams

Specifies the parameters specific to Physical Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_protection_type_params** | [**PhysicalFileProtectionGroupParams**](PhysicalFileProtectionGroupParams.md) |  | [optional] 
**protection_type** | **str** | Specifies the Physical Protection Group type. | 
**volume_protection_type_params** | [**PhysicalVolumeProtectionGroupParams**](PhysicalVolumeProtectionGroupParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.physical_protection_group_params import PhysicalProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalProtectionGroupParams from a JSON string
physical_protection_group_params_instance = PhysicalProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(PhysicalProtectionGroupParams.to_json())

# convert the object into a dict
physical_protection_group_params_dict = physical_protection_group_params_instance.to_dict()
# create an instance of PhysicalProtectionGroupParams from a dict
physical_protection_group_params_from_dict = PhysicalProtectionGroupParams.from_dict(physical_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


