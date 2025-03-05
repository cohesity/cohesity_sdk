# NimbleProtectionGroupObjectParams

Specifies the object parameters to create Nimble Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the object. | 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.nimble_protection_group_object_params import NimbleProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleProtectionGroupObjectParams from a JSON string
nimble_protection_group_object_params_instance = NimbleProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(NimbleProtectionGroupObjectParams.to_json())

# convert the object into a dict
nimble_protection_group_object_params_dict = nimble_protection_group_object_params_instance.to_dict()
# create an instance of NimbleProtectionGroupObjectParams from a dict
nimble_protection_group_object_params_from_dict = NimbleProtectionGroupObjectParams.from_dict(nimble_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


