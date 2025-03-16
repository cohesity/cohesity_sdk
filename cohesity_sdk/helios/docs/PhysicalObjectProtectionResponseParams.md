# PhysicalObjectProtectionResponseParams

Specifies the response parameters specific to Physical object protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_object_protection_type_params** | [**PhysicalFileProtectionGroupParams**](PhysicalFileProtectionGroupParams.md) |  | [optional] 
**object_protection_type** | **str** | Specifies the Physical Object Protection type. | 
**volume_object_protection_type_params** | [**PhysicalVolumeProtectionGroupParams**](PhysicalVolumeProtectionGroupParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.physical_object_protection_response_params import PhysicalObjectProtectionResponseParams

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalObjectProtectionResponseParams from a JSON string
physical_object_protection_response_params_instance = PhysicalObjectProtectionResponseParams.from_json(json)
# print the JSON string representation of the object
print(PhysicalObjectProtectionResponseParams.to_json())

# convert the object into a dict
physical_object_protection_response_params_dict = physical_object_protection_response_params_instance.to_dict()
# create an instance of PhysicalObjectProtectionResponseParams from a dict
physical_object_protection_response_params_from_dict = PhysicalObjectProtectionResponseParams.from_dict(physical_object_protection_response_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


