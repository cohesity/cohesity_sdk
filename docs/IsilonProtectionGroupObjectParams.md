# IsilonProtectionGroupObjectParams

Specifies an object protected by a Isilon Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the object. | 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.isilon_protection_group_object_params import IsilonProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of IsilonProtectionGroupObjectParams from a JSON string
isilon_protection_group_object_params_instance = IsilonProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(IsilonProtectionGroupObjectParams.to_json())

# convert the object into a dict
isilon_protection_group_object_params_dict = isilon_protection_group_object_params_instance.to_dict()
# create an instance of IsilonProtectionGroupObjectParams from a dict
isilon_protection_group_object_params_from_dict = IsilonProtectionGroupObjectParams.from_dict(isilon_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


